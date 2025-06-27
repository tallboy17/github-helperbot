Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
To run Unsloth directly on Windows:
- Install Triton from this Windows fork and follow the instructions [here](https://github.com/woct0rdho/triton-windows) (be aware that the Windows fork requires PyTorch >= 2.4 and CUDA 12)
- In the SFTTrainer, set `dataset_num_proc=1` to avoid a crashing issue:
```python
trainer = SFTTrainer(
dataset_num_proc=1,
...
)
```