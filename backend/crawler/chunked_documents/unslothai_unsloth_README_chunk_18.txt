Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
We tested Llama 3.1 (8B) Instruct and did 4bit QLoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads.
| GPU VRAM | 🦥Unsloth context length | Hugging Face + FA2 |
|----------|-----------------------|-----------------|
| 8 GB     | 2,972                 | OOM             |
| 12 GB    | 21,848                | 932             |
| 16 GB    | 40,724                | 2,551           |
| 24 GB    | 78,475                | 5,789           |
| 40 GB    | 153,977               | 12,264          |
| 48 GB    | 191,728               | 15,502          |
| 80 GB    | 342,733               | 28,454          |