Repository: comfyanonymous/ComfyUI
Language: Python
Stars: 80094
Forks: 8865
-----
(Option 1) Intel Arc GPU users can install native PyTorch with torch.xpu support using pip (currently available in PyTorch nightly builds). More information can be found [here](https://pytorch.org/docs/main/notes/get_start_xpu.html)  
1. To install PyTorch nightly, use the following command:  
```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/xpu```  
2. Launch ComfyUI by running `python main.py`  
(Option 2) Alternatively, Intel GPUs supported by Intel Extension for PyTorch (IPEX) can leverage IPEX for improved performance.  
1. For Intel® Arc™ A-Series Graphics utilizing IPEX, create a conda environment and use the commands below:  
```
conda install libuv
pip install torch==2.3.1.post0+cxx11.abi torchvision==0.18.1.post0+cxx11.abi torchaudio==2.3.1.post0+cxx11.abi intel-extension-for-pytorch==2.3.110.post0+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/ --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/cn/
```  
For other supported Intel GPUs with IPEX, visit [Installation](https://intel.github.io/intel-extension-for-pytorch/index.html#installation?platform=gpu) for more information.  
Additional discussion and help can be found [here](https://github.com/comfyanonymous/ComfyUI/discussions/476).