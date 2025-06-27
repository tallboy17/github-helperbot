Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
If you do not have enough memory, you can enable 8-bit compression by adding `--load-8bit` to commands above.
This can reduce memory usage by around half with slightly degraded model quality.
It is compatible with the CPU, GPU, and Metal backend.  
Vicuna-13B with 8-bit compression can run on a single GPU with 16 GB of VRAM, like an Nvidia RTX 3090, RTX 4080, T4, V100 (16GB), or an AMD RX 6800 XT.  
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --load-8bit
```  
In addition to that, you can add `--cpu-offloading` to commands above to offload weights that don't fit on your GPU onto the CPU memory.
This requires 8-bit compression to be enabled and the bitsandbytes package to be installed, which is only available on linux operating systems.