Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
This runs on the CPU only and does not require GPU. It requires around 30GB of CPU memory for Vicuna-7B and around 60GB of CPU memory for Vicuna-13B.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device cpu
```  
Use Intel AI Accelerator AVX512_BF16/AMX to accelerate CPU inference.
```
CPU_ISA=amx python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device cpu
```