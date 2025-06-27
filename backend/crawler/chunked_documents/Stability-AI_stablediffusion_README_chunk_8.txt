Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
This script incorporates an [invisible watermarking](https://github.com/ShieldMnt/invisible-watermark) of the outputs, to help viewers [identify the images as machine-generated](scripts/tests/test_watermark.py).
We provide the configs for the _SD2-v_ (768px) and _SD2-base_ (512px) model.  
First, download the weights for [_SD2.1-v_](https://huggingface.co/stabilityai/stable-diffusion-2-1) and [_SD2.1-base_](https://huggingface.co/stabilityai/stable-diffusion-2-1-base).  
To sample from the _SD2.1-v_ model, run the following:  
```
python scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt <path/to/768model.ckpt/> --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768
```
or try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/stabilityai/stable-diffusion).  
To sample from the base model, use
```
python scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt <path/to/model.ckpt/> --config <path/to/config.yaml/>
```  
By default, this uses the [DDIM sampler](https://arxiv.org/abs/2010.02502), and renders images of size 768x768 (which it was trained on) in 50 steps.
Empirically, the v-models can be sampled with higher guidance scales.  
Note: The inference config for all model versions is designed to be used with EMA-only checkpoints.
For this reason `use_ema=False` is set in the configuration, otherwise the code will try to switch from
non-EMA to EMA weights.