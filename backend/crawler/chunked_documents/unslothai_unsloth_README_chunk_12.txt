Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
For **advanced installation instructions** or if you see weird errors during installations:  
1. Install `torch` and `triton`. Go to https://pytorch.org to install it. For example `pip install torch torchvision torchaudio triton`
2. Confirm if CUDA is installed correctly. Try `nvcc`. If that fails, you need to install `cudatoolkit` or CUDA drivers.
3. Install `xformers` manually. You can try installing `vllm` and seeing if `vllm` succeeds. Check if `xformers` succeeded with `python -m xformers.info` Go to https://github.com/facebookresearch/xformers. Another option is to install `flash-attn` for Ampere GPUs.
4. Double check that your versions of Python, CUDA, CUDNN, `torch`, `triton`, and `xformers` are compatible with one another. The [PyTorch Compatibility Matrix](https://github.com/pytorch/pytorch/blob/main/RELEASE.md#release-compatibility-matrix) may be useful.
5. Finally, install `bitsandbytes` and check it with `python -m bitsandbytes`