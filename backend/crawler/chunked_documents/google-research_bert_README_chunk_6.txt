Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
**Important**: All results on the paper were fine-tuned on a single Cloud TPU,
which has 64GB of RAM. It is currently not possible to re-produce most of the
`BERT-Large` results on the paper using a GPU with 12GB - 16GB of RAM, because
the maximum batch size that can fit in memory is too small. We are working on
adding code to this repository which allows for much larger effective batch size
on the GPU. See the section on [out-of-memory issues](#out-of-memory-issues) for
more details.  
This code was tested with TensorFlow 1.11.0. It was tested with Python2 and
Python3 (but more thoroughly with Python2, since this is what's used internally
in Google).  
The fine-tuning examples which use `BERT-Base` should be able to run on a GPU
that has at least 12GB of RAM using the hyperparameters given.