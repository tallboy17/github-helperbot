Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
This repository does not include code for *learning* a new WordPiece vocabulary.
The reason is that the code used in the paper was implemented in C++ with
dependencies on Google's internal libraries. For English, it is almost always
better to just start with our vocabulary and pre-trained models. For learning
vocabularies of other languages, there are a number of open source options
available. However, keep in mind that these are not compatible with our
`tokenization.py` library:  
*   [Google's SentencePiece library](https://github.com/google/sentencepiece)  
*   [tensor2tensor's WordPiece generation script](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/text_encoder_build_subword.py)  
*   [Rico Sennrich's Byte Pair Encoding library](https://github.com/rsennrich/subword-nmt)