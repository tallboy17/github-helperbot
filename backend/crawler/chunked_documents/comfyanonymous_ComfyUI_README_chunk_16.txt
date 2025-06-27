Repository: comfyanonymous/ComfyUI
Language: Python
Stars: 80094
Forks: 8865
-----
AMD users can install rocm and pytorch with pip if you don't have it already installed, this is the command to install the stable version:  
```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.3```  
This is the command to install the nightly with ROCm 6.4 which might have some performance improvements:  
```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.4```