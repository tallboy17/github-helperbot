Repository: meta-llama/llama
Language: Python
Stars: 58396
Forks: 9778
-----
Different models require different model-parallel (MP) values:  
|  Model | MP |
|--------|----|
| 7B     | 1  |
| 13B    | 2  |
| 70B    | 8  |  
All models support sequence length up to 4096 tokens, but we pre-allocate the cache according to `max_seq_len` and `max_batch_size` values. So set those according to your hardware.