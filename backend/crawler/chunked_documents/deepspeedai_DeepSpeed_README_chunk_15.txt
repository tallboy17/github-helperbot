Repository: deepspeedai/DeepSpeed
Language: Python
Stars: 39026
Forks: 4426
-----
* [PyTorch](https://pytorch.org/) must be installed _before_ installing DeepSpeed.
* For full feature support we recommend a version of PyTorch that is >= 1.9 and ideally the latest PyTorch stable release.
* A CUDA or ROCm compiler such as [nvcc](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/#introduction) or [hipcc](https://github.com/ROCm-Developer-Tools/HIPCC) used to compile C++/CUDA/HIP extensions.
* Specific GPUs we develop and test against are listed below, this doesn't mean your GPU will not work if it doesn't fall into this category it's just DeepSpeed is most well tested on the following:
* NVIDIA: Pascal, Volta, Ampere, and Hopper architectures
* AMD: MI100 and MI200