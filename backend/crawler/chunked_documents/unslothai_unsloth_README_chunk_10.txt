Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
> [!warning]
> Python 3.13 does not support Unsloth. Use 3.12, 3.11 or 3.10  
1. **Install NVIDIA Video Driver:**
You should install the latest version of your GPUs driver. Download drivers here: [NVIDIA GPU Drive](https://www.nvidia.com/Download/index.aspx).  
3. **Install Visual Studio C++:**
You will need Visual Studio, with C++ installed. By default, C++ is not installed with [Visual Studio](https://visualstudio.microsoft.com/vs/community/), so make sure you select all of the C++ options. Also select options for Windows 10/11 SDK. For detailed instructions with options, see [here](https://docs.unsloth.ai/get-started/installing-+-updating).  
5. **Install CUDA Toolkit:**
Follow the instructions to install [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive).  
6. **Install PyTorch:**
You will need the correct version of PyTorch that is compatible with your CUDA drivers, so make sure to select them carefully.
[Install PyTorch](https://pytorch.org/get-started/locally/).  
7. **Install Unsloth:**  
```python
pip install unsloth
```