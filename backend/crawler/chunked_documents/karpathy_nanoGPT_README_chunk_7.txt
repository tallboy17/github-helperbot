Repository: karpathy/nanoGPT
Language: Python
Stars: 41980
Forks: 7009
-----
Use the script `sample.py` to sample either from pre-trained GPT-2 models released by OpenAI, or from a model you trained yourself. For example, here is a way to sample from the largest available `gpt2-xl` model:  
```sh
python sample.py \
--init_from=gpt2-xl \
--start="What is the answer to life, the universe, and everything?" \
--num_samples=5 --max_new_tokens=100
```  
If you'd like to sample from a model you trained, use the `--out_dir` to point the code appropriately. You can also prompt the model with some text from a file, e.g. ```python sample.py --start=FILE:prompt.txt```.