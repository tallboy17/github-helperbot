Repository: deepseek-ai/DeepSeek-V3
Language: Python
Stars: 97701
Forks: 15891
-----
[SGLang](https://github.com/sgl-project/sglang) currently supports [MLA optimizations](https://lmsys.org/blog/2024-09-04-sglang-v0-3/#deepseek-multi-head-latent-attention-mla-throughput-optimizations), [DP Attention](https://lmsys.org/blog/2024-12-04-sglang-v0-4/#data-parallelism-attention-for-deepseek-models), FP8 (W8A8), FP8 KV Cache, and Torch Compile, delivering state-of-the-art latency and throughput performance among open-source frameworks.  
Notably, [SGLang v0.4.1](https://github.com/sgl-project/sglang/releases/tag/v0.4.1) fully supports running DeepSeek-V3 on both **NVIDIA and AMD GPUs**, making it a highly versatile and robust solution.  
SGLang also supports [multi-node tensor parallelism](https://github.com/sgl-project/sglang/tree/main/benchmark/deepseek_v3#example-serving-with-2-h208), enabling you to run this model on multiple network-connected machines.  
Multi-Token Prediction (MTP) is in development, and progress can be tracked in the [optimization plan](https://github.com/sgl-project/sglang/issues/2591).  
Here are the launch instructions from the SGLang team: https://github.com/sgl-project/sglang/tree/main/benchmark/deepseek_v3