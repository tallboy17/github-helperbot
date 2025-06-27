Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
**BERT**, or **B**idirectional **E**ncoder **R**epresentations from
**T**ransformers, is a new method of pre-training language representations which
obtains state-of-the-art results on a wide array of Natural Language Processing
(NLP) tasks.  
Our academic paper which describes BERT in detail and provides full results on a
number of tasks can be found here:
[https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805).  
To give a few numbers, here are the results on the
[SQuAD v1.1](https://rajpurkar.github.io/SQuAD-explorer/) question answering
task:  
SQuAD v1.1 Leaderboard (Oct 8th 2018) | Test EM  | Test F1
------------------------------------- | :------: | :------:
1st Place Ensemble - BERT             | **87.4** | **93.2**
2nd Place Ensemble - nlnet            | 86.0     | 91.7
1st Place Single Model - BERT         | **85.1** | **91.8**
2nd Place Single Model - nlnet        | 83.5     | 90.1  
And several natural language inference tasks:  
System                  | MultiNLI | Question NLI | SWAG
----------------------- | :------: | :----------: | :------:
BERT                    | **86.7** | **91.1**     | **86.3**
OpenAI GPT (Prev. SOTA) | 82.2     | 88.1         | 75.0  
Plus many other tasks.  
Moreover, these results were all obtained with almost no task-specific neural
network architecture design.  
If you already know what BERT is and you just want to get started, you can
[download the pre-trained models](#pre-trained-models) and
[run a state-of-the-art fine-tuning](#fine-tuning-with-bert) in only a few
minutes.