Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
**\*\*\*\*\* New March 11th, 2020: Smaller BERT Models \*\*\*\*\***  
This is a release of 24 smaller BERT models (English only, uncased, trained with WordPiece masking) referenced in [Well-Read Students Learn Better: On the Importance of Pre-training Compact Models](https://arxiv.org/abs/1908.08962).  
We have shown that the standard BERT recipe (including model architecture and training objective) is effective on a wide range of model sizes, beyond BERT-Base and BERT-Large. The smaller BERT models are intended for environments with restricted computational resources. They can be fine-tuned in the same manner as the original BERT models. However, they are most effective in the context of knowledge distillation, where the fine-tuning labels are produced by a larger and more accurate teacher.  
Our goal is to enable research in institutions with fewer computational resources and encourage the community to seek directions of innovation alternative to increasing model capacity.  
You can download all 24 from [here][all], or individually from the table below:  
|   |H=128|H=256|H=512|H=768|
|---|:---:|:---:|:---:|:---:|
| **L=2**  |[**2/128 (BERT-Tiny)**][2_128]|[2/256][2_256]|[2/512][2_512]|[2/768][2_768]|
| **L=4**  |[4/128][4_128]|[**4/256 (BERT-Mini)**][4_256]|[**4/512 (BERT-Small)**][4_512]|[4/768][4_768]|
| **L=6**  |[6/128][6_128]|[6/256][6_256]|[6/512][6_512]|[6/768][6_768]|
| **L=8**  |[8/128][8_128]|[8/256][8_256]|[**8/512 (BERT-Medium)**][8_512]|[8/768][8_768]|
| **L=10** |[10/128][10_128]|[10/256][10_256]|[10/512][10_512]|[10/768][10_768]|
| **L=12** |[12/128][12_128]|[12/256][12_256]|[12/512][12_512]|[**12/768 (BERT-Base)**][12_768]|  
Note that the BERT-Base model in this release is included for completeness only; it was re-trained under the same regime as the original model.  
Here are the corresponding GLUE scores on the test set:  
|Model|Score|CoLA|SST-2|MRPC|STS-B|QQP|MNLI-m|MNLI-mm|QNLI(v2)|RTE|WNLI|AX|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|BERT-Tiny|64.2|0.0|83.2|81.1/71.1|74.3/73.6|62.2/83.4|70.2|70.3|81.5|57.2|62.3|21.0|
|BERT-Mini|65.8|0.0|85.9|81.1/71.8|75.4/73.3|66.4/86.2|74.8|74.3|84.1|57.9|62.3|26.1|
|BERT-Small|71.2|27.8|89.7|83.4/76.2|78.8/77.0|68.1/87.0|77.6|77.0|86.4|61.8|62.3|28.6|
|BERT-Medium|73.5|38.0|89.6|86.6/81.6|80.4/78.4|69.6/87.9|80.0|79.1|87.7|62.2|62.3|30.5|  
For each task, we selected the best fine-tuning hyperparameters from the lists below, and trained for 4 epochs:
- batch sizes: 8, 16, 32, 64, 128
- learning rates: 3e-4, 1e-4, 5e-5, 3e-5  
If you use these models, please cite the following paper:  
```
@article{turc2019,
title={Well-Read Students Learn Better: On the Importance of Pre-training Compact Models},
author={Turc, Iulia and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
journal={arXiv preprint arXiv:1908.08962v2 },
year={2019}
}
```  
[2_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-2_H-128_A-2.zip
[2_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-2_H-256_A-4.zip
[2_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-2_H-512_A-8.zip
[2_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-2_H-768_A-12.zip
[4_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-4_H-128_A-2.zip
[4_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-4_H-256_A-4.zip
[4_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-4_H-512_A-8.zip
[4_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-4_H-768_A-12.zip
[6_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-6_H-128_A-2.zip
[6_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-6_H-256_A-4.zip
[6_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-6_H-512_A-8.zip
[6_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-6_H-768_A-12.zip
[8_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-8_H-128_A-2.zip
[8_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-8_H-256_A-4.zip
[8_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-8_H-512_A-8.zip
[8_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-8_H-768_A-12.zip
[10_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-10_H-128_A-2.zip
[10_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-10_H-256_A-4.zip
[10_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-10_H-512_A-8.zip
[10_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-10_H-768_A-12.zip
[12_128]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-128_A-2.zip
[12_256]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-256_A-4.zip
[12_512]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-512_A-8.zip
[12_768]: https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip
[all]: https://storage.googleapis.com/bert_models/2020_02_20/all_bert_models.zip  
**\*\*\*\*\* New May 31st, 2019: Whole Word Masking Models \*\*\*\*\***  
This is a release of several new models which were the result of an improvement
the pre-processing code.  
In the original pre-processing code, we randomly select WordPiece tokens to
mask. For example:  
`Input Text: the man jumped up , put his basket on phil ##am ##mon ' s head`
`Original Masked Input: [MASK] man [MASK] up , put his [MASK] on phil
[MASK] ##mon ' s head`  
The new technique is called Whole Word Masking. In this case, we always mask
*all* of the the tokens corresponding to a word at once. The overall masking
rate remains the same.  
`Whole Word Masked Input: the man [MASK] up , put his basket on [MASK] [MASK]
[MASK] ' s head`  
The training is identical -- we still predict each masked WordPiece token
independently. The improvement comes from the fact that the original prediction
task was too 'easy' for words that had been split into multiple WordPieces.  
This can be enabled during data generation by passing the flag
`--do_whole_word_mask=True` to `create_pretraining_data.py`.  
Pre-trained models with Whole Word Masking are linked below. The data and
training were otherwise identical, and the models have identical structure and
vocab to the original models. We only include BERT-Large models. When using
these models, please make it clear in the paper that you are using the Whole
Word Masking variant of BERT-Large.  
*   **[`BERT-Large, Uncased (Whole Word Masking)`](https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip)**:
24-layer, 1024-hidden, 16-heads, 340M parameters  
*   **[`BERT-Large, Cased (Whole Word Masking)`](https://storage.googleapis.com/bert_models/2019_05_30/wwm_cased_L-24_H-1024_A-16.zip)**:
24-layer, 1024-hidden, 16-heads, 340M parameters  
Model                                    | SQUAD 1.1 F1/EM | Multi NLI Accuracy
---------------------------------------- | :-------------: | :----------------:
BERT-Large, Uncased (Original)           | 91.0/84.3       | 86.05
BERT-Large, Uncased (Whole Word Masking) | 92.8/86.7       | 87.07
BERT-Large, Cased (Original)             | 91.5/84.8       | 86.09
BERT-Large, Cased (Whole Word Masking)   | 92.9/86.7       | 86.46  
**\*\*\*\*\* New February 7th, 2019: TfHub Module \*\*\*\*\***  
BERT has been uploaded to [TensorFlow Hub](https://tfhub.dev). See
`run_classifier_with_tfhub.py` for an example of how to use the TF Hub module,
or run an example in the browser on
[Colab](https://colab.sandbox.google.com/github/google-research/bert/blob/master/predicting_movie_reviews_with_bert_on_tf_hub.ipynb).  
**\*\*\*\*\* New November 23rd, 2018: Un-normalized multilingual model + Thai +
Mongolian \*\*\*\*\***  
We uploaded a new multilingual model which does *not* perform any normalization
on the input (no lower casing, accent stripping, or Unicode normalization), and
additionally inclues Thai and Mongolian.  
**It is recommended to use this version for developing multilingual models,
especially on languages with non-Latin alphabets.**  
This does not require any code changes, and can be downloaded here:  
*   **[`BERT-Base, Multilingual Cased`](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip)**:
104 languages, 12-layer, 768-hidden, 12-heads, 110M parameters  
**\*\*\*\*\* New November 15th, 2018: SOTA SQuAD 2.0 System \*\*\*\*\***  
We released code changes to reproduce our 83% F1 SQuAD 2.0 system, which is
currently 1st place on the leaderboard by 3%. See the SQuAD 2.0 section of the
README for details.  
**\*\*\*\*\* New November 5th, 2018: Third-party PyTorch and Chainer versions of
BERT available \*\*\*\*\***  
NLP researchers from HuggingFace made a
[PyTorch version of BERT available](https://github.com/huggingface/pytorch-pretrained-BERT)
which is compatible with our pre-trained checkpoints and is able to reproduce
our results. Sosuke Kobayashi also made a
[Chainer version of BERT available](https://github.com/soskek/bert-chainer)
(Thanks!) We were not involved in the creation or maintenance of the PyTorch
implementation so please direct any questions towards the authors of that
repository.  
**\*\*\*\*\* New November 3rd, 2018: Multilingual and Chinese models available
\*\*\*\*\***  
We have made two new BERT models available:  
*   **[`BERT-Base, Multilingual`](https://storage.googleapis.com/bert_models/2018_11_03/multilingual_L-12_H-768_A-12.zip)
(Not recommended, use `Multilingual Cased` instead)**: 102 languages,
12-layer, 768-hidden, 12-heads, 110M parameters
*   **[`BERT-Base, Chinese`](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)**:
Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M
parameters  
We use character-based tokenization for Chinese, and WordPiece tokenization for
all other languages. Both models should work out-of-the-box without any code
changes. We did update the implementation of `BasicTokenizer` in
`tokenization.py` to support Chinese character tokenization, so please update if
you forked it. However, we did not change the tokenization API.  
For more, see the
[Multilingual README](https://github.com/google-research/bert/blob/master/multilingual.md).  
**\*\*\*\*\* End new information \*\*\*\*\***