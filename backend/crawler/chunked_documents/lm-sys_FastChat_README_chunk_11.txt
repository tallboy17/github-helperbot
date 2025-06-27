Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
You can use model parallelism to aggregate GPU memory from multiple GPUs on the same machine.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --num-gpus 2
```  
Tips:
Sometimes the "auto" device mapping strategy in huggingface/transformers does not perfectly balance the memory allocation across multiple GPUs.
You can use `--max-gpu-memory` to specify the maximum memory per GPU for storing model weights.
This allows it to allocate more memory for activations, so you can use longer context lengths or larger batch sizes. For example,  
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --num-gpus 2 --max-gpu-memory 8GiB
```