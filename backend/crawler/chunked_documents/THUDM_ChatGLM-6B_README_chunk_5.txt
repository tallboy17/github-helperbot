Repository: THUDM/ChatGLM-6B
Language: Python
Stars: 41067
Forks: 5214
-----
对 ChatGLM 进行加速的开源项目：
* [lyraChatGLM](https://huggingface.co/TMElyralab/lyraChatGLM): 对 ChatGLM-6B 进行推理加速，最高可以实现 9000+ tokens/s 的推理速度
* [ChatGLM-MNN](https://github.com/wangzhaode/ChatGLM-MNN): 一个基于 MNN 的 ChatGLM-6B C++ 推理实现，支持根据显存大小自动分配计算任务给 GPU 和 CPU
* [JittorLLMs](https://github.com/Jittor/JittorLLMs)：最低3G显存或者没有显卡都可运行 ChatGLM-6B FP16， 支持Linux、windows、Mac部署
* [InferLLM](https://github.com/MegEngine/InferLLM)：轻量级 C++ 推理，可以实现本地 x86，Arm 处理器上实时聊天，手机上也同样可以实时运行，运行内存只需要 4G  
基于或使用了 ChatGLM-6B 的开源项目：
* [langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM)：基于 langchain 的 ChatGLM 应用，实现基于可扩展知识库的问答
* [闻达](https://github.com/l15y/wenda)：大型语言模型调用平台，基于 ChatGLM-6B 实现了类 ChatPDF 功能
* [glm-bot](https://github.com/initialencounter/glm-bot)：将ChatGLM接入Koishi可在各大聊天平台上调用ChatGLM
* [Chuanhu Chat](https://github.com/GaiZhenbiao/ChuanhuChatGPT): 为各个大语言模型和在线模型API提供美观易用、功能丰富、快速部署的用户界面，支持ChatGLM-6B。  
支持 ChatGLM-6B 和相关应用在线训练的示例项目：
* [ChatGLM-6B 的部署与微调教程](https://www.heywhale.com/mw/project/6436d82948f7da1fee2be59e)
* [ChatGLM-6B 结合 langchain 实现本地知识库 QA Bot](https://www.heywhale.com/mw/project/643977aa446c45f4592a1e59)  
第三方评测：
* [Measuring Massive Multitask Chinese Understanding](https://arxiv.org/abs/2304.12986)  
更多开源项目参见 [PROJECT.md](PROJECT.md)