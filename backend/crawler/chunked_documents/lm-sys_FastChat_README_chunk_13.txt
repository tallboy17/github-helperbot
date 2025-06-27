Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Use `--device mps` to enable GPU acceleration on Mac computers (requires torch >= 2.0).
Use `--load-8bit` to turn on 8-bit compression.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device mps --load-8bit
```
Vicuna-7B can run on a 32GB M1 Macbook with 1 - 2 words / second.