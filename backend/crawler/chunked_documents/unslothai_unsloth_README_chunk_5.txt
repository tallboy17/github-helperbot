Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
- 📣 NEW! **[Text-to-Speech (TTS)](https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning)** is now supported, including `sesame/csm-1b` and STT `openai/whisper-large-v3`.
- 📣 NEW! **[Qwen3](https://docs.unsloth.ai/basics/qwen3-how-to-run-and-fine-tune)** is now supported. Qwen3-30B-A3B fits on 17.5GB VRAM.
- 📣 NEW! Introducing **[Dynamic 2.0](https://docs.unsloth.ai/basics/unsloth-dynamic-2.0-ggufs)** quants that set new benchmarks on 5-shot MMLU & KL Divergence.
- 📣 **[Llama 4](https://unsloth.ai/blog/llama4)** by Meta, including Scout & Maverick are now supported.
- 📣 [**EVERYTHING** is now supported](https://unsloth.ai/blog/gemma3#everything) - all models (BERT, diffusion, Cohere, Mamba), FFT, etc. MultiGPU coming soon. Enable FFT with `full_finetuning = True`, 8-bit with `load_in_8bit = True`.
- 📣 **Gemma 3** by Google: [Read Blog](https://unsloth.ai/blog/gemma3). We [uploaded GGUFs, 4-bit models](https://huggingface.co/collections/unsloth/gemma-3-67d12b7e8816ec6efa7e4e5b).
- 📣 Introducing Long-context [Reasoning (GRPO)](https://unsloth.ai/blog/grpo) in Unsloth. Train your own reasoning model with just 5GB VRAM. Transform Llama, Phi, Mistral etc. into reasoning LLMs!
- 📣 [DeepSeek-R1](https://unsloth.ai/blog/deepseek-r1) - run or fine-tune them [with our guide](https://unsloth.ai/blog/deepseek-r1). All model uploads: [here](https://huggingface.co/collections/unsloth/deepseek-r1-all-versions-678e1c48f5d2fce87892ace5).
<details>
<summary>Click for more news</summary>  
- 📣 Introducing Unsloth [Dynamic 4-bit Quantization](https://unsloth.ai/blog/dynamic-4bit)! We dynamically opt not to quantize certain parameters and this greatly increases accuracy while only using <10% more VRAM than BnB 4-bit. See our collection on [Hugging Face here.](https://huggingface.co/collections/unsloth/unsloth-4-bit-dynamic-quants-67503bb873f89e15276c44e7)
- 📣 [Phi-4](https://unsloth.ai/blog/phi4) by Microsoft: We also [fixed bugs](https://unsloth.ai/blog/phi4) in Phi-4 and [uploaded GGUFs, 4-bit](https://huggingface.co/collections/unsloth/phi-4-all-versions-677eecf93784e61afe762afa).
- 📣 [Vision models](https://unsloth.ai/blog/vision) now supported! [Llama 3.2 Vision (11B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(11B)-Vision.ipynb), [Qwen 2.5 VL (7B)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_VL_(7B)-Vision.ipynb) and [Pixtral (12B) 2409](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Pixtral_(12B)-Vision.ipynb)
- 📣 [Llama 3.3 (70B)](https://huggingface.co/collections/unsloth/llama-33-all-versions-67535d7d994794b9d7cf5e9f), Meta's latest model is supported.
- 📣 We worked with Apple to add [Cut Cross Entropy](https://arxiv.org/abs/2411.09009). Unsloth now supports 89K context for Meta's Llama 3.3 (70B) on a 80GB GPU - 13x longer than HF+FA2. For Llama 3.1 (8B), Unsloth enables 342K context, surpassing its native 128K support.
- 📣 We found and helped fix a [gradient accumulation bug](https://unsloth.ai/blog/gradient)! Please update Unsloth and transformers.
- 📣 We cut memory usage by a [further 30%](https://unsloth.ai/blog/long-context) and now support [4x longer context windows](https://unsloth.ai/blog/long-context)!
</details>