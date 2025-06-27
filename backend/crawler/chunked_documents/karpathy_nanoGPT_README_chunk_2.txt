Repository: karpathy/nanoGPT
Language: Python
Stars: 41980
Forks: 7009
-----
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```  
Dependencies:  
- [pytorch](https://pytorch.org) <3
- [numpy](https://numpy.org/install/) <3
-  `transformers` for huggingface transformers <3 (to load GPT-2 checkpoints)
-  `datasets` for huggingface datasets <3 (if you want to download + preprocess OpenWebText)
-  `tiktoken` for OpenAI's fast BPE code <3
-  `wandb` for optional logging <3
-  `tqdm` for progress bars <3