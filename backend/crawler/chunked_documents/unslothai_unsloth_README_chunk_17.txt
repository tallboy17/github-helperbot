Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
- For our most detailed benchmarks, read our [Llama 3.3 Blog](https://unsloth.ai/blog/llama3-3).
- Benchmarking of Unsloth was also conducted by [🤗Hugging Face](https://huggingface.co/blog/unsloth-trl).  
We tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down):  
| Model          | VRAM  | 🦥 Unsloth speed | 🦥 VRAM reduction | 🦥 Longer context | 😊 Hugging Face + FA2 |
|----------------|-------|-----------------|----------------|----------------|--------------------|
| Llama 3.3 (70B)| 80GB  | 2x              | >75%           | 13x longer     | 1x                 |
| Llama 3.1 (8B) | 80GB  | 2x              | >70%           | 12x longer     | 1x                 |