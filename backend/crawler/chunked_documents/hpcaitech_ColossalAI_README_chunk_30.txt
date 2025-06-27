Repository: hpcaitech/ColossalAI
Language: Python
Stars: 40976
Forks: 4521
-----
> The version of Colossal-AI will be in line with the main branch of the repository. Feel free to raise an issue if you encounter any problems. :)  
```shell
git clone https://github.com/hpcaitech/ColossalAI.git
cd ColossalAI

# install colossalai
pip install .
```  
By default, we do not compile CUDA/C++ kernels. ColossalAI will build them during runtime.
If you want to install and enable CUDA kernel fusion (compulsory installation when using fused optimizer):  
```shell
BUILD_EXT=1 pip install .
```  
For Users with CUDA 10.2, you can still build ColossalAI from source. However, you need to manually download the cub library and copy it to the corresponding directory.  
```bash
# clone the repository
git clone https://github.com/hpcaitech/ColossalAI.git
cd ColossalAI

# download the cub library
wget https://github.com/NVIDIA/cub/archive/refs/tags/1.8.0.zip
unzip 1.8.0.zip
cp -r cub-1.8.0/cub/ colossalai/kernel/cuda_native/csrc/kernels/include/

# install
BUILD_EXT=1 pip install .
```  
<p align="right">(<a href="#top">back to top</a>)</p>