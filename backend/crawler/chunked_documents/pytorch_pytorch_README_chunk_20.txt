Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
**NOTE:** Must be built with a docker version > 18.06  
The `Dockerfile` is supplied to build images with CUDA 11.1 support and cuDNN v8.
You can pass `PYTHON_VERSION=x.y` make variable to specify which Python version is to be used by Miniconda, or leave it
unset to use the default.  
```bash
make -f docker.Makefile
# images are tagged as docker.io/${your_docker_username}/pytorch
```  
You can also pass the `CMAKE_VARS="..."` environment variable to specify additional CMake variables to be passed to CMake during the build.
See [setup.py](./setup.py) for the list of available variables.  
```bash
make -f docker.Makefile
```