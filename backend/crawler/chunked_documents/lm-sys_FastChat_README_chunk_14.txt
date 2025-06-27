Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Install the [Intel Extension for PyTorch](https://intel.github.io/intel-extension-for-pytorch/xpu/latest/tutorials/installation.html). Set the OneAPI environment variables:
```
source /opt/intel/oneapi/setvars.sh
```  
Use `--device xpu` to enable XPU/GPU acceleration.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device xpu
```
Vicuna-7B can run on an Intel Arc A770 16GB.