Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
[25/04/28] We supported fine-tuning the **[Qwen3](https://qwenlm.github.io/blog/qwen3/)** model family.  
[25/04/21] We supported the **[Muon](https://github.com/KellerJordan/Muon)** optimizer. See [examples](examples/README.md) for usage. Thank [@tianshijing](https://github.com/tianshijing)'s PR.  
[25/04/16] We supported fine-tuning the **[InternVL3](https://huggingface.co/OpenGVLab/InternVL3-8B)** model. See [PR #7258](https://github.com/hiyouga/LLaMA-Factory/pull/7258) to get started.  
[25/04/14] We supported fine-tuning the **[GLM-Z1](https://huggingface.co/THUDM/GLM-Z1-9B-0414)** and **[Kimi-VL](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct)** models.  
[25/04/06] We supported fine-tuning the **[Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)** model. See [PR #7611](https://github.com/hiyouga/LLaMA-Factory/pull/7611) to get started.  
<details><summary>Full Changelog</summary>  
[25/03/31] We supported fine-tuning the **[Qwen2.5 Omni](https://qwenlm.github.io/blog/qwen2.5-omni/)** model. See [PR #7537](https://github.com/hiyouga/LLaMA-Factory/pull/7537) to get started.  
[25/03/15] We supported **[SGLang](https://github.com/sgl-project/sglang)** as inference backend. Try `infer_backend: sglang` to accelerate inference.  
[25/03/12] We supported fine-tuning the **[Gemma 3](https://huggingface.co/blog/gemma3)** model.  
[25/02/24] Announcing **[EasyR1](https://github.com/hiyouga/EasyR1)**, an efficient, scalable and multi-modality RL training framework for efficient GRPO training.  
[25/02/11] We supported saving the **[Ollama](https://github.com/ollama/ollama)** modelfile when exporting the model checkpoints. See [examples](examples/README.md) for usage.  
[25/02/05] We supported fine-tuning the **[Qwen2-Audio](Qwen/Qwen2-Audio-7B-Instruct)** and **[MiniCPM-o-2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6)** on audio understanding tasks.  
[25/01/31] We supported fine-tuning the **[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)** and **[Qwen2.5-VL](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)** models.  
[25/01/15] We supported **[APOLLO](https://arxiv.org/abs/2412.05270)** optimizer. See [examples](examples/README.md) for usage.  
[25/01/14] We supported fine-tuning the **[MiniCPM-o-2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6)** and **[MiniCPM-V-2.6](https://huggingface.co/openbmb/MiniCPM-V-2_6)** models. Thank [@BUAADreamer](https://github.com/BUAADreamer)'s PR.  
[25/01/14] We supported fine-tuning the **[InternLM 3](https://huggingface.co/collections/internlm/)** models. Thank [@hhaAndroid](https://github.com/hhaAndroid)'s PR.  
[25/01/10] We supported fine-tuning the **[Phi-4](https://huggingface.co/microsoft/phi-4)** model.  
[24/12/21] We supported using **[SwanLab](https://github.com/SwanHubX/SwanLab)** for experiment tracking and visualization. See [this section](#use-swanlab-logger) for details.  
[24/11/27] We supported fine-tuning the **[Skywork-o1](https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B)** model and the **[OpenO1](https://huggingface.co/datasets/O1-OPEN/OpenO1-SFT)** dataset.  
[24/10/09] We supported downloading pre-trained models and datasets from the **[Modelers Hub](https://modelers.cn/models)**. See [this tutorial](#download-from-modelers-hub) for usage.  
[24/09/19] We supported fine-tuning the **[Qwen2.5](https://qwenlm.github.io/blog/qwen2.5/)** models.  
[24/08/30] We supported fine-tuning the **[Qwen2-VL](https://qwenlm.github.io/blog/qwen2-vl/)** models. Thank [@simonJJJ](https://github.com/simonJJJ)'s PR.  
[24/08/27] We supported **[Liger Kernel](https://github.com/linkedin/Liger-Kernel)**. Try `enable_liger_kernel: true` for efficient training.  
[24/08/09] We supported **[Adam-mini](https://github.com/zyushun/Adam-mini)** optimizer. See [examples](examples/README.md) for usage. Thank [@relic-yuexi](https://github.com/relic-yuexi)'s PR.  
[24/07/04] We supported [contamination-free packed training](https://github.com/MeetKai/functionary/tree/main/functionary/train/packing). Use `neat_packing: true` to activate it. Thank [@chuan298](https://github.com/chuan298)'s PR.  
[24/06/16] We supported **[PiSSA](https://arxiv.org/abs/2404.02948)** algorithm. See [examples](examples/README.md) for usage.  
[24/06/07] We supported fine-tuning the **[Qwen2](https://qwenlm.github.io/blog/qwen2/)** and **[GLM-4](https://github.com/THUDM/GLM-4)** models.  
[24/05/26] We supported **[SimPO](https://arxiv.org/abs/2405.14734)** algorithm for preference learning. See [examples](examples/README.md) for usage.  
[24/05/20] We supported fine-tuning the **PaliGemma** series models. Note that the PaliGemma models are pre-trained models, you need to fine-tune them with `paligemma` template for chat completion.  
[24/05/18] We supported **[KTO](https://arxiv.org/abs/2402.01306)** algorithm for preference learning. See [examples](examples/README.md) for usage.  
[24/05/14] We supported training and inference on the Ascend NPU devices. Check [installation](#installation) section for details.  
[24/04/26] We supported fine-tuning the **LLaVA-1.5** multimodal LLMs. See [examples](examples/README.md) for usage.  
[24/04/22] We provided a **[Colab notebook](https://colab.research.google.com/drive/1eRTPn37ltBbYsISy9Aw2NuI2Aq5CQrD9?usp=sharing)** for fine-tuning the Llama-3 model on a free T4 GPU. Two Llama-3-derived models fine-tuned using LLaMA Factory are available at Hugging Face, check [Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat) and [Llama3-Chinese](https://huggingface.co/zhichen/Llama3-Chinese) for details.  
[24/04/21] We supported **[Mixture-of-Depths](https://arxiv.org/abs/2404.02258)** according to [AstraMindAI's implementation](https://github.com/astramind-ai/Mixture-of-depths). See [examples](examples/README.md) for usage.  
[24/04/16] We supported **[BAdam](https://arxiv.org/abs/2404.02827)** optimizer. See [examples](examples/README.md) for usage.  
[24/04/16] We supported **[unsloth](https://github.com/unslothai/unsloth)**'s long-sequence training (Llama-2-7B-56k within 24GB). It achieves **117%** speed and **50%** memory compared with FlashAttention-2, more benchmarks can be found in [this page](https://github.com/hiyouga/LLaMA-Factory/wiki/Performance-comparison).  
[24/03/31] We supported **[ORPO](https://arxiv.org/abs/2403.07691)**. See [examples](examples/README.md) for usage.  
[24/03/21] Our paper "[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://arxiv.org/abs/2403.13372)" is available at arXiv!  
[24/03/20] We supported **FSDP+QLoRA** that fine-tunes a 70B model on 2x24GB GPUs. See [examples](examples/README.md) for usage.  
[24/03/13] We supported **[LoRA+](https://arxiv.org/abs/2402.12354)**. See [examples](examples/README.md) for usage.  
[24/03/07] We supported **[GaLore](https://arxiv.org/abs/2403.03507)** optimizer. See [examples](examples/README.md) for usage.  
[24/03/07] We integrated **[vLLM](https://github.com/vllm-project/vllm)** for faster and concurrent inference. Try `infer_backend: vllm` to enjoy **270%** inference speed.  
[24/02/28] We supported weight-decomposed LoRA (**[DoRA](https://arxiv.org/abs/2402.09353)**). Try `use_dora: true` to activate DoRA training.  
[24/02/15] We supported **block expansion** proposed by [LLaMA Pro](https://github.com/TencentARC/LLaMA-Pro). See [examples](examples/README.md) for usage.  
[24/02/05] Qwen1.5 (Qwen2 beta version) series models are supported in LLaMA-Factory. Check this [blog post](https://qwenlm.github.io/blog/qwen1.5/) for details.  
[24/01/18] We supported **agent tuning** for most models, equipping model with tool using abilities by fine-tuning with `dataset: glaive_toolcall_en`.  
[23/12/23] We supported **[unsloth](https://github.com/unslothai/unsloth)**'s implementation to boost LoRA tuning for the LLaMA, Mistral and Yi models. Try `use_unsloth: true` argument to activate unsloth patch. It achieves **170%** speed in our benchmark, check [this page](https://github.com/hiyouga/LLaMA-Factory/wiki/Performance-comparison) for details.  
[23/12/12] We supported fine-tuning the latest MoE model **[Mixtral 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)** in our framework. See hardware requirement [here](#hardware-requirement).  
[23/12/01] We supported downloading pre-trained models and datasets from the **[ModelScope Hub](https://modelscope.cn/models)**. See [this tutorial](#download-from-modelscope-hub) for usage.  
[23/10/21] We supported **[NEFTune](https://arxiv.org/abs/2310.05914)** trick for fine-tuning. Try `neftune_noise_alpha: 5` argument to activate NEFTune.  
[23/09/27] We supported **$S^2$-Attn** proposed by [LongLoRA](https://github.com/dvlab-research/LongLoRA) for the LLaMA models. Try `shift_attn: true` argument to enable shift short attention.  
[23/09/23] We integrated MMLU, C-Eval and CMMLU benchmarks in this repo. See [examples](examples/README.md) for usage.  
[23/09/10] We supported **[FlashAttention-2](https://github.com/Dao-AILab/flash-attention)**. Try `flash_attn: fa2` argument to enable FlashAttention-2 if you are using RTX4090, A100 or H100 GPUs.  
[23/08/12] We supported **RoPE scaling** to extend the context length of the LLaMA models. Try `rope_scaling: linear` argument in training and `rope_scaling: dynamic` argument at inference to extrapolate the position embeddings.  
[23/08/11] We supported **[DPO training](https://arxiv.org/abs/2305.18290)** for instruction-tuned models. See [examples](examples/README.md) for usage.  
[23/07/31] We supported **dataset streaming**. Try `streaming: true` and `max_steps: 10000` arguments to load your dataset in streaming mode.  
[23/07/29] We released two instruction-tuned 13B models at Hugging Face. See these Hugging Face Repos ([LLaMA-2](https://huggingface.co/hiyouga/Llama-2-Chinese-13b-chat) / [Baichuan](https://huggingface.co/hiyouga/Baichuan-13B-sft)) for details.  
[23/07/18] We developed an **all-in-one Web UI** for training, evaluation and inference. Try `train_web.py` to fine-tune models in your Web browser. Thank [@KanadeSiina](https://github.com/KanadeSiina) and [@codemayq](https://github.com/codemayq) for their efforts in the development.  
[23/07/09] We released **[FastEdit](https://github.com/hiyouga/FastEdit)** ⚡🩹, an easy-to-use package for editing the factual knowledge of large language models efficiently. Please follow [FastEdit](https://github.com/hiyouga/FastEdit) if you are interested.  
[23/06/29] We provided a **reproducible example** of training a chat model using instruction-following datasets, see [Baichuan-7B-sft](https://huggingface.co/hiyouga/Baichuan-7B-sft) for details.  
[23/06/22] We aligned the [demo API](src/api_demo.py) with the [OpenAI's](https://platform.openai.com/docs/api-reference/chat) format where you can insert the fine-tuned model in **arbitrary ChatGPT-based applications**.  
[23/06/03] We supported quantized training and inference (aka **[QLoRA](https://github.com/artidoro/qlora)**). See [examples](examples/README.md) for usage.  
</details>  
> [!TIP]
> If you cannot use the latest feature, please pull the latest code and install LLaMA-Factory again.