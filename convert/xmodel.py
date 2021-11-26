"""
use Vitis-ai: 1.4.0
"""
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_nndct.apis import torch_quantizer, dump_xmodel

import sys
sys.path.append("..")

import utils
from models import RCAN


def quantize(lr, quant_mode: str = "calib", deploy: bool = False, device=torch.device("cpu")):
    print("\nbegin {}:".format(quant_mode))
    sr_model = RCAN(scale=2, num_rcab=10)
    sr_params = torch.load("../model/pretrain_low.pth", map_location=torch.device('cpu'))
    sr_model.load_state_dict(sr_params)

    sr_img = sr_model(lr)
    cv2.imwrite("sr_img_{}.png".format(quant_mode), sr_img.squeeze().detach().numpy())

    print("\n================================ Quantizer ====================================")
    quantizer = torch_quantizer(
        quant_mode, sr_model, (lr), device=device
    )
    quant_model = quantizer.quant_model
    sr_img_int = quant_model(lr)
    cv2.imwrite("sr_img_int_{}.png".format(quant_mode), sr_img_int.squeeze().detach().numpy())

    quantizer.export_quant_config()
    if deploy:
        quantizer.export_xmodel(deploy_check=True)


if __name__ == "__main__":
    import time

    cnt = 0
    lr_img = cv2.imread("img.png", 0)
    h, w = lr_img.shape
    lr_img = cv2.resize(lr_img, (h // 4, w // 4))
    cv2.imwrite("img.png", lr_img)

    lr = torch.from_numpy(lr_img).unsqueeze(0).unsqueeze(0).float()

    t0 = time.time()
    quantize(lr, quant_mode="calib")
    quantize(lr, quant_mode="test", deploy=True)
    t1 = time.time()
    print("quantize and dumpy xmodel, spend: {}s".format(t1 - t0))
