Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
RL including DPO, GRPO, PPO, Reward Modelling, Online DPO all work with Unsloth. We're in 🤗Hugging Face's official docs! We're on the [GRPO docs](https://huggingface.co/learn/nlp-course/en/chapter12/6) and the [DPO docs](https://huggingface.co/docs/trl/main/en/dpo_trainer#accelerate-dpo-fine-tuning-using-unsloth)! List of RL notebooks:  
- Advanced Qwen3 GRPO notebook: [Link](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb)
- ORPO notebook: [Link](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_(8B)-ORPO.ipynb)
- DPO Zephyr notebook: [Link](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Zephyr_(7B)-DPO.ipynb)
- KTO notebook: [Link](https://colab.research.google.com/drive/1MRgGtLWuZX4ypSfGguFgC-IblTvO2ivM?usp=sharing)
- SimPO notebook: [Link](https://colab.research.google.com/drive/1Hs5oQDovOay4mFA6Y9lQhVJ8TnbFLFh2?usp=sharing)  
<details>
<summary>Click for DPO code</summary>  
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0" # Optional set GPU device ID

from unsloth import FastLanguageModel
import torch
from trl import DPOTrainer, DPOConfig
max_seq_length = 2048

model, tokenizer = FastLanguageModel.from_pretrained(
model_name = "unsloth/zephyr-sft-bnb-4bit",
max_seq_length = max_seq_length,
load_in_4bit = True,
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
model,
r = 64,
target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",],
lora_alpha = 64,
lora_dropout = 0, # Supports any, but = 0 is optimized
bias = "none",    # Supports any, but = "none" is optimized
# [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
random_state = 3407,
max_seq_length = max_seq_length,
)

dpo_trainer = DPOTrainer(
model = model,
ref_model = None,
train_dataset = YOUR_DATASET_HERE,
# eval_dataset = YOUR_DATASET_HERE,
tokenizer = tokenizer,
args = DPOConfig(
per_device_train_batch_size = 4,
gradient_accumulation_steps = 8,
warmup_ratio = 0.1,
num_train_epochs = 3,
logging_steps = 1,
optim = "adamw_8bit",
seed = 42,
output_dir = "outputs",
max_length = 1024,
max_prompt_length = 512,
beta = 0.1,
),
)
dpo_trainer.train()
```
</details>