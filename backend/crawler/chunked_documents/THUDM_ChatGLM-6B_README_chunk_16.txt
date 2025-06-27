Repository: THUDM/ChatGLM-6B
Language: Python
Stars: 41067
Forks: 5214
-----
对于搭载了 Apple Silicon 或者 AMD GPU 的Mac，可以使用 MPS 后端来在 GPU 上运行 ChatGLM-6B。需要参考 Apple 的 [官方说明](https://developer.apple.com/metal/pytorch) 安装 PyTorch-Nightly（正确的版本号应该是2.1.0.dev2023xxxx，而不是2.0.0）。  
目前在 MacOS 上只支持[从本地加载模型](README.md#从本地加载模型)。将代码中的模型加载改为从本地加载，并使用 mps 后端：
```python
model = AutoModel.from_pretrained("your local path", trust_remote_code=True).half().to('mps')
```  
加载半精度的 ChatGLM-6B 模型需要大概 13GB 内存。内存较小的机器（比如 16GB 内存的 MacBook Pro），在空余内存不足的情况下会使用硬盘上的虚拟内存，导致推理速度严重变慢。此时可以使用量化后的模型如 chatglm-6b-int4。因为 GPU 上量化的 kernel 是使用 CUDA 编写的，因此无法在 MacOS 上使用，只能使用 CPU 进行推理。
```python
# INT8 量化的模型将"THUDM/chatglm-6b-int4"改为"THUDM/chatglm-6b-int8"
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()
```
为了充分使用 CPU 并行，还需要[单独安装 OpenMP](FAQ.md#q1)。