# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class RCAN(torch.nn.Module):
    def __init__(self):
        super(RCAN, self).__init__()
        self.module_0 = py_nndct.nn.Input() #RCAN::input_0
        self.module_1 = py_nndct.nn.Module('const') #RCAN::2809
        self.module_2 = py_nndct.nn.Module('const') #RCAN::2826
        self.module_3 = py_nndct.nn.Conv2d(in_channels=1, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Conv2d[conv1]/input.2
        self.module_4 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[0]/input.3
        self.module_5 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[1]/input.4
        self.module_6 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.5
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.6
        self.module_8 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/469
        self.module_9 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/470
        self.module_10 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/472
        self.module_11 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[0]/input.7
        self.module_12 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[0]/input.8
        self.module_13 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[1]/input.9
        self.module_14 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.10
        self.module_15 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.11
        self.module_16 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/515
        self.module_17 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/516
        self.module_18 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/518
        self.module_19 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[1]/input.12
        self.module_20 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[0]/input.13
        self.module_21 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[1]/input.14
        self.module_22 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.15
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.16
        self.module_24 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/561
        self.module_25 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/562
        self.module_26 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/564
        self.module_27 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[2]/input.17
        self.module_28 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[0]/input.18
        self.module_29 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[1]/input.19
        self.module_30 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.20
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.21
        self.module_32 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/607
        self.module_33 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/608
        self.module_34 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/610
        self.module_35 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[3]/input.22
        self.module_36 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[0]/input.23
        self.module_37 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[1]/input.24
        self.module_38 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.25
        self.module_39 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.26
        self.module_40 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/653
        self.module_41 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/654
        self.module_42 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/656
        self.module_43 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[4]/input.27
        self.module_44 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[0]/input.28
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[1]/input.29
        self.module_46 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.30
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.31
        self.module_48 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/699
        self.module_49 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/700
        self.module_50 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/702
        self.module_51 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[5]/input.32
        self.module_52 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[0]/input.33
        self.module_53 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[1]/input.34
        self.module_54 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.35
        self.module_55 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.36
        self.module_56 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/745
        self.module_57 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/746
        self.module_58 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/748
        self.module_59 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[6]/input.37
        self.module_60 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[0]/input.38
        self.module_61 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[1]/input.39
        self.module_62 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.40
        self.module_63 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.41
        self.module_64 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/791
        self.module_65 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/792
        self.module_66 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/794
        self.module_67 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[7]/input.42
        self.module_68 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[0]/input.43
        self.module_69 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[1]/input.44
        self.module_70 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.45
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.46
        self.module_72 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/837
        self.module_73 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/838
        self.module_74 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/840
        self.module_75 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[8]/input.47
        self.module_76 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[0]/input.48
        self.module_77 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[1]/input.49
        self.module_78 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.50
        self.module_79 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.51
        self.module_80 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/883
        self.module_81 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/884
        self.module_82 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/886
        self.module_83 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/RCAB[9]/input.52
        self.module_84 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[0]/Sequential[module]/Conv2d[10]/898
        self.module_85 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[0]/input.53
        self.module_86 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[0]/input.54
        self.module_87 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[1]/input.55
        self.module_88 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.56
        self.module_89 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.57
        self.module_90 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/941
        self.module_91 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/942
        self.module_92 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/944
        self.module_93 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[0]/input.58
        self.module_94 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[0]/input.59
        self.module_95 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[1]/input.60
        self.module_96 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.61
        self.module_97 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.62
        self.module_98 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/987
        self.module_99 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/988
        self.module_100 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/990
        self.module_101 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[1]/input.63
        self.module_102 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[0]/input.64
        self.module_103 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[1]/input.65
        self.module_104 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.66
        self.module_105 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.67
        self.module_106 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1033
        self.module_107 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1034
        self.module_108 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/1036
        self.module_109 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[2]/input.68
        self.module_110 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[0]/input.69
        self.module_111 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[1]/input.70
        self.module_112 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.71
        self.module_113 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.72
        self.module_114 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1079
        self.module_115 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1080
        self.module_116 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/1082
        self.module_117 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[3]/input.73
        self.module_118 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[0]/input.74
        self.module_119 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[1]/input.75
        self.module_120 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.76
        self.module_121 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.77
        self.module_122 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1125
        self.module_123 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1126
        self.module_124 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/1128
        self.module_125 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[4]/input.78
        self.module_126 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[0]/input.79
        self.module_127 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[1]/input.80
        self.module_128 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.81
        self.module_129 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.82
        self.module_130 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1171
        self.module_131 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1172
        self.module_132 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/1174
        self.module_133 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[5]/input.83
        self.module_134 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[0]/input.84
        self.module_135 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[1]/input.85
        self.module_136 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.86
        self.module_137 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.87
        self.module_138 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1217
        self.module_139 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1218
        self.module_140 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/1220
        self.module_141 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[6]/input.88
        self.module_142 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[0]/input.89
        self.module_143 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[1]/input.90
        self.module_144 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.91
        self.module_145 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.92
        self.module_146 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1263
        self.module_147 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1264
        self.module_148 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/1266
        self.module_149 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[7]/input.93
        self.module_150 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[0]/input.94
        self.module_151 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[1]/input.95
        self.module_152 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.96
        self.module_153 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.97
        self.module_154 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1309
        self.module_155 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1310
        self.module_156 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/1312
        self.module_157 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[8]/input.98
        self.module_158 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[0]/input.99
        self.module_159 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[1]/input.100
        self.module_160 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.101
        self.module_161 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.102
        self.module_162 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1355
        self.module_163 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1356
        self.module_164 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/1358
        self.module_165 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/RCAB[9]/input.103
        self.module_166 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[1]/Sequential[module]/Conv2d[10]/1370
        self.module_167 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[1]/input.104
        self.module_168 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[0]/input.105
        self.module_169 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[1]/input.106
        self.module_170 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.107
        self.module_171 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.108
        self.module_172 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1413
        self.module_173 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1414
        self.module_174 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/1416
        self.module_175 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[0]/input.109
        self.module_176 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[0]/input.110
        self.module_177 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[1]/input.111
        self.module_178 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.112
        self.module_179 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.113
        self.module_180 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1459
        self.module_181 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1460
        self.module_182 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/1462
        self.module_183 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[1]/input.114
        self.module_184 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[0]/input.115
        self.module_185 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[1]/input.116
        self.module_186 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.117
        self.module_187 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.118
        self.module_188 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1505
        self.module_189 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1506
        self.module_190 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/1508
        self.module_191 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[2]/input.119
        self.module_192 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[0]/input.120
        self.module_193 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[1]/input.121
        self.module_194 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.122
        self.module_195 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.123
        self.module_196 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1551
        self.module_197 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1552
        self.module_198 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/1554
        self.module_199 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[3]/input.124
        self.module_200 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[0]/input.125
        self.module_201 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[1]/input.126
        self.module_202 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.127
        self.module_203 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.128
        self.module_204 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1597
        self.module_205 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1598
        self.module_206 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/1600
        self.module_207 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[4]/input.129
        self.module_208 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[0]/input.130
        self.module_209 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[1]/input.131
        self.module_210 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.132
        self.module_211 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.133
        self.module_212 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1643
        self.module_213 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1644
        self.module_214 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/1646
        self.module_215 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[5]/input.134
        self.module_216 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[0]/input.135
        self.module_217 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[1]/input.136
        self.module_218 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.137
        self.module_219 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.138
        self.module_220 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1689
        self.module_221 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1690
        self.module_222 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/1692
        self.module_223 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[6]/input.139
        self.module_224 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[0]/input.140
        self.module_225 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[1]/input.141
        self.module_226 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.142
        self.module_227 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.143
        self.module_228 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1735
        self.module_229 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1736
        self.module_230 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/1738
        self.module_231 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[7]/input.144
        self.module_232 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[0]/input.145
        self.module_233 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[1]/input.146
        self.module_234 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.147
        self.module_235 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.148
        self.module_236 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1781
        self.module_237 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1782
        self.module_238 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/1784
        self.module_239 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[8]/input.149
        self.module_240 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[0]/input.150
        self.module_241 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[1]/input.151
        self.module_242 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.152
        self.module_243 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.153
        self.module_244 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1827
        self.module_245 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1828
        self.module_246 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/1830
        self.module_247 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/RCAB[9]/input.154
        self.module_248 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[2]/Sequential[module]/Conv2d[10]/1842
        self.module_249 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[2]/input.155
        self.module_250 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[0]/input.156
        self.module_251 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[1]/input.157
        self.module_252 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.158
        self.module_253 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.159
        self.module_254 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1885
        self.module_255 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1886
        self.module_256 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/1888
        self.module_257 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[0]/input.160
        self.module_258 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[0]/input.161
        self.module_259 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[1]/input.162
        self.module_260 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.163
        self.module_261 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.164
        self.module_262 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1931
        self.module_263 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1932
        self.module_264 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/1934
        self.module_265 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[1]/input.165
        self.module_266 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[0]/input.166
        self.module_267 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[1]/input.167
        self.module_268 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.168
        self.module_269 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.169
        self.module_270 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/1977
        self.module_271 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/1978
        self.module_272 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/1980
        self.module_273 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[2]/input.170
        self.module_274 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[0]/input.171
        self.module_275 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[1]/input.172
        self.module_276 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.173
        self.module_277 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.174
        self.module_278 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2023
        self.module_279 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2024
        self.module_280 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/2026
        self.module_281 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[3]/input.175
        self.module_282 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[0]/input.176
        self.module_283 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[1]/input.177
        self.module_284 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.178
        self.module_285 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.179
        self.module_286 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2069
        self.module_287 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2070
        self.module_288 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/2072
        self.module_289 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[4]/input.180
        self.module_290 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[0]/input.181
        self.module_291 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[1]/input.182
        self.module_292 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.183
        self.module_293 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.184
        self.module_294 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2115
        self.module_295 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2116
        self.module_296 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/2118
        self.module_297 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[5]/input.185
        self.module_298 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[0]/input.186
        self.module_299 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[1]/input.187
        self.module_300 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.188
        self.module_301 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.189
        self.module_302 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2161
        self.module_303 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2162
        self.module_304 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/2164
        self.module_305 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[6]/input.190
        self.module_306 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[0]/input.191
        self.module_307 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[1]/input.192
        self.module_308 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.193
        self.module_309 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.194
        self.module_310 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2207
        self.module_311 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2208
        self.module_312 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/2210
        self.module_313 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[7]/input.195
        self.module_314 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[0]/input.196
        self.module_315 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[1]/input.197
        self.module_316 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.198
        self.module_317 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.199
        self.module_318 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2253
        self.module_319 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2254
        self.module_320 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/2256
        self.module_321 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[8]/input.200
        self.module_322 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[0]/input.201
        self.module_323 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[1]/input.202
        self.module_324 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.203
        self.module_325 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.204
        self.module_326 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2299
        self.module_327 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2300
        self.module_328 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/2302
        self.module_329 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/RCAB[9]/input.205
        self.module_330 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[3]/Sequential[module]/Conv2d[10]/2314
        self.module_331 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[3]/input.206
        self.module_332 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[0]/input.207
        self.module_333 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/Conv2d[1]/input.208
        self.module_334 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.209
        self.module_335 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.210
        self.module_336 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2357
        self.module_337 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2358
        self.module_338 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/Sequential[module]/ChannelAttention[2]/2360
        self.module_339 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[0]/input.211
        self.module_340 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[0]/input.212
        self.module_341 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/Conv2d[1]/input.213
        self.module_342 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.214
        self.module_343 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.215
        self.module_344 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2403
        self.module_345 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2404
        self.module_346 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/Sequential[module]/ChannelAttention[2]/2406
        self.module_347 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[1]/input.216
        self.module_348 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[0]/input.217
        self.module_349 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/Conv2d[1]/input.218
        self.module_350 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.219
        self.module_351 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.220
        self.module_352 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2449
        self.module_353 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2450
        self.module_354 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/Sequential[module]/ChannelAttention[2]/2452
        self.module_355 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[2]/input.221
        self.module_356 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[0]/input.222
        self.module_357 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/Conv2d[1]/input.223
        self.module_358 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.224
        self.module_359 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.225
        self.module_360 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2495
        self.module_361 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2496
        self.module_362 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/Sequential[module]/ChannelAttention[2]/2498
        self.module_363 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[3]/input.226
        self.module_364 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[0]/input.227
        self.module_365 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/Conv2d[1]/input.228
        self.module_366 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.229
        self.module_367 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.230
        self.module_368 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2541
        self.module_369 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2542
        self.module_370 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/Sequential[module]/ChannelAttention[2]/2544
        self.module_371 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[4]/input.231
        self.module_372 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[0]/input.232
        self.module_373 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/Conv2d[1]/input.233
        self.module_374 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.234
        self.module_375 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.235
        self.module_376 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2587
        self.module_377 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2588
        self.module_378 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/Sequential[module]/ChannelAttention[2]/2590
        self.module_379 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[5]/input.236
        self.module_380 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[0]/input.237
        self.module_381 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/Conv2d[1]/input.238
        self.module_382 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.239
        self.module_383 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.240
        self.module_384 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2633
        self.module_385 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2634
        self.module_386 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/Sequential[module]/ChannelAttention[2]/2636
        self.module_387 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[6]/input.241
        self.module_388 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[0]/input.242
        self.module_389 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/Conv2d[1]/input.243
        self.module_390 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.244
        self.module_391 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.245
        self.module_392 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2679
        self.module_393 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2680
        self.module_394 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/Sequential[module]/ChannelAttention[2]/2682
        self.module_395 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[7]/input.246
        self.module_396 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[0]/input.247
        self.module_397 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/Conv2d[1]/input.248
        self.module_398 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.249
        self.module_399 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.250
        self.module_400 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2725
        self.module_401 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2726
        self.module_402 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/Sequential[module]/ChannelAttention[2]/2728
        self.module_403 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[8]/input.251
        self.module_404 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[0]/input.252
        self.module_405 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/Conv2d[1]/input.253
        self.module_406 = py_nndct.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[0]/input.254
        self.module_407 = py_nndct.nn.ReLU(inplace=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/ReLU[1]/input.255
        self.module_408 = py_nndct.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Conv2d[2]/2771
        self.module_409 = py_nndct.nn.Sigmoid() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/Sequential[conv]/Sigmoid[3]/2772
        self.module_410 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/Sequential[module]/ChannelAttention[2]/2774
        self.module_411 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/RCAB[9]/input.256
        self.module_412 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[rgs]/RG[4]/Sequential[module]/Conv2d[10]/2786
        self.module_413 = py_nndct.nn.Add() #RCAN::RCAN/Sequential[rgs]/RG[4]/input.257
        self.module_414 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Conv2d[conv2]/2798
        self.module_415 = py_nndct.nn.Add() #RCAN::RCAN/input.258
        self.module_416 = py_nndct.nn.Module('shape') #RCAN::RCAN/2802
        self.module_417 = py_nndct.nn.Module('tensor') #RCAN::RCAN/2803
        self.module_418 = py_nndct.nn.Module('cast') #RCAN::RCAN/2808
        self.module_419 = py_nndct.nn.Module('mul') #RCAN::RCAN/2810
        self.module_420 = py_nndct.nn.Module('cast') #RCAN::RCAN/2815
        self.module_421 = py_nndct.nn.Module('floor') #RCAN::RCAN/2816
        self.module_422 = py_nndct.nn.Int() #RCAN::RCAN/2817
        self.module_423 = py_nndct.nn.Module('shape') #RCAN::RCAN/2819
        self.module_424 = py_nndct.nn.Module('tensor') #RCAN::RCAN/2820
        self.module_425 = py_nndct.nn.Module('cast') #RCAN::RCAN/2825
        self.module_426 = py_nndct.nn.Module('mul') #RCAN::RCAN/2827
        self.module_427 = py_nndct.nn.Module('cast') #RCAN::RCAN/2832
        self.module_428 = py_nndct.nn.Module('floor') #RCAN::RCAN/2833
        self.module_429 = py_nndct.nn.Int() #RCAN::RCAN/2834
        self.module_430 = py_nndct.nn.Interpolate() #RCAN::RCAN/2836
        self.module_431 = py_nndct.nn.Conv2d(in_channels=64, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Sequential[upscale]/Conv2d[0]/2846
        self.module_432 = py_nndct.nn.Module('pixel_shuffle',upscale_factor=2) #RCAN::RCAN/Sequential[upscale]/PixelShuffle[1]/2848
        self.module_433 = py_nndct.nn.Add() #RCAN::RCAN/input
        self.module_434 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #RCAN::RCAN/Conv2d[conv3]/2860

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(dtype=torch.float, device='cpu', data=2.0)
        self.output_module_2 = self.module_2(dtype=torch.float, device='cpu', data=2.0)
        self.output_module_3 = self.module_3(self.output_module_0)
        self.output_module_4 = self.module_4(self.output_module_3)
        self.output_module_5 = self.module_5(self.output_module_4)
        self.output_module_6 = self.module_6(self.output_module_5)
        self.output_module_7 = self.module_7(self.output_module_6)
        self.output_module_8 = self.module_8(self.output_module_7)
        self.output_module_9 = self.module_9(self.output_module_8)
        self.output_module_10 = self.module_10(alpha=1, other=self.output_module_9, input=self.output_module_5)
        self.output_module_11 = self.module_11(alpha=1, other=self.output_module_10, input=self.output_module_3)
        self.output_module_12 = self.module_12(self.output_module_11)
        self.output_module_13 = self.module_13(self.output_module_12)
        self.output_module_14 = self.module_14(self.output_module_13)
        self.output_module_15 = self.module_15(self.output_module_14)
        self.output_module_16 = self.module_16(self.output_module_15)
        self.output_module_17 = self.module_17(self.output_module_16)
        self.output_module_18 = self.module_18(alpha=1, other=self.output_module_17, input=self.output_module_13)
        self.output_module_19 = self.module_19(alpha=1, other=self.output_module_18, input=self.output_module_11)
        self.output_module_20 = self.module_20(self.output_module_19)
        self.output_module_21 = self.module_21(self.output_module_20)
        self.output_module_22 = self.module_22(self.output_module_21)
        self.output_module_23 = self.module_23(self.output_module_22)
        self.output_module_24 = self.module_24(self.output_module_23)
        self.output_module_25 = self.module_25(self.output_module_24)
        self.output_module_26 = self.module_26(alpha=1, other=self.output_module_25, input=self.output_module_21)
        self.output_module_27 = self.module_27(alpha=1, other=self.output_module_26, input=self.output_module_19)
        self.output_module_28 = self.module_28(self.output_module_27)
        self.output_module_29 = self.module_29(self.output_module_28)
        self.output_module_30 = self.module_30(self.output_module_29)
        self.output_module_31 = self.module_31(self.output_module_30)
        self.output_module_32 = self.module_32(self.output_module_31)
        self.output_module_33 = self.module_33(self.output_module_32)
        self.output_module_34 = self.module_34(alpha=1, other=self.output_module_33, input=self.output_module_29)
        self.output_module_35 = self.module_35(alpha=1, other=self.output_module_34, input=self.output_module_27)
        self.output_module_36 = self.module_36(self.output_module_35)
        self.output_module_37 = self.module_37(self.output_module_36)
        self.output_module_38 = self.module_38(self.output_module_37)
        self.output_module_39 = self.module_39(self.output_module_38)
        self.output_module_40 = self.module_40(self.output_module_39)
        self.output_module_41 = self.module_41(self.output_module_40)
        self.output_module_42 = self.module_42(alpha=1, other=self.output_module_41, input=self.output_module_37)
        self.output_module_43 = self.module_43(alpha=1, other=self.output_module_42, input=self.output_module_35)
        self.output_module_44 = self.module_44(self.output_module_43)
        self.output_module_45 = self.module_45(self.output_module_44)
        self.output_module_46 = self.module_46(self.output_module_45)
        self.output_module_47 = self.module_47(self.output_module_46)
        self.output_module_48 = self.module_48(self.output_module_47)
        self.output_module_49 = self.module_49(self.output_module_48)
        self.output_module_50 = self.module_50(alpha=1, other=self.output_module_49, input=self.output_module_45)
        self.output_module_51 = self.module_51(alpha=1, other=self.output_module_50, input=self.output_module_43)
        self.output_module_52 = self.module_52(self.output_module_51)
        self.output_module_53 = self.module_53(self.output_module_52)
        self.output_module_54 = self.module_54(self.output_module_53)
        self.output_module_55 = self.module_55(self.output_module_54)
        self.output_module_56 = self.module_56(self.output_module_55)
        self.output_module_57 = self.module_57(self.output_module_56)
        self.output_module_58 = self.module_58(alpha=1, other=self.output_module_57, input=self.output_module_53)
        self.output_module_59 = self.module_59(alpha=1, other=self.output_module_58, input=self.output_module_51)
        self.output_module_60 = self.module_60(self.output_module_59)
        self.output_module_61 = self.module_61(self.output_module_60)
        self.output_module_62 = self.module_62(self.output_module_61)
        self.output_module_63 = self.module_63(self.output_module_62)
        self.output_module_64 = self.module_64(self.output_module_63)
        self.output_module_65 = self.module_65(self.output_module_64)
        self.output_module_66 = self.module_66(alpha=1, other=self.output_module_65, input=self.output_module_61)
        self.output_module_67 = self.module_67(alpha=1, other=self.output_module_66, input=self.output_module_59)
        self.output_module_68 = self.module_68(self.output_module_67)
        self.output_module_69 = self.module_69(self.output_module_68)
        self.output_module_70 = self.module_70(self.output_module_69)
        self.output_module_71 = self.module_71(self.output_module_70)
        self.output_module_72 = self.module_72(self.output_module_71)
        self.output_module_73 = self.module_73(self.output_module_72)
        self.output_module_74 = self.module_74(alpha=1, other=self.output_module_73, input=self.output_module_69)
        self.output_module_75 = self.module_75(alpha=1, other=self.output_module_74, input=self.output_module_67)
        self.output_module_76 = self.module_76(self.output_module_75)
        self.output_module_77 = self.module_77(self.output_module_76)
        self.output_module_78 = self.module_78(self.output_module_77)
        self.output_module_79 = self.module_79(self.output_module_78)
        self.output_module_80 = self.module_80(self.output_module_79)
        self.output_module_81 = self.module_81(self.output_module_80)
        self.output_module_82 = self.module_82(alpha=1, other=self.output_module_81, input=self.output_module_77)
        self.output_module_83 = self.module_83(alpha=1, other=self.output_module_82, input=self.output_module_75)
        self.output_module_84 = self.module_84(self.output_module_83)
        self.output_module_85 = self.module_85(alpha=1, other=self.output_module_84, input=self.output_module_3)
        self.output_module_86 = self.module_86(self.output_module_85)
        self.output_module_87 = self.module_87(self.output_module_86)
        self.output_module_88 = self.module_88(self.output_module_87)
        self.output_module_89 = self.module_89(self.output_module_88)
        self.output_module_90 = self.module_90(self.output_module_89)
        self.output_module_91 = self.module_91(self.output_module_90)
        self.output_module_92 = self.module_92(alpha=1, other=self.output_module_91, input=self.output_module_87)
        self.output_module_93 = self.module_93(alpha=1, other=self.output_module_92, input=self.output_module_85)
        self.output_module_94 = self.module_94(self.output_module_93)
        self.output_module_95 = self.module_95(self.output_module_94)
        self.output_module_96 = self.module_96(self.output_module_95)
        self.output_module_97 = self.module_97(self.output_module_96)
        self.output_module_98 = self.module_98(self.output_module_97)
        self.output_module_99 = self.module_99(self.output_module_98)
        self.output_module_100 = self.module_100(alpha=1, other=self.output_module_99, input=self.output_module_95)
        self.output_module_101 = self.module_101(alpha=1, other=self.output_module_100, input=self.output_module_93)
        self.output_module_102 = self.module_102(self.output_module_101)
        self.output_module_103 = self.module_103(self.output_module_102)
        self.output_module_104 = self.module_104(self.output_module_103)
        self.output_module_105 = self.module_105(self.output_module_104)
        self.output_module_106 = self.module_106(self.output_module_105)
        self.output_module_107 = self.module_107(self.output_module_106)
        self.output_module_108 = self.module_108(alpha=1, other=self.output_module_107, input=self.output_module_103)
        self.output_module_109 = self.module_109(alpha=1, other=self.output_module_108, input=self.output_module_101)
        self.output_module_110 = self.module_110(self.output_module_109)
        self.output_module_111 = self.module_111(self.output_module_110)
        self.output_module_112 = self.module_112(self.output_module_111)
        self.output_module_113 = self.module_113(self.output_module_112)
        self.output_module_114 = self.module_114(self.output_module_113)
        self.output_module_115 = self.module_115(self.output_module_114)
        self.output_module_116 = self.module_116(alpha=1, other=self.output_module_115, input=self.output_module_111)
        self.output_module_117 = self.module_117(alpha=1, other=self.output_module_116, input=self.output_module_109)
        self.output_module_118 = self.module_118(self.output_module_117)
        self.output_module_119 = self.module_119(self.output_module_118)
        self.output_module_120 = self.module_120(self.output_module_119)
        self.output_module_121 = self.module_121(self.output_module_120)
        self.output_module_122 = self.module_122(self.output_module_121)
        self.output_module_123 = self.module_123(self.output_module_122)
        self.output_module_124 = self.module_124(alpha=1, other=self.output_module_123, input=self.output_module_119)
        self.output_module_125 = self.module_125(alpha=1, other=self.output_module_124, input=self.output_module_117)
        self.output_module_126 = self.module_126(self.output_module_125)
        self.output_module_127 = self.module_127(self.output_module_126)
        self.output_module_128 = self.module_128(self.output_module_127)
        self.output_module_129 = self.module_129(self.output_module_128)
        self.output_module_130 = self.module_130(self.output_module_129)
        self.output_module_131 = self.module_131(self.output_module_130)
        self.output_module_132 = self.module_132(alpha=1, other=self.output_module_131, input=self.output_module_127)
        self.output_module_133 = self.module_133(alpha=1, other=self.output_module_132, input=self.output_module_125)
        self.output_module_134 = self.module_134(self.output_module_133)
        self.output_module_135 = self.module_135(self.output_module_134)
        self.output_module_136 = self.module_136(self.output_module_135)
        self.output_module_137 = self.module_137(self.output_module_136)
        self.output_module_138 = self.module_138(self.output_module_137)
        self.output_module_139 = self.module_139(self.output_module_138)
        self.output_module_140 = self.module_140(alpha=1, other=self.output_module_139, input=self.output_module_135)
        self.output_module_141 = self.module_141(alpha=1, other=self.output_module_140, input=self.output_module_133)
        self.output_module_142 = self.module_142(self.output_module_141)
        self.output_module_143 = self.module_143(self.output_module_142)
        self.output_module_144 = self.module_144(self.output_module_143)
        self.output_module_145 = self.module_145(self.output_module_144)
        self.output_module_146 = self.module_146(self.output_module_145)
        self.output_module_147 = self.module_147(self.output_module_146)
        self.output_module_148 = self.module_148(alpha=1, other=self.output_module_147, input=self.output_module_143)
        self.output_module_149 = self.module_149(alpha=1, other=self.output_module_148, input=self.output_module_141)
        self.output_module_150 = self.module_150(self.output_module_149)
        self.output_module_151 = self.module_151(self.output_module_150)
        self.output_module_152 = self.module_152(self.output_module_151)
        self.output_module_153 = self.module_153(self.output_module_152)
        self.output_module_154 = self.module_154(self.output_module_153)
        self.output_module_155 = self.module_155(self.output_module_154)
        self.output_module_156 = self.module_156(alpha=1, other=self.output_module_155, input=self.output_module_151)
        self.output_module_157 = self.module_157(alpha=1, other=self.output_module_156, input=self.output_module_149)
        self.output_module_158 = self.module_158(self.output_module_157)
        self.output_module_159 = self.module_159(self.output_module_158)
        self.output_module_160 = self.module_160(self.output_module_159)
        self.output_module_161 = self.module_161(self.output_module_160)
        self.output_module_162 = self.module_162(self.output_module_161)
        self.output_module_163 = self.module_163(self.output_module_162)
        self.output_module_164 = self.module_164(alpha=1, other=self.output_module_163, input=self.output_module_159)
        self.output_module_165 = self.module_165(alpha=1, other=self.output_module_164, input=self.output_module_157)
        self.output_module_166 = self.module_166(self.output_module_165)
        self.output_module_167 = self.module_167(alpha=1, other=self.output_module_166, input=self.output_module_85)
        self.output_module_168 = self.module_168(self.output_module_167)
        self.output_module_169 = self.module_169(self.output_module_168)
        self.output_module_170 = self.module_170(self.output_module_169)
        self.output_module_171 = self.module_171(self.output_module_170)
        self.output_module_172 = self.module_172(self.output_module_171)
        self.output_module_173 = self.module_173(self.output_module_172)
        self.output_module_174 = self.module_174(alpha=1, other=self.output_module_173, input=self.output_module_169)
        self.output_module_175 = self.module_175(alpha=1, other=self.output_module_174, input=self.output_module_167)
        self.output_module_176 = self.module_176(self.output_module_175)
        self.output_module_177 = self.module_177(self.output_module_176)
        self.output_module_178 = self.module_178(self.output_module_177)
        self.output_module_179 = self.module_179(self.output_module_178)
        self.output_module_180 = self.module_180(self.output_module_179)
        self.output_module_181 = self.module_181(self.output_module_180)
        self.output_module_182 = self.module_182(alpha=1, other=self.output_module_181, input=self.output_module_177)
        self.output_module_183 = self.module_183(alpha=1, other=self.output_module_182, input=self.output_module_175)
        self.output_module_184 = self.module_184(self.output_module_183)
        self.output_module_185 = self.module_185(self.output_module_184)
        self.output_module_186 = self.module_186(self.output_module_185)
        self.output_module_187 = self.module_187(self.output_module_186)
        self.output_module_188 = self.module_188(self.output_module_187)
        self.output_module_189 = self.module_189(self.output_module_188)
        self.output_module_190 = self.module_190(alpha=1, other=self.output_module_189, input=self.output_module_185)
        self.output_module_191 = self.module_191(alpha=1, other=self.output_module_190, input=self.output_module_183)
        self.output_module_192 = self.module_192(self.output_module_191)
        self.output_module_193 = self.module_193(self.output_module_192)
        self.output_module_194 = self.module_194(self.output_module_193)
        self.output_module_195 = self.module_195(self.output_module_194)
        self.output_module_196 = self.module_196(self.output_module_195)
        self.output_module_197 = self.module_197(self.output_module_196)
        self.output_module_198 = self.module_198(alpha=1, other=self.output_module_197, input=self.output_module_193)
        self.output_module_199 = self.module_199(alpha=1, other=self.output_module_198, input=self.output_module_191)
        self.output_module_200 = self.module_200(self.output_module_199)
        self.output_module_201 = self.module_201(self.output_module_200)
        self.output_module_202 = self.module_202(self.output_module_201)
        self.output_module_203 = self.module_203(self.output_module_202)
        self.output_module_204 = self.module_204(self.output_module_203)
        self.output_module_205 = self.module_205(self.output_module_204)
        self.output_module_206 = self.module_206(alpha=1, other=self.output_module_205, input=self.output_module_201)
        self.output_module_207 = self.module_207(alpha=1, other=self.output_module_206, input=self.output_module_199)
        self.output_module_208 = self.module_208(self.output_module_207)
        self.output_module_209 = self.module_209(self.output_module_208)
        self.output_module_210 = self.module_210(self.output_module_209)
        self.output_module_211 = self.module_211(self.output_module_210)
        self.output_module_212 = self.module_212(self.output_module_211)
        self.output_module_213 = self.module_213(self.output_module_212)
        self.output_module_214 = self.module_214(alpha=1, other=self.output_module_213, input=self.output_module_209)
        self.output_module_215 = self.module_215(alpha=1, other=self.output_module_214, input=self.output_module_207)
        self.output_module_216 = self.module_216(self.output_module_215)
        self.output_module_217 = self.module_217(self.output_module_216)
        self.output_module_218 = self.module_218(self.output_module_217)
        self.output_module_219 = self.module_219(self.output_module_218)
        self.output_module_220 = self.module_220(self.output_module_219)
        self.output_module_221 = self.module_221(self.output_module_220)
        self.output_module_222 = self.module_222(alpha=1, other=self.output_module_221, input=self.output_module_217)
        self.output_module_223 = self.module_223(alpha=1, other=self.output_module_222, input=self.output_module_215)
        self.output_module_224 = self.module_224(self.output_module_223)
        self.output_module_225 = self.module_225(self.output_module_224)
        self.output_module_226 = self.module_226(self.output_module_225)
        self.output_module_227 = self.module_227(self.output_module_226)
        self.output_module_228 = self.module_228(self.output_module_227)
        self.output_module_229 = self.module_229(self.output_module_228)
        self.output_module_230 = self.module_230(alpha=1, other=self.output_module_229, input=self.output_module_225)
        self.output_module_231 = self.module_231(alpha=1, other=self.output_module_230, input=self.output_module_223)
        self.output_module_232 = self.module_232(self.output_module_231)
        self.output_module_233 = self.module_233(self.output_module_232)
        self.output_module_234 = self.module_234(self.output_module_233)
        self.output_module_235 = self.module_235(self.output_module_234)
        self.output_module_236 = self.module_236(self.output_module_235)
        self.output_module_237 = self.module_237(self.output_module_236)
        self.output_module_238 = self.module_238(alpha=1, other=self.output_module_237, input=self.output_module_233)
        self.output_module_239 = self.module_239(alpha=1, other=self.output_module_238, input=self.output_module_231)
        self.output_module_240 = self.module_240(self.output_module_239)
        self.output_module_241 = self.module_241(self.output_module_240)
        self.output_module_242 = self.module_242(self.output_module_241)
        self.output_module_243 = self.module_243(self.output_module_242)
        self.output_module_244 = self.module_244(self.output_module_243)
        self.output_module_245 = self.module_245(self.output_module_244)
        self.output_module_246 = self.module_246(alpha=1, other=self.output_module_245, input=self.output_module_241)
        self.output_module_247 = self.module_247(alpha=1, other=self.output_module_246, input=self.output_module_239)
        self.output_module_248 = self.module_248(self.output_module_247)
        self.output_module_249 = self.module_249(alpha=1, other=self.output_module_248, input=self.output_module_167)
        self.output_module_250 = self.module_250(self.output_module_249)
        self.output_module_251 = self.module_251(self.output_module_250)
        self.output_module_252 = self.module_252(self.output_module_251)
        self.output_module_253 = self.module_253(self.output_module_252)
        self.output_module_254 = self.module_254(self.output_module_253)
        self.output_module_255 = self.module_255(self.output_module_254)
        self.output_module_256 = self.module_256(alpha=1, other=self.output_module_255, input=self.output_module_251)
        self.output_module_257 = self.module_257(alpha=1, other=self.output_module_256, input=self.output_module_249)
        self.output_module_258 = self.module_258(self.output_module_257)
        self.output_module_259 = self.module_259(self.output_module_258)
        self.output_module_260 = self.module_260(self.output_module_259)
        self.output_module_261 = self.module_261(self.output_module_260)
        self.output_module_262 = self.module_262(self.output_module_261)
        self.output_module_263 = self.module_263(self.output_module_262)
        self.output_module_264 = self.module_264(alpha=1, other=self.output_module_263, input=self.output_module_259)
        self.output_module_265 = self.module_265(alpha=1, other=self.output_module_264, input=self.output_module_257)
        self.output_module_266 = self.module_266(self.output_module_265)
        self.output_module_267 = self.module_267(self.output_module_266)
        self.output_module_268 = self.module_268(self.output_module_267)
        self.output_module_269 = self.module_269(self.output_module_268)
        self.output_module_270 = self.module_270(self.output_module_269)
        self.output_module_271 = self.module_271(self.output_module_270)
        self.output_module_272 = self.module_272(alpha=1, other=self.output_module_271, input=self.output_module_267)
        self.output_module_273 = self.module_273(alpha=1, other=self.output_module_272, input=self.output_module_265)
        self.output_module_274 = self.module_274(self.output_module_273)
        self.output_module_275 = self.module_275(self.output_module_274)
        self.output_module_276 = self.module_276(self.output_module_275)
        self.output_module_277 = self.module_277(self.output_module_276)
        self.output_module_278 = self.module_278(self.output_module_277)
        self.output_module_279 = self.module_279(self.output_module_278)
        self.output_module_280 = self.module_280(alpha=1, other=self.output_module_279, input=self.output_module_275)
        self.output_module_281 = self.module_281(alpha=1, other=self.output_module_280, input=self.output_module_273)
        self.output_module_282 = self.module_282(self.output_module_281)
        self.output_module_283 = self.module_283(self.output_module_282)
        self.output_module_284 = self.module_284(self.output_module_283)
        self.output_module_285 = self.module_285(self.output_module_284)
        self.output_module_286 = self.module_286(self.output_module_285)
        self.output_module_287 = self.module_287(self.output_module_286)
        self.output_module_288 = self.module_288(alpha=1, other=self.output_module_287, input=self.output_module_283)
        self.output_module_289 = self.module_289(alpha=1, other=self.output_module_288, input=self.output_module_281)
        self.output_module_290 = self.module_290(self.output_module_289)
        self.output_module_291 = self.module_291(self.output_module_290)
        self.output_module_292 = self.module_292(self.output_module_291)
        self.output_module_293 = self.module_293(self.output_module_292)
        self.output_module_294 = self.module_294(self.output_module_293)
        self.output_module_295 = self.module_295(self.output_module_294)
        self.output_module_296 = self.module_296(alpha=1, other=self.output_module_295, input=self.output_module_291)
        self.output_module_297 = self.module_297(alpha=1, other=self.output_module_296, input=self.output_module_289)
        self.output_module_298 = self.module_298(self.output_module_297)
        self.output_module_299 = self.module_299(self.output_module_298)
        self.output_module_300 = self.module_300(self.output_module_299)
        self.output_module_301 = self.module_301(self.output_module_300)
        self.output_module_302 = self.module_302(self.output_module_301)
        self.output_module_303 = self.module_303(self.output_module_302)
        self.output_module_304 = self.module_304(alpha=1, other=self.output_module_303, input=self.output_module_299)
        self.output_module_305 = self.module_305(alpha=1, other=self.output_module_304, input=self.output_module_297)
        self.output_module_306 = self.module_306(self.output_module_305)
        self.output_module_307 = self.module_307(self.output_module_306)
        self.output_module_308 = self.module_308(self.output_module_307)
        self.output_module_309 = self.module_309(self.output_module_308)
        self.output_module_310 = self.module_310(self.output_module_309)
        self.output_module_311 = self.module_311(self.output_module_310)
        self.output_module_312 = self.module_312(alpha=1, other=self.output_module_311, input=self.output_module_307)
        self.output_module_313 = self.module_313(alpha=1, other=self.output_module_312, input=self.output_module_305)
        self.output_module_314 = self.module_314(self.output_module_313)
        self.output_module_315 = self.module_315(self.output_module_314)
        self.output_module_316 = self.module_316(self.output_module_315)
        self.output_module_317 = self.module_317(self.output_module_316)
        self.output_module_318 = self.module_318(self.output_module_317)
        self.output_module_319 = self.module_319(self.output_module_318)
        self.output_module_320 = self.module_320(alpha=1, other=self.output_module_319, input=self.output_module_315)
        self.output_module_321 = self.module_321(alpha=1, other=self.output_module_320, input=self.output_module_313)
        self.output_module_322 = self.module_322(self.output_module_321)
        self.output_module_323 = self.module_323(self.output_module_322)
        self.output_module_324 = self.module_324(self.output_module_323)
        self.output_module_325 = self.module_325(self.output_module_324)
        self.output_module_326 = self.module_326(self.output_module_325)
        self.output_module_327 = self.module_327(self.output_module_326)
        self.output_module_328 = self.module_328(alpha=1, other=self.output_module_327, input=self.output_module_323)
        self.output_module_329 = self.module_329(alpha=1, other=self.output_module_328, input=self.output_module_321)
        self.output_module_330 = self.module_330(self.output_module_329)
        self.output_module_331 = self.module_331(alpha=1, other=self.output_module_330, input=self.output_module_249)
        self.output_module_332 = self.module_332(self.output_module_331)
        self.output_module_333 = self.module_333(self.output_module_332)
        self.output_module_334 = self.module_334(self.output_module_333)
        self.output_module_335 = self.module_335(self.output_module_334)
        self.output_module_336 = self.module_336(self.output_module_335)
        self.output_module_337 = self.module_337(self.output_module_336)
        self.output_module_338 = self.module_338(alpha=1, other=self.output_module_337, input=self.output_module_333)
        self.output_module_339 = self.module_339(alpha=1, other=self.output_module_338, input=self.output_module_331)
        self.output_module_340 = self.module_340(self.output_module_339)
        self.output_module_341 = self.module_341(self.output_module_340)
        self.output_module_342 = self.module_342(self.output_module_341)
        self.output_module_343 = self.module_343(self.output_module_342)
        self.output_module_344 = self.module_344(self.output_module_343)
        self.output_module_345 = self.module_345(self.output_module_344)
        self.output_module_346 = self.module_346(alpha=1, other=self.output_module_345, input=self.output_module_341)
        self.output_module_347 = self.module_347(alpha=1, other=self.output_module_346, input=self.output_module_339)
        self.output_module_348 = self.module_348(self.output_module_347)
        self.output_module_349 = self.module_349(self.output_module_348)
        self.output_module_350 = self.module_350(self.output_module_349)
        self.output_module_351 = self.module_351(self.output_module_350)
        self.output_module_352 = self.module_352(self.output_module_351)
        self.output_module_353 = self.module_353(self.output_module_352)
        self.output_module_354 = self.module_354(alpha=1, other=self.output_module_353, input=self.output_module_349)
        self.output_module_355 = self.module_355(alpha=1, other=self.output_module_354, input=self.output_module_347)
        self.output_module_356 = self.module_356(self.output_module_355)
        self.output_module_357 = self.module_357(self.output_module_356)
        self.output_module_358 = self.module_358(self.output_module_357)
        self.output_module_359 = self.module_359(self.output_module_358)
        self.output_module_360 = self.module_360(self.output_module_359)
        self.output_module_361 = self.module_361(self.output_module_360)
        self.output_module_362 = self.module_362(alpha=1, other=self.output_module_361, input=self.output_module_357)
        self.output_module_363 = self.module_363(alpha=1, other=self.output_module_362, input=self.output_module_355)
        self.output_module_364 = self.module_364(self.output_module_363)
        self.output_module_365 = self.module_365(self.output_module_364)
        self.output_module_366 = self.module_366(self.output_module_365)
        self.output_module_367 = self.module_367(self.output_module_366)
        self.output_module_368 = self.module_368(self.output_module_367)
        self.output_module_369 = self.module_369(self.output_module_368)
        self.output_module_370 = self.module_370(alpha=1, other=self.output_module_369, input=self.output_module_365)
        self.output_module_371 = self.module_371(alpha=1, other=self.output_module_370, input=self.output_module_363)
        self.output_module_372 = self.module_372(self.output_module_371)
        self.output_module_373 = self.module_373(self.output_module_372)
        self.output_module_374 = self.module_374(self.output_module_373)
        self.output_module_375 = self.module_375(self.output_module_374)
        self.output_module_376 = self.module_376(self.output_module_375)
        self.output_module_377 = self.module_377(self.output_module_376)
        self.output_module_378 = self.module_378(alpha=1, other=self.output_module_377, input=self.output_module_373)
        self.output_module_379 = self.module_379(alpha=1, other=self.output_module_378, input=self.output_module_371)
        self.output_module_380 = self.module_380(self.output_module_379)
        self.output_module_381 = self.module_381(self.output_module_380)
        self.output_module_382 = self.module_382(self.output_module_381)
        self.output_module_383 = self.module_383(self.output_module_382)
        self.output_module_384 = self.module_384(self.output_module_383)
        self.output_module_385 = self.module_385(self.output_module_384)
        self.output_module_386 = self.module_386(alpha=1, other=self.output_module_385, input=self.output_module_381)
        self.output_module_387 = self.module_387(alpha=1, other=self.output_module_386, input=self.output_module_379)
        self.output_module_388 = self.module_388(self.output_module_387)
        self.output_module_389 = self.module_389(self.output_module_388)
        self.output_module_390 = self.module_390(self.output_module_389)
        self.output_module_391 = self.module_391(self.output_module_390)
        self.output_module_392 = self.module_392(self.output_module_391)
        self.output_module_393 = self.module_393(self.output_module_392)
        self.output_module_394 = self.module_394(alpha=1, other=self.output_module_393, input=self.output_module_389)
        self.output_module_395 = self.module_395(alpha=1, other=self.output_module_394, input=self.output_module_387)
        self.output_module_396 = self.module_396(self.output_module_395)
        self.output_module_397 = self.module_397(self.output_module_396)
        self.output_module_398 = self.module_398(self.output_module_397)
        self.output_module_399 = self.module_399(self.output_module_398)
        self.output_module_400 = self.module_400(self.output_module_399)
        self.output_module_401 = self.module_401(self.output_module_400)
        self.output_module_402 = self.module_402(alpha=1, other=self.output_module_401, input=self.output_module_397)
        self.output_module_403 = self.module_403(alpha=1, other=self.output_module_402, input=self.output_module_395)
        self.output_module_404 = self.module_404(self.output_module_403)
        self.output_module_405 = self.module_405(self.output_module_404)
        self.output_module_406 = self.module_406(self.output_module_405)
        self.output_module_407 = self.module_407(self.output_module_406)
        self.output_module_408 = self.module_408(self.output_module_407)
        self.output_module_409 = self.module_409(self.output_module_408)
        self.output_module_410 = self.module_410(alpha=1, other=self.output_module_409, input=self.output_module_405)
        self.output_module_411 = self.module_411(alpha=1, other=self.output_module_410, input=self.output_module_403)
        self.output_module_412 = self.module_412(self.output_module_411)
        self.output_module_413 = self.module_413(alpha=1, other=self.output_module_412, input=self.output_module_331)
        self.output_module_414 = self.module_414(self.output_module_413)
        self.output_module_415 = self.module_415(alpha=1, other=self.output_module_414, input=self.output_module_3)
        self.output_module_416 = self.module_416(input=self.output_module_415, dim=2)
        self.output_module_417 = self.module_417(dtype=torch.int, device='cpu', data=self.output_module_416)
        self.output_module_418 = self.module_418(input=self.output_module_417, dtype=torch.float)
        self.output_module_419 = self.module_419(other=self.output_module_1, input=self.output_module_418)
        self.output_module_420 = self.module_420(input=self.output_module_419, dtype=torch.float)
        self.output_module_421 = self.module_421(input=self.output_module_420)
        self.output_module_422 = self.module_422(input=self.output_module_421)
        self.output_module_423 = self.module_423(input=self.output_module_415, dim=3)
        self.output_module_424 = self.module_424(dtype=torch.int, device='cpu', data=self.output_module_423)
        self.output_module_425 = self.module_425(input=self.output_module_424, dtype=torch.float)
        self.output_module_426 = self.module_426(other=self.output_module_2, input=self.output_module_425)
        self.output_module_427 = self.module_427(input=self.output_module_426, dtype=torch.float)
        self.output_module_428 = self.module_428(input=self.output_module_427)
        self.output_module_429 = self.module_429(input=self.output_module_428)
        self.output_module_430 = self.module_430(input=self.output_module_415, size=[self.output_module_422,self.output_module_429], scale_factor=None, mode='nearest')
        self.output_module_431 = self.module_431(self.output_module_415)
        self.output_module_432 = self.module_432(self.output_module_431)
        self.output_module_433 = self.module_433(alpha=1, other=self.output_module_430, input=self.output_module_432)
        self.output_module_434 = self.module_434(self.output_module_433)
        return self.output_module_434
