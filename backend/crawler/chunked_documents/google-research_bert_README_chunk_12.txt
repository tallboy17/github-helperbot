Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
All experiments in the paper were fine-tuned on a Cloud TPU, which has 64GB of
device RAM. Therefore, when using a GPU with 12GB - 16GB of RAM, you are likely
to encounter out-of-memory issues if you use the same hyperparameters described
in the paper.  
The factors that affect memory usage are:  
*   **`max_seq_length`**: The released models were trained with sequence lengths
up to 512, but you can fine-tune with a shorter max sequence length to save
substantial memory. This is controlled by the `max_seq_length` flag in our
example code.  
*   **`train_batch_size`**: The memory usage is also directly proportional to
the batch size.  
*   **Model type, `BERT-Base` vs. `BERT-Large`**: The `BERT-Large` model
requires significantly more memory than `BERT-Base`.  
*   **Optimizer**: The default optimizer for BERT is Adam, which requires a lot
of extra memory to store the `m` and `v` vectors. Switching to a more memory
efficient optimizer can reduce memory usage, but can also affect the
results. We have not experimented with other optimizers for fine-tuning.  
Using the default training scripts (`run_classifier.py` and `run_squad.py`), we
benchmarked the maximum batch size on single Titan X GPU (12GB RAM) with
TensorFlow 1.11.0:  
System       | Seq Length | Max Batch Size
------------ | ---------- | --------------
`BERT-Base`  | 64         | 64
...          | 128        | 32
...          | 256        | 16
...          | 320        | 14
...          | 384        | 12
...          | 512        | 6
`BERT-Large` | 64         | 12
...          | 128        | 6
...          | 256        | 2
...          | 320        | 1
...          | 384        | 0
...          | 512        | 0  
Unfortunately, these max batch sizes for `BERT-Large` are so small that they
will actually harm the model accuracy, regardless of the learning rate used. We
are working on adding code to this repository which will allow much larger
effective batch sizes to be used on the GPU. The code will be based on one (or
both) of the following techniques:  
*   **Gradient accumulation**: The samples in a minibatch are typically
independent with respect to gradient computation (excluding batch
normalization, which is not used here). This means that the gradients of
multiple smaller minibatches can be accumulated before performing the weight
update, and this will be exactly equivalent to a single larger update.  
*   [**Gradient checkpointing**](https://github.com/openai/gradient-checkpointing):
The major use of GPU/TPU memory during DNN training is caching the
intermediate activations in the forward pass that are necessary for
efficient computation in the backward pass. "Gradient checkpointing" trades
memory for compute time by re-computing the activations in an intelligent
way.  
**However, this is not implemented in the current release.**