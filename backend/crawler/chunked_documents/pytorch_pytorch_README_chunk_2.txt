Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
[Learn the basics of PyTorch](https://pytorch.org/tutorials/beginner/basics/intro.html)  
At a granular level, PyTorch is a library that consists of the following components:  
| Component | Description |
| ---- | --- |
| [**torch**](https://pytorch.org/docs/stable/torch.html) | A Tensor library like NumPy, with strong GPU support |
| [**torch.autograd**](https://pytorch.org/docs/stable/autograd.html) | A tape-based automatic differentiation library that supports all differentiable Tensor operations in torch |
| [**torch.jit**](https://pytorch.org/docs/stable/jit.html) | A compilation stack (TorchScript) to create serializable and optimizable models from PyTorch code  |
| [**torch.nn**](https://pytorch.org/docs/stable/nn.html) | A neural networks library deeply integrated with autograd designed for maximum flexibility |
| [**torch.multiprocessing**](https://pytorch.org/docs/stable/multiprocessing.html) | Python multiprocessing, but with magical memory sharing of torch Tensors across processes. Useful for data loading and Hogwild training |
| [**torch.utils**](https://pytorch.org/docs/stable/data.html) | DataLoader and other utility functions for convenience |  
Usually, PyTorch is used either as:  
- A replacement for NumPy to use the power of GPUs.
- A deep learning research platform that provides maximum flexibility and speed.  
Elaborating Further: