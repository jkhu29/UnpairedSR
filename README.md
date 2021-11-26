# UnpairedSR
An unofficial implementation of "Unpaired Image Super-Resolution using Pseudo-Supervision." CVPR2020
turn RCAN(modified) --> xmodel(xilinx graph)

## Usage

```
python -W ignore train.py
```

if you want to deploy it on pynq-dpu(now support V2.6)

```
cd convert
sh quantize.sh
```

you can get `.xmodel` in RCAN_DPU_OutPut, that's what you want
