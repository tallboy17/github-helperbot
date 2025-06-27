Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
If you want to compile with ROCm support, install
- [AMD ROCm](https://rocm.docs.amd.com/en/latest/deploy/linux/quick_start.html) 4.0 and above installation
- ROCm is currently supported only for Linux systems.  
By default the build system expects ROCm to be installed in `/opt/rocm`. If ROCm is installed in a different directory, the `ROCM_PATH` environment variable must be set to the ROCm installation directory. The build system automatically detects the AMD GPU architecture. Optionally, the AMD GPU architecture can be explicitly set with the `PYTORCH_ROCM_ARCH` environment variable [AMD GPU architecture](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-gpus)  
If you want to disable ROCm support, export the environment variable `USE_ROCM=0`.
Other potentially useful environment variables may be found in `setup.py`.