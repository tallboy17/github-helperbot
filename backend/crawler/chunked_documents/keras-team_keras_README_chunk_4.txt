Repository: keras-team/keras
Language: Python
Stars: 63136
Forks: 19580
-----
The `requirements.txt` file will install a CPU-only version of TensorFlow, JAX, and PyTorch. For GPU support, we also
provide a separate `requirements-{backend}-cuda.txt` for TensorFlow, JAX, and PyTorch. These install all CUDA
dependencies via `pip` and expect a NVIDIA driver to be pre-installed. We recommend a clean python environment for each
backend to avoid CUDA version mismatches. As an example, here is how to create a Jax GPU environment with `conda`:  
```shell
conda create -y -n keras-jax python=3.10
conda activate keras-jax
pip install -r requirements-jax-cuda.txt
python pip_build.py --install
```