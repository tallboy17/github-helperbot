Repository: THUDM/ChatGLM-6B
Language: Python
Stars: 41067
Forks: 5214
-----
由于 ChatGLM-6B 的小规模，其能力仍然有许多局限性。以下是我们目前发现的一些问题：  
- 模型容量较小：6B 的小容量，决定了其相对较弱的模型记忆和语言能力。在面对许多事实性知识任务时，ChatGLM-6B 可能会生成不正确的信息；它也不擅长逻辑类问题（如数学、编程）的解答。
<details><summary><b>点击查看例子</b></summary>  
![](limitations/factual_error.png)  
![](limitations/math_error.png)  
</details>  
- 产生有害说明或有偏见的内容：ChatGLM-6B 只是一个初步与人类意图对齐的语言模型，可能会生成有害、有偏见的内容。（内容可能具有冒犯性，此处不展示）  
- 英文能力不足：ChatGLM-6B 训练时使用的指示/回答大部分都是中文的，仅有极小一部分英文内容。因此，如果输入英文指示，回复的质量远不如中文，甚至与中文指示下的内容矛盾，并且出现中英夹杂的情况。  
- 易被误导，对话能力较弱：ChatGLM-6B 对话能力还比较弱，而且 “自我认知” 存在问题，并很容易被误导并产生错误的言论。例如当前版本的模型在被误导的情况下，会在自我认知上发生偏差。
<details><summary><b>点击查看例子</b></summary>  
![](limitations/self-confusion_google.jpg)  
![](limitations/self-confusion_openai.jpg)  
![](limitations/self-confusion_tencent.jpg)  
</details>