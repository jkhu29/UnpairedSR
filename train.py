import random

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import dataloader
from tfrecord.torch.dataset import TFRecordDataset

from tqdm import tqdm

import models
import config
import utils
import criterions


opt = config.get_options()
scale = opt.scale

# deveice init
CUDA_ENABLE = torch.cuda.is_available()
device = torch.device('cuda:0' if CUDA_ENABLE else 'cpu')

# seed init
manual_seed = opt.seed
random.seed(manual_seed)
torch.manual_seed(manual_seed)

# dataset init, train file need .tfrecord
description = {
    "lr": "byte",
    "hr": "byte",
    "size": "int",
}
train_dataset = TFRecordDataset("train.tfrecord", None, description, shuffle_queue_size=1024)
# do not shuffle
train_dataloader = dataloader.DataLoader(
    dataset=train_dataset,
    batch_size=opt.batch_size,
    num_workers=opt.workers,
    pin_memory=True,
    drop_last=True
)
length = 74432

valid_dataset = TFRecordDataset("valid.tfrecord", None, description)
valid_dataloader = dataloader.DataLoader(dataset=valid_dataset, batch_size=opt.batch_size, drop_last=True)

# models init
model_g_x2y = models.make_cleaning_net().to(device)
model_g_y2x = models.TransferNet().to(device)
model_sr = models.make_sr_net(scale=scale).to(device)
model_d_x = models.NLayerDiscriminator(1, norm_layer=nn.Identity).to(device)
model_d_y = models.NLayerDiscriminator(1, norm_layer=nn.Identity).to(device)
model_d_sr = models.NLayerDiscriminator(1, scale_factor=scale, norm_layer=nn.Identity).to(device)

# optim and scheduler init
opt_g_x2y = optim.Adam(model_g_x2y.parameters(), lr=opt.lr_g)
opt_g_y2x = optim.Adam(model_g_y2x.parameters(), lr=opt.lr_g)
opt_sr = optim.Adam(model_sr.parameters(), lr=opt.lr_g)
opt_d_x = optim.Adam(model_d_x.parameters(), lr=opt.lr_d)
opt_d_y = optim.Adam(model_d_y.parameters(), lr=opt.lr_d)
opt_d_sr = optim.Adam(model_d_sr.parameters(), lr=opt.lr_d)

lr_g_x2y = optim.lr_scheduler.MultiStepLR(opt_g_x2y, milestones=opt.lr_milestones, gamma=opt.lr_gamma)
lr_g_y2x = optim.lr_scheduler.MultiStepLR(opt_g_y2x, milestones=opt.lr_milestones, gamma=opt.lr_gamma)
lr_sr = optim.lr_scheduler.MultiStepLR(opt_sr, milestones=opt.lr_milestones, gamma=opt.lr_gamma)
lr_d_x = optim.lr_scheduler.MultiStepLR(opt_d_x, milestones=opt.lr_milestones, gamma=opt.lr_gamma)
lr_d_y = optim.lr_scheduler.MultiStepLR(opt_d_y, milestones=opt.lr_milestones, gamma=opt.lr_gamma)
lr_d_sr = optim.lr_scheduler.MultiStepLR(opt_d_sr, milestones=opt.lr_milestones, gamma=opt.lr_gamma)

# criterion init
geo_criterion = criterions.GeoLoss(model_g_x2y).to(device)
gan_criterion = criterions.GANLoss("lsgan").to(device)
l2_criterion = nn.MSELoss().to(device)

