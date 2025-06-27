Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
| System | GPU | Command |
|--------|---------|---------|
| Linux/WSL | NVIDIA | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124` |
| Linux/WSL | CPU only | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cpu` |
| Linux | AMD | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/rocm6.2.4` |
| MacOS + MPS | Any | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0` |
| Windows | NVIDIA | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124` |
| Windows | CPU only | `pip3 install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0` |  
The up-to-date commands can be found here: https://pytorch.org/get-started/locally/.  
If you need `nvcc` to compile some library manually, you will additionally need to install this:  
```
conda install -y -c "nvidia/label/cuda-12.4.1" cuda
```