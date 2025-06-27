Repository: huggingface/transformers
Language: Python
Stars: 145843
Forks: 29409
-----
Transformers works with Python 3.9+ [PyTorch](https://pytorch.org/get-started/locally/) 2.1+, [TensorFlow](https://www.tensorflow.org/install/pip) 2.6+, and [Flax](https://flax.readthedocs.io/en/latest/) 0.4.1+.  
Create and activate a virtual environment with [venv](https://docs.python.org/3/library/venv.html) or [uv](https://docs.astral.sh/uv/), a fast Rust-based Python package and project manager.  
```py
# venv
python -m venv .my-env
source .my-env/bin/activate
# uv
uv venv .my-env
source .my-env/bin/activate
```  
Install Transformers in your virtual environment.  
```py
# pip
pip install "transformers[torch]"

# uv
uv pip install "transformers[torch]"
```  
Install Transformers from source if you want the latest changes in the library or are interested in contributing. However, the *latest* version may not be stable. Feel free to open an [issue](https://github.com/huggingface/transformers/issues) if you encounter an error.  
```shell
git clone https://github.com/huggingface/transformers.git
cd transformers

# pip
pip install .[torch]

# uv
uv pip install .[torch]
```