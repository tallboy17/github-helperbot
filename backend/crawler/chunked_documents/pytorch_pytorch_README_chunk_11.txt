Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
If you are installing from source, you will need:
- Python 3.9 or later
- A compiler that fully supports C++17, such as clang or gcc (gcc 9.4.0 or newer is required, on Linux)
- Visual Studio or Visual Studio Build Tool (Windows only)  
\* PyTorch CI uses Visual C++ BuildTools, which come with Visual Studio Enterprise,
Professional, or Community Editions. You can also install the build tools from
https://visualstudio.microsoft.com/visual-cpp-build-tools/. The build tools *do not*
come with Visual Studio Code by default.  
An example of environment setup is shown below:  
* Linux:  
```bash
$ source <CONDA_INSTALL_DIR>/bin/activate
$ conda create -y -n <CONDA_NAME>
$ conda activate <CONDA_NAME>
```  
* Windows:  
```bash
$ source <CONDA_INSTALL_DIR>\Scripts\activate.bat
$ conda create -y -n <CONDA_NAME>
$ conda activate <CONDA_NAME>
$ call "C:\Program Files\Microsoft Visual Studio\<VERSION>\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```  
A conda environment is not required.  You can also do a PyTorch build in a
standard virtual environment, e.g., created with tools like `uv`, provided
your system has installed all the necessary dependencies unavailable as pip
packages (e.g., CUDA, MKL.)