Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
```
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r <requirements file according to table below>
```  
Requirements file to use:  
| GPU | CPU | requirements file to use |
|--------|---------|---------|
| NVIDIA | has AVX2 | `requirements.txt` |
| NVIDIA | no AVX2 | `requirements_noavx2.txt` |
| AMD | has AVX2 | `requirements_amd.txt` |
| AMD | no AVX2 | `requirements_amd_noavx2.txt` |
| CPU only | has AVX2 | `requirements_cpu_only.txt` |
| CPU only | no AVX2 | `requirements_cpu_only_noavx2.txt` |
| Apple | Intel | `requirements_apple_intel.txt` |
| Apple | Apple Silicon | `requirements_apple_silicon.txt` |