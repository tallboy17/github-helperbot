Repository: meta-llama/llama
Language: Python
Stars: 58396
Forks: 9778
-----
The fine-tuned models were trained for dialogue applications. To get the expected features and performance for them, a specific formatting defined in [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212)
needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces).  
You can also deploy additional classifiers for filtering out inputs and outputs that are deemed unsafe. See the llama-cookbook repo for [an example](https://github.com/facebookresearch/llama-recipes/blob/main/examples/inference.py) of how to add a safety checker to the inputs and outputs of your inference code.  
Examples using llama-2-7b-chat:  
```
torchrun --nproc_per_node 1 example_chat_completion.py \
--ckpt_dir llama-2-7b-chat/ \
--tokenizer_path tokenizer.model \
--max_seq_len 512 --max_batch_size 6
```  
Llama 2 is a new technology that carries potential risks with use. Testing conducted to date has not — and could not — cover all scenarios.
In order to help developers address these risks, we have created the [Responsible Use Guide](Responsible-Use-Guide.pdf). More details can be found in our research paper as well.