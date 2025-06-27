Repository: microsoft/markitdown
Language: Python
Stars: 59294
Forks: 3083
-----
MarkItDown requires Python 3.10 or higher. It is recommended to use a virtual environment to avoid dependency conflicts.  
With the standard Python installation, you can create and activate a virtual environment using the following commands:  
```bash
python -m venv .venv
source .venv/bin/activate
```  
If using `uv`, you can create a virtual environment with:  
```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
# NOTE: Be sure to use 'uv pip install' rather than just 'pip install' to install packages in this virtual environment
```  
If you are using Anaconda, you can create a virtual environment with:  
```bash
conda create -n markitdown python=3.12
conda activate markitdown
```