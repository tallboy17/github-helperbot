Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
The command below requires around 14GB of GPU memory for Vicuna-7B and 28GB of GPU memory for Vicuna-13B.
See the ["Not Enough Memory" section](#not-enough-memory) below if you do not have enough memory.
`--model-path` can be a local folder or a Hugging Face repo name.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5
```