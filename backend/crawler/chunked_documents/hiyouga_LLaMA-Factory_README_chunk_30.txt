Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
To use [Weights & Biases](https://wandb.ai) for logging experimental results, you need to add the following arguments to yaml files.  
```yaml
report_to: wandb
run_name: test_run # optional
```  
Set `WANDB_API_KEY` to [your key](https://wandb.ai/authorize) when launching training tasks to log in with your W&B account.