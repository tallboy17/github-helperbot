Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
```bash
docker run -it --rm --gpus=all --ipc=host hiyouga/llamafactory:latest
```  
This image is built on Ubuntu 22.04 (x86\_64), CUDA 12.4, Python 3.11, PyTorch 2.6.0, and Flash-attn 2.7.4.  
Find the pre-built images: https://hub.docker.com/r/hiyouga/llamafactory/tags  
Please refer to [build docker](#build-docker) to build the image yourself.  
<details><summary>Setting up a virtual environment with <b>uv</b></summary>  
Create an isolated Python environment with [uv](https://github.com/astral-sh/uv):  
```bash
uv sync --extra torch --extra metrics --prerelease=allow
```  
Run LLaMA-Factory in the isolated environment:  
```bash
uv run --prerelease=allow llamafactory-cli train examples/train_lora/llama3_lora_pretrain.yaml
```  
</details>  
<details><summary>For Windows users</summary>