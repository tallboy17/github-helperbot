Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Besides Vicuna, we also released two additional models: [LongChat](https://lmsys.org/blog/2023-06-29-longchat/) and FastChat-T5.
You can use the commands below to chat with them. They will automatically download the weights from Hugging Face repos.  
| Model | Chat Command | Hugging Face Repo |
| ---  | --- | --- |
| LongChat-7B   | `python3 -m fastchat.serve.cli --model-path lmsys/longchat-7b-32k-v1.5`  | [lmsys/longchat-7b-32k](https://huggingface.co/lmsys/longchat-7b-32k-v1.5)   |
| FastChat-T5-3B   | `python3 -m fastchat.serve.cli --model-path lmsys/fastchat-t5-3b-v1.0`  | [lmsys/fastchat-t5-3b-v1.0](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0) |