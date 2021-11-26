from numpy.core.fromnumeric import reshape
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from collections import namedtuple
from functools import partial


class MeanShift(nn.Conv2d):
    def __init__(self, rgb_range, rgb_mean, rgb_std, sign=-1):
        super(MeanShift, self).__init__(3, 3, kernel_size=1)
        std = torch.Tensor(rgb_std)
        self.weight.data = torch.eye(3).view(3, 3, 1, 1)
        self.weight.data.div_(std.view(3, 1, 1, 1))
        self.bias.data = sign * rgb_range * torch.Tensor(rgb_mean)
        self.bias.data.div_(std)
        self.requires_grad = False


class RedBlock(nn.Module):
    def __init__(self, channels=64, kernel_size=3):
        super(ResBlock, self).__init__()
        self.m = nn.Sequential(
            nn.Conv2d(channels, channels, kernel_size, bias=True),
            nn.InstanceNorm2d(channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels, channels, kernel_size, bias=True),
            nn.InstanceNorm2d(channels),
        )

    def forward(self, x, scale):
        res = self.m(x) * scale
        return x + res


class TransferNet(nn.Module):
    def __init__(self, channels=64, z_feat=8, leaky_neg=0.2, n_resblock=6, bn=True):
        super(TransferNet, self).__init__()
        leaky_neg = leaky_neg
        z_channel = z_feat

        self.img_head = nn.Sequential(
            nn.Conv2d(1, channels // 2, kernel_size=5, padding=2, bias=True),
            nn.BatchNorm2d(channels // 2),
            nn.LeakyReLU(0.2, inplace=True),
            ResBlock(channels=channels // 2)
        )

        in_z = [nn.ConvTranspose2d(1, z_channel, 2, 2, 0, 0),  # 8 -> 16
                nn.LeakyReLU(leaky_neg, True),
                nn.ConvTranspose2d(z_channel, 2 * z_channel,
                                   2, 2, 0, 0),  # 16 -> 32
                nn.LeakyReLU(leaky_neg, True)]
        self.z_head = nn.Sequential(*in_z)

        self.merge = nn.Conv2d(channels // 2 + 2 *
                               z_channel, channels, 1, 1, 0)
        resblocks = [ResBlock(channels=channels) for _ in range(n_resblock)]
        self.res_blocks = nn.Sequential(*resblocks)
        self.fusion = nn.Sequential(
            nn.Conv2d(channels, channels // 2, 1),
            nn.LeakyReLU(leaky_neg, True),
            nn.Conv2d(channels // 2, channels // 4, 1),
            nn.LeakyReLU(leaky_neg, True),
            nn.Conv2d(channels // 4, 1, 1)
        )

    def forward(self, x):
        n, c, h, w = x.shape
        z = torch.randn((n, c, h // 4, w // 4)).to(x.device)
        x = self.img_head(x)
        z = self.z_head(z)
        out = self.merge(torch.cat((x, z), dim=1))
        out = self.res_blocks(out)
        out = self.fusion(out)
        return out


# --------
# RFDN: https://github.com/jkhu29/super-resolution/blob/master/rfdn/model.py
# --------
class ConvReLU(nn.Module):
    """ConvReLU: conv 64 * 3 * 3 + leakyrelu"""

    def __init__(self, in_channels, out_channels, withbn=True, kernel_size=3, stride=1, padding=1):
        super(ConvReLU, self).__init__()
        self.withbn = withbn
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size,
                              stride=stride, padding=padding, bias=False)
        self.bn = nn.InstanceNorm2d(out_channels)
        self.relu = nn.LeakyReLU(0.2, inplace=True)

    def forward(self, x):
        x = self.conv(x)
        if self.withbn:
            x = self.bn(x)
        x = self.relu(x)
        return x


class ResBlock(nn.Module):
    """ResBlock used by CartoonGAN and DeCartoonGAN"""

    def __init__(self, num_conv=1, channels=64):
        super(ResBlock, self).__init__()

        self.conv_relu = ConvReLU(channels, channels)
        self.conv = nn.Conv2d(channels, channels,
                              kernel_size=3, stride=1, padding=1, bias=False)

    def forward(self, x):
        x = self.conv_relu(x)
        res = x
        x = self.conv(x) + res
        return x


class ESA(nn.Module):
    def __init__(self, channels: int = 64, reduction: int = 4):
        super(ESA, self).__init__()
        mid_channels = channels // reduction
        self.conv1 = ConvReLU(channels, mid_channels,
                              kernel_size=1, stride=1, padding=0)
        self.conv_f = ConvReLU(mid_channels, mid_channels,
                               kernel_size=1, stride=1, padding=0)
        self.conv_max = ConvReLU(mid_channels, mid_channels)
        self.conv2 = ConvReLU(mid_channels, mid_channels,
                              kernel_size=3, stride=2, padding=0)
        self.conv3 = ResBlock(mid_channels, mid_channels)
        self.conv4 = ConvReLU(mid_channels, channels, kernel_size=1, padding=0)

    def forward(self, x):
        _, _, h, w = x.shape
        x = self.conv1(x)
        res = x
        x = self.conv2(x)
        x = F.max_pool2d(x, kernel_size=7, stride=3)
        x = self.conv_max(x)
        x = self.conv3(x)
        x = F.interpolate(x, (h, w), mode='bilinear', align_corners=False)
        res = self.conv_f(res)
        x = self.conv4(x + res)
        m = torch.sigmoid(x)
        return x * m


class RFDB(nn.Module):
    def __init__(self, in_channels: int = 64, reduction: int = 4):
        super(RFDB, self).__init__()
        distilled_channels = in_channels // reduction
        remaining_channels = in_channels
        self.c1_d = nn.Conv2d(
            in_channels, distilled_channels, kernel_size=1, padding=0)
        self.c1_r = nn.Conv2d(in_channels, remaining_channels,
                              kernel_size=3, stride=1, padding=1)
        self.c2_d = nn.Conv2d(remaining_channels,
                              distilled_channels, kernel_size=1, padding=0)
        self.c2_r = nn.Conv2d(
            remaining_channels, remaining_channels, kernel_size=3, stride=1, padding=1)
        self.c3_d = nn.Conv2d(remaining_channels,
                              distilled_channels, kernel_size=1, padding=0)
        self.c3_r = nn.Conv2d(
            remaining_channels, remaining_channels, kernel_size=3, stride=1, padding=1)
        self.c4 = nn.Conv2d(remaining_channels, distilled_channels,
                            kernel_size=3, stride=1, padding=1)
        self.c5 = nn.Conv2d(distilled_channels * 4,
                            in_channels, kernel_size=1, padding=0)
        self.act = nn.LeakyReLU(0.2, inplace=True)
        self.esa = ESA(in_channels)

    def forward(self, x):
        distilled_c1 = self.c1_d(x)
        r_c1 = self.c1_r(x)
        r_c1 = self.act(r_c1+x)

        distilled_c2 = self.act(self.c2_d(r_c1))
        r_c2 = (self.c2_r(r_c1))
        r_c2 = self.act(r_c2+r_c1)

        distilled_c3 = self.act(self.c3_d(r_c2))
        r_c3 = (self.c3_r(r_c2))
        r_c3 = self.act(r_c3+r_c2)

        r_c4 = self.act(self.c4(r_c3))

        out = torch.cat([distilled_c1, distilled_c2,
                        distilled_c3, r_c4], dim=1)
        out_fused = self.esa(self.c5(out))

        return out_fused


class RFDN(nn.Module):
    def __init__(self, channels: int = 64, scale: int = 4):
        super(RFDN, self).__init__()
        self.conv1 = nn.Conv2d(1, channels, 3, 1, 1)
        self.rfdb1 = RFDB(channels)
        self.rfdb2 = RFDB(channels)
        self.rfdb3 = RFDB(channels)
        self.rfdb4 = RFDB(channels)

        self.conv2 = ConvReLU(channels * 4, channels, kernel_size=1, padding=0)
        self.lr_conv = nn.Conv2d(channels, channels, 3, 1, 1)
        self.upsample = nn.Sequential(
            ConvReLU(channels, 1 * (scale ** 2)),
            nn.PixelShuffle(scale),
        )

    def forward(self, x):
        x = self.conv1(x)
        res = x
        x1 = self.rfdb1(x)
        x2 = self.rfdb2(x1)
        x3 = self.rfdb2(x2)
        x4 = self.rfdb2(x3)
        x = self.conv2(torch.cat([x1, x2, x3, x4], dim=1))
        x = self.lr_conv(x) + res
        x = self.upsample(x)
        return x


# ----------
# RCAN: https://github.com/jkhu29/super-resolution/blob/master/rcan/model.py
# ----------
class ChannelAttention(nn.Module):
    def __init__(self, num_features, reduction):
        super(ChannelAttention, self).__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(num_features, num_features //
                      reduction, kernel_size=1, bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(num_features // reduction,
                      num_features, kernel_size=1, bias=True),
            nn.Sigmoid()
        )

    def forward(self, x):
        return x + self.conv(x)


class RCAB(nn.Module):
    def __init__(self, num_features, reduction):
        super(RCAB, self).__init__()
        self.module = nn.Sequential(
            nn.Conv2d(num_features, num_features, kernel_size=3, padding=1),
            # nn.ReLU(inplace=True),
            nn.Conv2d(num_features, num_features, kernel_size=3, padding=1),
            ChannelAttention(num_features, reduction)
        )

    def forward(self, x):
        return x + self.module(x)


class RG(nn.Module):
    def __init__(self, num_features, num_rcab, reduction):
        super(RG, self).__init__()
        self.module = [RCAB(num_features, reduction) for _ in range(num_rcab)]
        self.module.append(
            nn.Conv2d(num_features, num_features, kernel_size=3, padding=1))
        self.module = nn.Sequential(*self.module)

    def forward(self, x):
        return x + self.module(x)


class RCAN(nn.Module):
    def __init__(self, scale=4, num_features=64, num_rg=5, num_rcab=10, reduction=8):
        super(RCAN, self).__init__()
        self.scale = scale

        self.conv1 = nn.Conv2d(1, num_features, kernel_size=3, padding=1)
        self.rgs = nn.Sequential(
            *[RG(num_features, num_rcab, reduction) for _ in range(num_rg)])
        self.conv2 = nn.Conv2d(num_features, num_features,
                               kernel_size=3, padding=1)
        # self.bn1 = nn.InstanceNorm2d(num_features)  # rethink

        self.upscale = nn.Sequential(
            *self.UpscaleBlock(num_features, num_features * (self.scale ** 2), self.scale))
        self.conv3 = nn.Conv2d(num_features, 1, kernel_size=3, padding=1)
        # self.dropout = nn.Dropout()

    def UpscaleBlock(self, in_channels, out_channels, num_scale):
        layers = [nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1),
                  nn.PixelShuffle(num_scale), ]
        return layers

    def forward(self, x):
        out = self.conv1(x)
        out1 = self.conv2(self.rgs(out))
        out = out + out1
        if self.scale != 1:
            res = F.interpolate(out, scale_factor=2.)
            out = self.upscale(out)
            out = self.conv3(out + res)
        else:
       	    out = self.conv3(out)
        return out


class VGG16(nn.Module):
    def __init__(self):
        super(VGG16, self).__init__()
        vgg_pretrained_features = torchvision.models.vgg16(
            pretrained=True).features
        self.slice1 = nn.Sequential()
        self.slice2 = nn.Sequential()
        self.slice3 = nn.Sequential()
        self.slice4 = nn.Sequential()
        self.slice5 = nn.Sequential()
        for x in range(4):
            self.slice1.add_module(str(x), vgg_pretrained_features[x])
        for x in range(4, 9):
            self.slice2.add_module(str(x), vgg_pretrained_features[x])
        for x in range(9, 16):
            self.slice3.add_module(str(x), vgg_pretrained_features[x])
        for x in range(16, 23):
            self.slice4.add_module(str(x), vgg_pretrained_features[x])
        for x in range(23, 30):
            self.slice5.add_module(str(x), vgg_pretrained_features[x])

    def forward(self, X):
        h = self.slice1(X)
        h_relu1_2 = h
        h = self.slice2(h)
        h_relu2_2 = h
        h = self.slice3(h)
        h_relu3_3 = h
        h = self.slice4(h)
        h_relu4_3 = h
        h = self.slice5(h)
        h_relu5_3 = h
        vgg_outputs = namedtuple(
            "VggOutputs", ["relu1_2", "relu2_2", "relu3_3", "relu4_3", "relu5_3"])
        out = vgg_outputs(h_relu1_2, h_relu2_2,
                          h_relu3_3, h_relu4_3, h_relu5_3)
        return out


class NLayerDiscriminator(nn.Module):
    def __init__(self, input_nc, ndf=64, n_layers=3, scale_factor=1, norm_layer=nn.BatchNorm2d):
        super(NLayerDiscriminator, self).__init__()
        # no need to use bias as BatchNorm2d has affine parameters
        if type(norm_layer) == partial:
            use_bias = norm_layer.func != nn.BatchNorm2d
        else:
            use_bias = norm_layer != nn.BatchNorm2d
        self.strides, self.n_down = self.comp_strides(scale_factor, n_layers)

        kw = 4
        padw = 1
        sequence = [nn.Conv2d(input_nc, ndf, kernel_size=kw,
                              stride=self.strides[0], padding=padw), nn.LeakyReLU(0.2, True)]
        nf_mult = 1
        nf_mult_prev = 1
        # gradually increase the number of filters
        for n in range(1, n_layers):
            nf_mult_prev = nf_mult
            nf_mult = min(2 ** n, 8)
            sequence += [
                nn.Conv2d(ndf * nf_mult_prev, ndf * nf_mult, kernel_size=kw,
                          stride=self.strides[n], padding=padw, bias=use_bias),
                norm_layer(ndf * nf_mult),
                nn.LeakyReLU(0.2, True)
            ]

        nf_mult_prev = nf_mult
        nf_mult = min(2 ** n_layers, 8)
        sequence += [
            nn.Conv2d(ndf * nf_mult_prev, ndf * nf_mult,
                      kernel_size=kw, stride=1, padding=padw, bias=use_bias),
            norm_layer(ndf * nf_mult),
            nn.LeakyReLU(0.2, True)
        ]

        sequence += [nn.Conv2d(ndf * nf_mult, 1,
                               kernel_size=kw, stride=1, padding=padw)]
        # output one channel prediction map
        self.model = nn.Sequential(*sequence)

    def forward(self, input):
        return self.model(input)

    def comp_strides(self, scale_factor, n_layers):
        strides = [1 for _ in range(n_layers)]
        assert scale_factor in [1, 2, 4]
        n_down = 0
        while True:
            scale_factor = scale_factor // 2
            if scale_factor <= 0:
                break
            n_down += 1
        for s in range(n_down):
            strides[s] = 2
        return strides, n_down


def make_cleaning_net():
    return RCAN(scale=1, num_rcab=5)


def make_sr_net(scale=2):
    return RCAN(scale=scale, num_rcab=10)


if __name__ == "__main__":
    from torchsummary import summary
    # a = RFDN(scale=2)
    b = RCAN(scale=1).cuda()
    # c = TransferNet()
    # print("RFDN: \n")
    # summary(a, (1, 64, 64))
    print("RCAN: \n")
    summary(b, (1, 64, 64))
    # print("Transfer: \n")
    # summary(c, (1, 64, 64))
