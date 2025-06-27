Repository: hpcaitech/ColossalAI
Language: Python
Stars: 40976
Forks: 4521
-----
You can easily install Colossal-AI with the following command. **By default, we do not build PyTorch extensions during installation.**  
```bash
pip install colossalai
```  
**Note: only Linux is supported for now.**  
However, if you want to build the PyTorch extensions during installation, you can set `BUILD_EXT=1`.  
```bash
BUILD_EXT=1 pip install colossalai
```  
**Otherwise, CUDA kernels will be built during runtime when you actually need them.**  
We also keep releasing the nightly version to PyPI every week. This allows you to access the unreleased features and bug fixes in the main branch.
Installation can be made via  
```bash
pip install colossalai-nightly
```