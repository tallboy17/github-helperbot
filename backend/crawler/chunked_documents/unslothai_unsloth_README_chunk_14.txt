Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
`⚠️Do **NOT** use this if you have Conda.` Pip is a bit more complex since there are dependency issues. The pip command is different for `torch 2.2,2.3,2.4,2.5` and CUDA versions.  
For other torch versions, we support `torch211`, `torch212`, `torch220`, `torch230`, `torch240` and for CUDA versions, we support `cu118` and `cu121` and `cu124`. For Ampere devices (A100, H100, RTX3090) and above, use `cu118-ampere` or `cu121-ampere` or `cu124-ampere`.  
For example, if you have `torch 2.4` and `CUDA 12.1`, use:
```bash
pip install --upgrade pip
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"
```  
Another example, if you have `torch 2.5` and `CUDA 12.4`, use:
```bash
pip install --upgrade pip
pip install "unsloth[cu124-torch250] @ git+https://github.com/unslothai/unsloth.git"
```  
And other examples:
```bash
pip install "unsloth[cu121-ampere-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu118-ampere-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu118-torch240] @ git+https://github.com/unslothai/unsloth.git"

pip install "unsloth[cu121-torch230] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu121-ampere-torch230] @ git+https://github.com/unslothai/unsloth.git"

pip install "unsloth[cu121-torch250] @ git+https://github.com/unslothai/unsloth.git"
pip install "unsloth[cu124-ampere-torch250] @ git+https://github.com/unslothai/unsloth.git"
```  
Or, run the below in a terminal to get the **optimal** pip installation command:
```bash
wget -qO- https://raw.githubusercontent.com/unslothai/unsloth/main/unsloth/_auto_install.py | python -
```  
Or, run the below manually in a Python REPL:
```python
try: import torch
except: raise ImportError('Install torch via `pip install torch`')
from packaging.version import Version as V
v = V(torch.__version__)
cuda = str(torch.version.cuda)
is_ampere = torch.cuda.get_device_capability()[0] >= 8
if cuda != "12.1" and cuda != "11.8" and cuda != "12.4": raise RuntimeError(f"CUDA = {cuda} not supported!")
if   v <= V('2.1.0'): raise RuntimeError(f"Torch = {v} too old!")
elif v <= V('2.1.1'): x = 'cu{}{}-torch211'
elif v <= V('2.1.2'): x = 'cu{}{}-torch212'
elif v  < V('2.3.0'): x = 'cu{}{}-torch220'
elif v  < V('2.4.0'): x = 'cu{}{}-torch230'
elif v  < V('2.5.0'): x = 'cu{}{}-torch240'
elif v  < V('2.6.0'): x = 'cu{}{}-torch250'
else: raise RuntimeError(f"Torch = {v} too new!")
x = x.format(cuda.replace(".", ""), "-ampere" if is_ampere else "")
print(f'pip install --upgrade pip && pip install "unsloth[{x}] @ git+https://github.com/unslothai/unsloth.git"')
```