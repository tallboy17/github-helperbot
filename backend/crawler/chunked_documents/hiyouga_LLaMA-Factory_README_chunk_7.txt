Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
- **Various models**: LLaMA, LLaVA, Mistral, Mixtral-MoE, Qwen, Qwen2-VL, DeepSeek, Yi, Gemma, ChatGLM, Phi, etc.
- **Integrated methods**: (Continuous) pre-training, (multimodal) supervised fine-tuning, reward modeling, PPO, DPO, KTO, ORPO, etc.
- **Scalable resources**: 16-bit full-tuning, freeze-tuning, LoRA and 2/3/4/5/6/8-bit QLoRA via AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ.
- **Advanced algorithms**: [GaLore](https://github.com/jiaweizzhao/GaLore), [BAdam](https://github.com/Ledzy/BAdam), [APOLLO](https://github.com/zhuhanqing/APOLLO), [Adam-mini](https://github.com/zyushun/Adam-mini), [Muon](https://github.com/KellerJordan/Muon), DoRA, LongLoRA, LLaMA Pro, Mixture-of-Depths, LoRA+, LoftQ and PiSSA.
- **Practical tricks**: [FlashAttention-2](https://github.com/Dao-AILab/flash-attention), [Unsloth](https://github.com/unslothai/unsloth), [Liger Kernel](https://github.com/linkedin/Liger-Kernel), RoPE scaling, NEFTune and rsLoRA.
- **Wide tasks**: Multi-turn dialogue, tool using, image understanding, visual grounding, video recognition, audio understanding, etc.
- **Experiment monitors**: LlamaBoard, TensorBoard, Wandb, MLflow, [SwanLab](https://github.com/SwanHubX/SwanLab), etc.
- **Faster inference**: OpenAI-style API, Gradio UI and CLI with [vLLM worker](https://github.com/vllm-project/vllm) or [SGLang worker](https://github.com/sgl-project/sglang).