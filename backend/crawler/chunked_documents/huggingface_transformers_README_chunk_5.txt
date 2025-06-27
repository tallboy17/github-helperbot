Repository: huggingface/transformers
Language: Python
Stars: 145843
Forks: 29409
-----
- This library is not a modular toolbox of building blocks for neural nets. The code in the model files is not refactored with additional abstractions on purpose, so that researchers can quickly iterate on each of the models without diving into additional abstractions/files.
- The training API is optimized to work with PyTorch models provided by Transformers. For generic machine learning loops, you should use another library like [Accelerate](https://huggingface.co/docs/accelerate).
- The [example scripts]((https://github.com/huggingface/transformers/tree/main/examples)) are only *examples*. They may not necessarily work out-of-the-box on your specific use case and you'll need to adapt the code for it to work.