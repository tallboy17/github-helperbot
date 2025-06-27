Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
If you're planning on running Text-to-Image on Intel® CPU, try to sample an image with TorchScript and Intel® Extension for PyTorch* optimizations. Intel® Extension for PyTorch* extends PyTorch by enabling up-to-date features optimizations for an extra performance boost on Intel® hardware. It can optimize memory layout of the operators to Channel Last memory format, which is generally beneficial for Intel CPUs, take advantage of the most advanced instruction set available on a machine, optimize operators and many more.  
**Prerequisites**  
Before running the script, make sure you have all needed libraries installed. (the optimization was checked on `Ubuntu 20.04`). Install [jemalloc](https://github.com/jemalloc/jemalloc), [numactl](https://linux.die.net/man/8/numactl), Intel® OpenMP and Intel® Extension for PyTorch*.  
```bash
apt-get install numactl libjemalloc-dev
pip install intel-openmp
pip install intel_extension_for_pytorch -f https://software.intel.com/ipex-whl-stable
```  
To sample from the _SD2.1-v_ model with TorchScript+IPEX optimizations, run the following. Remember to specify desired number of instances you want to run the program on ([more](https://github.com/intel/intel-extension-for-pytorch/blob/master/intel_extension_for_pytorch/cpu/launch.py#L48)).  
```
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt \"a corgi is playing guitar, oil on canvas\" --ckpt <path/to/768model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-v-fp32.yaml  --H 768 --W 768 --precision full --device cpu --torchscript --ipex
```  
To sample from the base model with IPEX optimizations, use  
```
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt \"a corgi is playing guitar, oil on canvas\" --ckpt <path/to/model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-fp32.yaml  --n_samples 1 --n_iter 4 --precision full --device cpu --torchscript --ipex
```  
If you're using a CPU that supports `bfloat16`, consider sample from the model with bfloat16 enabled for a performance boost, like so  
```bash
# SD2.1-v
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt \"a corgi is playing guitar, oil on canvas\" --ckpt <path/to/768model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-v-bf16.yaml --H 768 --W 768 --precision full --device cpu --torchscript --ipex --bf16
# SD2.1-base
MALLOC_CONF=oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000 python -m intel_extension_for_pytorch.cpu.launch --ninstance <number of an instance> --enable_jemalloc scripts/txt2img.py --prompt \"a corgi is playing guitar, oil on canvas\" --ckpt <path/to/model.ckpt/> --config configs/stable-diffusion/intel/v2-inference-bf16.yaml --precision full --device cpu --torchscript --ipex --bf16
```