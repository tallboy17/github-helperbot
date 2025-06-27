Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
- You can register multiple model workers to a single controller, which can be used for serving a single model with higher throughput or serving multiple models at the same time. When doing so, please allocate different GPUs and ports for different model workers.
```
# worker 0
CUDA_VISIBLE_DEVICES=0 python3 -m fastchat.serve.model_worker --model-path lmsys/vicuna-7b-v1.5 --controller http://localhost:21001 --port 31000 --worker http://localhost:31000
# worker 1
CUDA_VISIBLE_DEVICES=1 python3 -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0 --controller http://localhost:21001 --port 31001 --worker http://localhost:31001
```
- You can also launch a multi-tab gradio server, which includes the Chatbot Arena tabs.
```bash
python3 -m fastchat.serve.gradio_web_server_multi
```
- The default model worker based on huggingface/transformers has great compatibility but can be slow. If you want high-throughput batched serving, you can try [vLLM integration](docs/vllm_integration.md).
- If you want to host it on your own UI or third party UI, see [Third Party UI](docs/third_party_ui.md).