Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
We tested Llama 3.3 (70B) Instruct on a 80GB A100 and did 4bit QLoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads.  
| GPU VRAM | 🦥Unsloth context length | Hugging Face + FA2 |
|----------|------------------------|------------------|
| 48 GB    | 12,106                | OOM              |
| 80 GB    | 89,389                | 6,916            |  
<br>  
![](https://i.ibb.co/sJ7RhGG/image-41.png)
<br>