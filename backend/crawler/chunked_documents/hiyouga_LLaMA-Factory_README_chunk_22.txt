Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
To use QLoRA based on bitsandbytes on Ascend NPU, please follow these 3 steps:  
1. Manually compile bitsandbytes: Refer to [the installation documentation](https://huggingface.co/docs/bitsandbytes/installation?backend=Ascend+NPU&platform=Ascend+NPU) for the NPU version of bitsandbytes to complete the compilation and installation. The compilation requires a cmake version of at least 3.22.1 and a g++ version of at least 12.x.  
```bash
# Install bitsandbytes from source
# Clone bitsandbytes repo, Ascend NPU backend is currently enabled on multi-backend-refactor branch
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes/

# Install dependencies
pip install -r requirements-dev.txt

# Install the dependencies for the compilation tools. Note that the commands for this step may vary depending on the operating system. The following are provided for reference
apt-get install -y build-essential cmake

# Compile & install
cmake -DCOMPUTE_BACKEND=npu -S .
make
pip install .
```  
2. Install transformers from the main branch.  
```bash
git clone -b main https://github.com/huggingface/transformers.git
cd transformers
pip install .
```  
3. Set `double_quantization: false` in the configuration. You can refer to the [example](examples/train_qlora/llama3_lora_sft_bnb_npu.yaml).  
</details>