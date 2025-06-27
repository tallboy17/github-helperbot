Repository: THUDM/ChatGLM-6B
Language: Python
Stars: 41067
Forks: 5214
-----
默认情况下，模型以 FP16 精度加载，运行上述代码需要大概 13GB 显存。如果你的 GPU 显存有限，可以尝试以量化方式加载模型，使用方法如下：  
```python
# 按需修改，目前只支持 4/8 bit 量化
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).quantize(8).half().cuda()
```  
进行 2 至 3 轮对话后，8-bit 量化下 GPU 显存占用约为 10GB，4-bit 量化下仅需 6GB 占用。随着对话轮数的增多，对应消耗显存也随之增长，由于采用了相对位置编码，理论上 ChatGLM-6B 支持无限长的 context-length，但总长度超过 2048（训练长度）后性能会逐渐下降。  
模型量化会带来一定的性能损失，经过测试，ChatGLM-6B 在 4-bit 量化下仍然能够进行自然流畅的生成。使用 [GPT-Q](https://arxiv.org/abs/2210.17323) 等量化方案可以进一步压缩量化精度/提升相同量化精度下的模型性能，欢迎大家提出对应的 Pull Request。  
量化过程需要在内存中首先加载 FP16 格式的模型，消耗大概 13GB 的内存。如果你的内存不足的话，可以直接加载量化后的模型，INT4 量化后的模型仅需大概 5.2GB 的内存：
```python
# INT8 量化的模型将"THUDM/chatglm-6b-int4"改为"THUDM/chatglm-6b-int8"
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
```
量化模型的参数文件也可以从[这里](https://cloud.tsinghua.edu.cn/d/674208019e314311ab5c/)手动下载。