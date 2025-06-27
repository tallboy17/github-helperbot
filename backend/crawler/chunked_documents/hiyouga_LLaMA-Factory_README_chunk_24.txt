Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
Use the following 3 commands to run LoRA **fine-tuning**, **inference** and **merging** of the Llama3-8B-Instruct model, respectively.  
```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
llamafactory-cli chat examples/inference/llama3_lora_sft.yaml
llamafactory-cli export examples/merge_lora/llama3_lora_sft.yaml
```  
See [examples/README.md](examples/README.md) for advanced usage (including distributed training).  
> [!TIP]
> Use `llamafactory-cli help` to show help information.
>
> Read [FAQs](https://github.com/hiyouga/LLaMA-Factory/issues/4614) first if you encounter any problems.