Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
- For AMD GPU users, please install ROCm and [the ROCm version of PyTorch](https://pytorch.org/get-started/locally/) before you install FastChat. See also this [post](https://github.com/lm-sys/FastChat/issues/104#issuecomment-1613791563).
- FastChat supports ExLlama V2. See [docs/exllama_v2.md](/docs/exllama_v2.md).
- FastChat supports GPTQ 4bit inference with [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa). See [docs/gptq.md](/docs/gptq.md).
- FastChat supports AWQ 4bit inference with [mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq). See [docs/awq.md](/docs/awq.md).
- [MLC LLM](https://mlc.ai/mlc-llm/), backed by [TVM Unity](https://github.com/apache/tvm/tree/unity) compiler, deploys Vicuna natively on phones, consumer-class GPUs and web browsers via Vulkan, Metal, CUDA and WebGPU.