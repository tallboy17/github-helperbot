Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
- Supports **full-finetuning**, pretraining, 4b-bit, 16-bit and **8-bit** training
- Supports **all transformer-style models** including [TTS, STT](https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning), multimodal, diffusion, [BERT](https://docs.unsloth.ai/get-started/unsloth-notebooks#other-important-notebooks) and more!
- All kernels written in [OpenAI's Triton](https://openai.com/index/triton/) language. **Manual backprop engine**.
- **0% loss in accuracy** - no approximation methods - all exact.
- No change of hardware. Supports NVIDIA GPUs since 2018+. Minimum CUDA Capability 7.0 (V100, T4, Titan V, RTX 20, 30, 40x, A100, H100, L40 etc) [Check your GPU!](https://developer.nvidia.com/cuda-gpus) GTX 1070, 1080 works, but is slow.
- Works on **Linux** and **Windows**
- If you trained a model with 🦥Unsloth, you can use this cool sticker! &nbsp; <img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/made with unsloth.png" height="50" align="center" />