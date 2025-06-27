Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Install the [Ascend PyTorch Adapter](https://github.com/Ascend/pytorch). Set the CANN environment variables:
```
source /usr/local/Ascend/ascend-toolkit/set_env.sh
```  
Use `--device npu` to enable NPU acceleration.
```
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device npu
```
Vicuna-7B/13B can run on an Ascend NPU.