Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
PyTorch has a unique way of building neural networks: using and replaying a tape recorder.  
Most frameworks such as TensorFlow, Theano, Caffe, and CNTK have a static view of the world.
One has to build a neural network and reuse the same structure again and again.
Changing the way the network behaves means that one has to start from scratch.  
With PyTorch, we use a technique called reverse-mode auto-differentiation, which allows you to
change the way your network behaves arbitrarily with zero lag or overhead. Our inspiration comes
from several research papers on this topic, as well as current and past work such as
[torch-autograd](https://github.com/twitter/torch-autograd),
[autograd](https://github.com/HIPS/autograd),
[Chainer](https://chainer.org), etc.  
While this technique is not unique to PyTorch, it's one of the fastest implementations of it to date.
You get the best of speed and flexibility for your crazy research.  
![Dynamic graph](https://github.com/pytorch/pytorch/raw/main/docs/source/_static/img/dynamic_graph.gif)