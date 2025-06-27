Repository: THUDM/ChatGLM-6B
Language: Python
Stars: 41067
Forks: 5214
-----
**[2023/07/25]** 发布 [CodeGeeX2](https://github.com/THUDM/CodeGeeX2) ，基于 ChatGLM2-6B 的代码生成模型，代码能力全面提升，更多特性包括：  
* **更强大的代码能力**：CodeGeeX2-6B 进一步经过了 600B 代码数据预训练，相比 CodeGeeX 一代模型，在代码能力上全面提升，[HumanEval-X](https://huggingface.co/datasets/THUDM/humaneval-x) 评测集的六种编程语言均大幅提升 (Python +57%, C++ +71%, Java +54%, JavaScript +83%, Go +56%, Rust +321\%)，在Python上达到 35.9\% 的 Pass@1 一次通过率，超越规模更大的 StarCoder-15B。
* **更优秀的模型特性**：继承 ChatGLM2-6B 模型特性，CodeGeeX2-6B 更好支持中英文输入，支持最大 8192 序列长度，推理速度较一代 大幅提升，量化后仅需6GB显存即可运行，支持轻量级本地化部署。
* **更全面的AI编程助手**：CodeGeeX插件（[VS Code](https://marketplace.visualstudio.com/items?itemName=aminer.codegeex), [Jetbrains](https://plugins.jetbrains.com/plugin/20587-codegeex)）后端升级，支持超过100种编程语言，新增上下文补全、跨文件补全等实用功能。结合 Ask CodeGeeX 交互式AI编程助手，支持中英文对话解决各种编程问题，包括且不限于代码解释、代码翻译、代码纠错、文档生成等，帮助程序员更高效开发。  
**[2023/06/25]** 发布 [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)，ChatGLM-6B 的升级版本，在保留了了初代模型对话流畅、部署门槛较低等众多优秀特性的基础之上，ChatGLM**2**-6B 引入了如下新特性：  
1. **更强大的性能**：基于 ChatGLM 初代模型的开发经验，我们全面升级了 ChatGLM2-6B 的基座模型。ChatGLM2-6B 使用了 [GLM](https://github.com/THUDM/GLM) 的混合目标函数，经过了 1.4T 中英标识符的预训练与人类偏好对齐训练，[评测结果](#评测结果)显示，相比于初代模型，ChatGLM2-6B 在 MMLU（+23%）、CEval（+33%）、GSM8K（+571%） 、BBH（+60%）等数据集上的性能取得了大幅度的提升，在同尺寸开源模型中具有较强的竞争力。
2. **更长的上下文**：基于 [FlashAttention](https://github.com/HazyResearch/flash-attention) 技术，我们将基座模型的上下文长度（Context Length）由 ChatGLM-6B 的 2K 扩展到了 32K，并在对话阶段使用 8K 的上下文长度训练，允许更多轮次的对话。但当前版本的 ChatGLM2-6B 对单轮超长文档的理解能力有限，我们会在后续迭代升级中着重进行优化。
3. **更高效的推理**：基于 [Multi-Query Attention](http://arxiv.org/abs/1911.02150) 技术，ChatGLM2-6B 有更高效的推理速度和更低的显存占用：在官方的模型实现下，推理速度相比初代提升了 42%，INT4 量化下，6G 显存支持的对话长度由 1K 提升到了 8K。  
更多信息参见 [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)。  
**[2023/06/14]** 发布 [WebGLM](https://github.com/THUDM/WebGLM)，一项被接受于KDD 2023的研究工作，支持利用网络信息生成带有准确引用的长回答。  
![](resources/webglm.jpg)  
**[2023/05/17]** 发布 [VisualGLM-6B](https://github.com/THUDM/VisualGLM-6B)，一个支持图像理解的多模态对话语言模型。  
![](resources/visualglm.png)  
可以通过本仓库中的 [cli_demo_vision.py](cli_demo_vision.py) 和 [web_demo_vision.py](web_demo_vision.py) 来运行命令行和网页 Demo。注意 VisualGLM-6B 需要额外安装 [SwissArmyTransformer](https://github.com/THUDM/SwissArmyTransformer/) 和 torchvision。更多信息参见 [VisualGLM-6B](https://github.com/THUDM/VisualGLM-6B)。  
**[2023/05/15]** 更新 v1.1 版本 checkpoint，训练数据增加英文指令微调数据以平衡中英文数据比例，解决英文回答中夹杂中文词语的现象。  
<details><summary><b>以下是更新前后的英文问题对比：</b></summary>  
* 问题：Describe a time when you had to make a difficult decision.
- v1.0:
![](resources/english-q1-old.png)
- v1.1:
![](resources/english-q1-new.png)
* 问题：Describe the function of a computer motherboard
- v1.0:
![](resources/english-q2-old.png)
- v1.1:
![](resources/english-q2-new.png)
* 问题：Develop a plan to reduce electricity usage in a home.
- v1.0:
![](resources/english-q3-old.png)
- v1.1:
![](resources/english-q3-new.png)
* 问题：未来的NFT，可能真实定义一种现实的资产，它会是一处房产，一辆汽车，一片土地等等，这样的数字凭证可能比真实的东西更有价值，你可以随时交易和使用，在虚拟和现实中无缝的让拥有的资产继续创造价值，未来会是万物归我所用，但不归我所有的时代。翻译成专业的英语
- v1.0:
![](resources/english-q4-old.png)
- v1.1:
![](resources/english-q4-new.png)
</details>  
更多更新信息参见 [UPDATE.md](UPDATE.md)