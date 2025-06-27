Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
If you want to compile with Intel GPU support, follow these
- [PyTorch Prerequisites for Intel GPUs](https://www.intel.com/content/www/us/en/developer/articles/tool/pytorch-prerequisites-for-intel-gpus.html) instructions.
- Intel GPU is supported for Linux and Windows.  
If you want to disable Intel GPU support, export the environment variable `USE_XPU=0`.
Other potentially useful environment variables may be found in `setup.py`.