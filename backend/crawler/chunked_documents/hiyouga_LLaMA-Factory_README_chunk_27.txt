Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
```bash
API_PORT=8000 llamafactory-cli api examples/inference/llama3.yaml infer_backend=vllm vllm_enforce_eager=true
```  
> [!TIP]
> Visit [this page](https://platform.openai.com/docs/api-reference/chat/create) for API document.
>
> Examples: [Image understanding](scripts/api_example/test_image.py) | [Function calling](scripts/api_example/test_toolcall.py)