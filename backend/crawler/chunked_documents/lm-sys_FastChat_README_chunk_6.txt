Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
[Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/) is based on Llama 2 and should be used under Llama's [model license](https://github.com/facebookresearch/llama/blob/main/LICENSE).  
You can use the commands below to start chatting. It will automatically download the weights from Hugging Face repos.
Downloaded weights are stored in a `.cache` folder in the user's home folder (e.g., `~/.cache/huggingface/hub/<model_name>`).  
See more command options and how to handle out-of-memory in the "Inference with Command Line Interface" section below.  
**NOTE: `transformers>=4.31` is required for 16K versions.**  
| Size | Chat Command | Hugging Face Repo |
| ---  | --- | --- |
| 7B   | `python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5`  | [lmsys/vicuna-7b-v1.5](https://huggingface.co/lmsys/vicuna-7b-v1.5)   |
| 7B-16k   | `python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5-16k`  | [lmsys/vicuna-7b-v1.5-16k](https://huggingface.co/lmsys/vicuna-7b-v1.5-16k)   |
| 13B  | `python3 -m fastchat.serve.cli --model-path lmsys/vicuna-13b-v1.5` | [lmsys/vicuna-13b-v1.5](https://huggingface.co/lmsys/vicuna-13b-v1.5) |
| 13B-16k  | `python3 -m fastchat.serve.cli --model-path lmsys/vicuna-13b-v1.5-16k` | [lmsys/vicuna-13b-v1.5-16k](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k) |
| 33B  | `python3 -m fastchat.serve.cli --model-path lmsys/vicuna-33b-v1.3` | [lmsys/vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3) |  
**Old weights**: see [docs/vicuna_weights_version.md](docs/vicuna_weights_version.md) for all versions of weights and their differences.