Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
- Install dependency
```bash
pip3 install -e ".[train]"
```  
- You can use the following command to train Vicuna-7B with 4 x A100 (40GB). Update `--model_name_or_path` with the actual path to Llama weights and `--data_path` with the actual path to data.
```bash
torchrun --nproc_per_node=4 --master_port=20001 fastchat/train/train_mem.py \
--model_name_or_path meta-llama/Llama-2-7b-hf \
--data_path data/dummy_conversation.json \
--bf16 True \
--output_dir output_vicuna \
--num_train_epochs 3 \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 2 \
--gradient_accumulation_steps 16 \
--evaluation_strategy "no" \
--save_strategy "steps" \
--save_steps 1200 \
--save_total_limit 10 \
--learning_rate 2e-5 \
--weight_decay 0. \
--warmup_ratio 0.03 \
--lr_scheduler_type "cosine" \
--logging_steps 1 \
--fsdp "full_shard auto_wrap" \
--fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
--tf32 True \
--model_max_length 2048 \
--gradient_checkpointing True \
--lazy_preprocess True
```  
Tips:
- If you are using V100 which is not supported by FlashAttention, you can use the [memory-efficient attention](https://arxiv.org/abs/2112.05682) implemented in [xFormers](https://github.com/facebookresearch/xformers). Install xformers and replace `fastchat/train/train_mem.py` above with [fastchat/train/train_xformers.py](fastchat/train/train_xformers.py).
- If you meet out-of-memory due to "FSDP Warning: When using FSDP, it is efficient and recommended... ", see solutions [here](https://github.com/huggingface/transformers/issues/24724#issuecomment-1645189539).
- If you meet out-of-memory during model saving, see solutions [here](https://github.com/pytorch/pytorch/issues/98823).
- To turn on logging to popular experiment tracking tools such as Tensorboard, MLFlow or Weights & Biases, use the `report_to` argument, e.g. pass `--report_to wandb` to turn on logging to Weights & Biases.