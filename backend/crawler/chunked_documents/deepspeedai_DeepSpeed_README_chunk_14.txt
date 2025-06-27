Repository: deepspeedai/DeepSpeed
Language: Python
Stars: 39026
Forks: 4426
-----
The quickest way to get started with DeepSpeed is via pip, this will install
the latest release of DeepSpeed which is not tied to specific PyTorch or CUDA
versions. DeepSpeed includes several C++/CUDA extensions that we commonly refer
to as our 'ops'.  By default, all of these extensions/ops will be built
just-in-time (JIT) using [torch's JIT C++ extension loader that relies on
ninja](https://pytorch.org/docs/stable/cpp_extension.html) to build and
dynamically link them at runtime.