Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
If you want to compile with CUDA support, [select a supported version of CUDA from our support matrix](https://pytorch.org/get-started/locally/), then install the following:
- [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)
- [NVIDIA cuDNN](https://developer.nvidia.com/cudnn) v8.5 or above
- [Compiler](https://gist.github.com/ax3l/9489132) compatible with CUDA  
Note: You could refer to the [cuDNN Support Matrix](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/reference/support-matrix.html) for cuDNN versions with the various supported CUDA, CUDA driver and NVIDIA hardware  
If you want to disable CUDA support, export the environment variable `USE_CUDA=0`.
Other potentially useful environment variables may be found in `setup.py`.  If
CUDA is installed in a non-standard location, set PATH so that the nvcc you
want to use can be found (e.g., `export PATH=/usr/local/cuda-12.8/bin:$PATH`).  
If you are building for NVIDIA's Jetson platforms (Jetson Nano, TX1, TX2, AGX Xavier), Instructions to install PyTorch for Jetson Nano are [available here](https://devtalk.nvidia.com/default/topic/1049071/jetson-nano/pytorch-for-jetson-nano/)