# train model
print("-----------------train-----------------")
for epoch in range(opt.niter):
    model_sr.train()
    epoch_losses_gen = utils.AverageMeter()
    epoch_losses_sr = utils.AverageMeter()

    with tqdm(total=(length - length % opt.batch_size)) as t:
        t.set_description('epoch: {}/{}'.format(epoch + 1, opt.niter))

        for record in train_dataloader:
            lr = record["lr"].reshape(
                opt.batch_size,
                1,
                record["size"][0],
                record["size"][0],
            ).float().to(device)
            # shape: (-1, 1, 32, 32)
            hr = record["hr"].reshape(
                opt.batch_size,
                1,
                record["size"][0] * scale,
                record["size"][0] * scale,
            ).float().to(device)
            # shape: (-1, 1, 64, 64)
            down_hr = F.interpolate(hr, scale_factor=0.5, mode="bicubic", align_corners=False)
            # shape: (-1, 1, 32, 32)
            n, _, h, w = lr.shape

            fake_lr = model_g_y2x(down_hr)
            recon_down_hr = model_g_x2y(fake_lr)
            fake_down_hr = model_g_x2y(lr)
            geo_down_hr = geo_criterion.geometry_ensemble(lr)
            idt_out = model_g_x2y(down_hr)
            sr_hr = model_sr(recon_down_hr)
            sr_lr = model_sr(fake_down_hr)

            model_d_x.train()
            pred_fake_lr = model_d_x(fake_lr.detach())
            pred_real_lr = model_d_x(lr)
            loss_d_x = gan_criterion(pred_real_lr, True, True) + gan_criterion(pred_fake_lr, False, True) * 0.5
            opt_d_x.zero_grad()
            loss_d_x.backward()
            opt_d_x.step()
            model_d_x.eval()

            model_d_y.train()
            pred_fake_hr = model_d_x(fake_down_hr.detach())
            pred_real_hr = model_d_x(down_hr)
            loss_d_y = gan_criterion(pred_real_hr, True, True) + gan_criterion(pred_fake_hr, False, True) * 0.5
            opt_d_y.zero_grad()
            loss_d_y.backward()
            opt_d_y.step()
            model_d_y.eval()

            model_d_sr.train()
            pred_sr_lr = model_d_sr(sr_lr.detach())
            pred_sr_hr = model_d_sr(sr_hr.detach())
            loss_d_sr = gan_criterion(pred_sr_lr, True, True) + gan_criterion(pred_sr_hr, False, True) * 0.5
            opt_d_sr.zero_grad()
            loss_d_sr.backward()
            opt_d_sr.step()
            model_d_sr.eval()

            model_g_x2y.train()
            model_g_y2x.train()
            opt_g_x2y.zero_grad()
            opt_g_y2x.zero_grad()
            pred_fake_lr = model_d_x(fake_lr)
            loss_gan_y2x = gan_criterion(pred_fake_lr, True, False)
            pred_fake_down_hr = model_d_y(fake_down_hr)
            pred_sr_hr = model_d_sr(sr_hr)
            loss_gan_x2y = gan_criterion(pred_fake_down_hr, True, False)

            loss_idt_x2y = l2_criterion(idt_out, down_hr)
            loss_cycle = l2_criterion(recon_down_hr, down_hr)
            loss_geo = l2_criterion(fake_down_hr, geo_down_hr)
            loss_d_sr = gan_criterion(pred_sr_hr, True, False)
            loss_total_gen = loss_gan_y2x + loss_gan_x2y + \
                opt.cyc_weight * loss_cycle + \
                opt.idt_weight * loss_idt_x2y + \
                opt.geo_weight * loss_geo + \
                opt.d_sr_weight * loss_d_sr
            loss_total_gen.backward()
            opt_g_x2y.step()
            opt_g_y2x.step()

            opt_sr.zero_grad()
            loss_sr = l2_criterion(model_sr(recon_down_hr.detach()), hr)
            loss_sr.backward()
            opt_sr.step()

            epoch_losses_gen.update(loss_total_gen.item(), len(lr))
            epoch_losses_sr.update(loss_sr.item(), len(lr))

            t.set_postfix(
                loss_total='{:.6f}'.format(epoch_losses_gen.avg),
                loss_sr='{:.6f}'.format(epoch_losses_sr.avg),
            )
            t.update(len(lr))

    lr_d_x.step()
    lr_d_y.step()
    lr_d_sr.step()
    lr_g_x2y.step()
    lr_g_y2x.step()
    lr_sr.step()

    torch.save(model_sr.state_dict(), "model_sr/epoch_{}.pth".format(epoch))
    torch.save(model_g_x2y.state_dict(), "model_x2y/epoch_{}.pth".format(epoch))
    torch.save(model_g_y2x.state_dict(), "model_y2x/epoch_{}.pth".format(epoch))
