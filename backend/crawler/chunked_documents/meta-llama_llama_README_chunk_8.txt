Repository: meta-llama/llama
Language: Python
Stars: 58396
Forks: 9778
-----
These models are not finetuned for chat or Q&A. They should be prompted so that the expected answer is the natural continuation of the prompt.  
See `example_text_completion.py` for some examples. To illustrate, see the command below to run it with the llama-2-7b model (`nproc_per_node` needs to be set to the `MP` value):  
```
torchrun --nproc_per_node 1 example_text_completion.py \
--ckpt_dir llama-2-7b/ \
--tokenizer_path tokenizer.model \
--max_seq_len 128 --max_batch_size 4
```