Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
We are releasing the following:  
*   TensorFlow code for the BERT model architecture (which is mostly a standard
[Transformer](https://arxiv.org/abs/1706.03762) architecture).
*   Pre-trained checkpoints for both the lowercase and cased version of
`BERT-Base` and `BERT-Large` from the paper.
*   TensorFlow code for push-button replication of the most important
fine-tuning experiments from the paper, including SQuAD, MultiNLI, and MRPC.  
All of the code in this repository works out-of-the-box with CPU, GPU, and Cloud
TPU.