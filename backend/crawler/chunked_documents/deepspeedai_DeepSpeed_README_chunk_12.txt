Repository: deepspeedai/DeepSpeed
Language: Python
Stars: 39026
Forks: 4426
-----
DeepSpeed was an important part of Microsoft’s
[AI at Scale](https://www.microsoft.com/en-us/research/project/ai-at-scale/)
initiative to enable next-generation AI capabilities at scale, where you can find more
information [here](https://innovation.microsoft.com/en-us/exploring-ai-at-scale).  
DeepSpeed has been used to train many different large-scale models, below is a list of several examples that we are aware of (if you'd like to include your model please submit a PR):  
* [Megatron-Turing NLG (530B)](https://www.microsoft.com/en-us/research/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/)
* [Jurassic-1 (178B)](https://uploads-ssl.webflow.com/60fd4503684b466578c0d307/61138924626a6981ee09caf6_jurassic_tech_paper.pdf)
* [BLOOM (176B)](https://huggingface.co/blog/bloom-megatron-deepspeed)
* [GLM (130B)](https://github.com/THUDM/GLM-130B)
* [xTrimoPGLM (100B)](https://www.biorxiv.org/content/10.1101/2023.07.05.547496v2)
* [YaLM (100B)](https://github.com/yandex/YaLM-100B)
* [GPT-NeoX (20B)](https://github.com/EleutherAI/gpt-neox)
* [AlexaTM (20B)](https://www.amazon.science/blog/20b-parameter-alexa-model-sets-new-marks-in-few-shot-learning)
* [Turing NLG (17B)](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/)
* [METRO-LM (5.4B)](https://arxiv.org/pdf/2204.06644.pdf)  
DeepSpeed has been integrated with several different popular open-source DL frameworks such as:  
|                                                                                                | Documentation                                |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
<img src="docs/assets/images/transformers-light.png#gh-light-mode-only" width="250px"><img src="docs/assets/images/transformers-dark.png#gh-dark-mode-only" width="250px"> | [Transformers with DeepSpeed](https://huggingface.co/docs/transformers/deepspeed) |
| <img src="docs/assets/images/accelerate-light.png#gh-light-mode-only" width="250px"><img src="docs/assets/images/accelerate-dark.png#gh-dark-mode-only" width="250px"> | [Accelerate with DeepSpeed](https://huggingface.co/docs/accelerate/usage_guides/deepspeed) |
| <img src="docs/assets/images/lightning-light.svg#gh-light-mode-only" width="200px"><img src="docs/assets/images/lightning-dark.svg#gh-dark-mode-only" width="200px"> | [Lightning with DeepSpeed](https://lightning.ai/docs/pytorch/stable/advanced/model_parallel.html#deepspeed) |
| <img src="docs/assets/images/mosaicml.svg" width="200px"> | [MosaicML with DeepSpeed](https://docs.mosaicml.com/projects/composer/en/latest/trainer/using_the_trainer.html?highlight=deepspeed#deepspeed-integration) |
| <img src="docs/assets/images/determined.svg" width="225px"> | [Determined with DeepSpeed](https://docs.determined.ai/latest/training/apis-howto/deepspeed/overview.html) |
| <img src="https://user-images.githubusercontent.com/58739961/187154444-fce76639-ac8d-429b-9354-c6fac64b7ef8.jpg" width=150> | [MMEngine with DeepSpeed](https://mmengine.readthedocs.io/en/latest/common_usage/large_model_training.html#deepspeed) |  
---