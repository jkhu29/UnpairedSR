rm -rf RCAN_DPU_OutPut

echo "\e[1;33;41m !!!!!!!!!RCAN CONVERTING!!!!!!!!! \e[0m"

echo "\e[1;33;41m convert to xilinx graph \e[0m"

python xmodel.py

echo "\e[1;33;41m compile to a xmodel file which could be deployed \e[0m"
mkdir RCAN_DPU_OutPut

vai_c_xir -x quantize_result/RCAN_int.xmodel -a arch.json -o RCAN_DPU_OutPut/ -n RCAN

xir svg RCAN_DPU_OutPut/RCAN.xmodel RCAN.svg
echo "\e[1;33;41m you can see the graph in ./RCAN.svg \e[0m"

