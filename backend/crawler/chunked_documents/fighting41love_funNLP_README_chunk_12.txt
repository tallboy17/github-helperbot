Repository: fighting41love/funNLP
Language: Python
Stars: 74199
Forks: 14882
-----
| 资源名（Name）      | 描述（Description） | 链接     |
| :---        |    :----   |          :--- |
|  DeepFloyd IF    |  高度逼真且具有语言理解能力的最新开源文本到图像模型，由一个冻结文本编码器和三个连续的像素扩散模块组成，是一个高效的模型，性超越了当前最先进的模型，在COCO数据集上实现了零样本的FID得分为6.66     |    [github](https://github.com/deep-floyd/IF)   |
|  Multi-modal GPT    |   用多模态GPT训练一个能同时接收视觉和语言指令的聊天机器人。基于OpenFlamingo多模态模型，使用各种开放数据集创建各种视觉指导数据，联合训练视觉和语言指导，有效提高模型性能    |   [github](https://github.com/open-mmlab/Multimodal-GPT)    |
|   AudioGPT   |   Understanding and Generating Speech, Music, Sound, and Talking Head' by AIGC-Audio    |   [github](https://github.com/AIGC-Audio/AudioGPT)    |
|   text2image-prompt-generator   |    基于GPT-2用25万条Midjourney的promps训练出来的小模型，可以生成高质量的Midjourney  prompt   |    [link](https://huggingface.co/succinctly/text2image-prompt-generator)  [data](https://huggingface.co/datasets/succinctly/midjourney-prompts) |
|  汇总6个Midjourney以外的免费以文生图服务：    |       |   [Bing Image Creator](http://t.cn/A6C1cnVg) [Playground AI](http://t.cn/A6CtFmLN) [DreamStudio](http://t.cn/A6NSI6la) [Pixlr](http://t.cn/A6NSI6li)  [Leonardo AI ](http://t.cn/A6NSI6lS)[Craiyon](http://t.cn/A6NSI6lX)    |
| BARK   |   一个非常强大的TTS（文字转语音）项目，这个项目的特点是，它可以在文字中加入提示词，比如“大笑”。这个提示词会变成笑的声音，然后合成到语音里去。它也可以混合“男声”，“女声”，这样再做就可以不用再做拼接操作了    |   [github](https://github.com/suno-ai/bark)    |
|  whisper    |   在语音转文字（STT，也称ASR）方面，whisper是我用过的最好的，最快的库。没想到，这么快的模型，还能70x的优化空间。我准备部署这个模型，并开放给大家使用，可以用来转录大的语音文件，和进行翻译。这个模型是多语言的，而且能自动识别是什么语言，真的非常强大    |    [github](https://github.com/sanchit-gandhi/whisper-jax)   |
|  OFA-Chinese：中文多模态统一预训练模型    |  transformers结构的中文OFA模型     |    [github](https://github.com/yangjianxin1/OFA-Chinese)   |
|文生图开源模型试炼场|可根据输入文字同时用stable-diffusion 1.5、stable-diffusion 2.1、DALL-E、kandinsky-2等模型生成图像，方便测试比较|[link](https://zoo.replicate.dev/?id=a-still-life-of-birds-analytical-art-by-ludwig-knaus-wfsbarr)|
|LLMScore|LLMScore是一种全新的框架，能够提供具有多粒度组合性的评估分数。它使用大语言模型（LLM）来评估文本到图像生成模型。首先，将图像转化为图像级别和对象级别的视觉描述，然后将评估指令输入到LLM中，以衡量合成图像与文本的对齐程度，并最终生成一个评分和解释。我们的大量分析显示，LLMScore在众多数据集上与人类判断的相关性最高，明显优于常用的文本-图像匹配度量指标CLIP和BLIP。|[paper](https://arxiv.org/abs/2305.11116)[github](https://github.com/YujieLu10/LLMScore)|
|VisualGLM-6B|VisualGLM-6B 是一个开源的，支持图像、中文和英文的多模态对话语言模型，语言模型基于 ChatGLM-6B，具有 62 亿参数；图像部分通过训练 BLIP2-Qformer 构建起视觉模型与语言模型的桥梁，整体模型共78亿参数。|[github](https://github.com/THUDM/VisualGLM-6B)|