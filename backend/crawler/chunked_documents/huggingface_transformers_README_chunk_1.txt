Repository: huggingface/transformers
Language: Python
Stars: 145843
Forks: 29409
-----
<!---
Copyright 2020 The HuggingFace Team. All rights reserved.  
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at  
http://www.apache.org/licenses/LICENSE-2.0  
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->  
<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-dark.svg">
<source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-light.svg">
<img alt="Hugging Face Transformers Library" src="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-light.svg" width="352" height="59" style="max-width: 100%;">
</picture>
<br/>
<br/>
</p>  
<p align="center">
<a href="https://huggingface.com/models"><img alt="Checkpoints on Hub" src="https://img.shields.io/endpoint?url=https://huggingface.co/api/shields/models&color=brightgreen"></a>
<a href="https://circleci.com/gh/huggingface/transformers"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/main"></a>
<a href="https://github.com/huggingface/transformers/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/huggingface/transformers.svg?color=blue"></a>
<a href="https://huggingface.co/docs/transformers/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online"></a>
<a href="https://github.com/huggingface/transformers/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/transformers.svg"></a>
<a href="https://github.com/huggingface/transformers/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
<a href="https://zenodo.org/badge/latestdoi/155220641"><img src="https://zenodo.org/badge/155220641.svg" alt="DOI"></a>
</p>  
<h4 align="center">
<p>
<b>English</b> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hans.md">简体中文</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hant.md">繁體中文</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ko.md">한국어</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_es.md">Español</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ja.md">日本語</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_hd.md">हिन्दी</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ru.md">Русский</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_pt-br.md">Рortuguês</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_te.md">తెలుగు</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_fr.md">Français</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_de.md">Deutsch</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_vi.md">Tiếng Việt</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ar.md">العربية</a> |
<a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ur.md">اردو</a> |
</p>
</h4>  
<h3 align="center">
<p>State-of-the-art pretrained models for inference and training</p>
</h3>  
<h3 align="center">
<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/transformers_as_a_model_definition.png"/>
</h3>  
Transformers acts as the model-definition framework for state-of-the-art machine learning models in text, computer
vision, audio, video, and multimodal model, for both inference and training.  
It centralizes the model definition so that this definition is agreed upon across the ecosystem. `transformers` is the
pivot across frameworks: if a model definition is supported, it will be compatible with the majority of training
frameworks (Axolotl, Unsloth, DeepSpeed, FSDP, PyTorch-Lightning, ...), inference engines (vLLM, SGLang, TGI, ...),
and adjacent modeling libraries (llama.cpp, mlx, ...) which leverage the model definition from `transformers`.  
We pledge to help support new state-of-the-art models and democratize their usage by having their model definition be
simple, customizable, and efficient.  
There are over 1M+ Transformers [model checkpoints](https://huggingface.co/models?library=transformers&sort=trending) on the [Hugging Face Hub](https://huggingface.com/models) you can use.  
Explore the [Hub](https://huggingface.com/) today to find a model and use Transformers to help you get started right away.