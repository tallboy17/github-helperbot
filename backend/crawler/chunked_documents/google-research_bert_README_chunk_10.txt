Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
The Stanford Question Answering Dataset (SQuAD) is a popular question answering
benchmark dataset. BERT (at the time of the release) obtains state-of-the-art
results on SQuAD with almost no task-specific network architecture modifications
or data augmentation. However, it does require semi-complex data pre-processing
and post-processing to deal with (a) the variable-length nature of SQuAD context
paragraphs, and (b) the character-level answer annotations which are used for
SQuAD training. This processing is implemented and documented in `run_squad.py`.  
To run on SQuAD, you will first need to download the dataset. The
[SQuAD website](https://rajpurkar.github.io/SQuAD-explorer/) does not seem to
link to the v1.1 datasets any longer, but the necessary files can be found here:  
*   [train-v1.1.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json)
*   [dev-v1.1.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json)
*   [evaluate-v1.1.py](https://github.com/allenai/bi-att-flow/blob/master/squad/evaluate-v1.1.py)  
Download these to some directory `$SQUAD_DIR`.  
The state-of-the-art SQuAD results from the paper currently cannot be reproduced
on a 12GB-16GB GPU due to memory constraints (in fact, even batch size 1 does
not seem to fit on a 12GB GPU using `BERT-Large`). However, a reasonably strong
`BERT-Base` model can be trained on the GPU with these hyperparameters:  
```shell
python run_squad.py \
--vocab_file=$BERT_BASE_DIR/vocab.txt \
--bert_config_file=$BERT_BASE_DIR/bert_config.json \
--init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
--do_train=True \
--train_file=$SQUAD_DIR/train-v1.1.json \
--do_predict=True \
--predict_file=$SQUAD_DIR/dev-v1.1.json \
--train_batch_size=12 \
--learning_rate=3e-5 \
--num_train_epochs=2.0 \
--max_seq_length=384 \
--doc_stride=128 \
--output_dir=/tmp/squad_base/
```  
The dev set predictions will be saved into a file called `predictions.json` in
the `output_dir`:  
```shell
python $SQUAD_DIR/evaluate-v1.1.py $SQUAD_DIR/dev-v1.1.json ./squad/predictions.json
```  
Which should produce an output like this:  
```shell
{"f1": 88.41249612335034, "exact_match": 81.2488174077578}
```  
You should see a result similar to the 88.5% reported in the paper for
`BERT-Base`.  
If you have access to a Cloud TPU, you can train with `BERT-Large`. Here is a
set of hyperparameters (slightly different than the paper) which consistently
obtain around 90.5%-91.0% F1 single-system trained only on SQuAD:  
```shell
python run_squad.py \
--vocab_file=$BERT_LARGE_DIR/vocab.txt \
--bert_config_file=$BERT_LARGE_DIR/bert_config.json \
--init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
--do_train=True \
--train_file=$SQUAD_DIR/train-v1.1.json \
--do_predict=True \
--predict_file=$SQUAD_DIR/dev-v1.1.json \
--train_batch_size=24 \
--learning_rate=3e-5 \
--num_train_epochs=2.0 \
--max_seq_length=384 \
--doc_stride=128 \
--output_dir=gs://some_bucket/squad_large/ \
--use_tpu=True \
--tpu_name=$TPU_NAME
```  
For example, one random run with these parameters produces the following Dev
scores:  
```shell
{"f1": 90.87081895814865, "exact_match": 84.38978240302744}
```  
If you fine-tune for one epoch on
[TriviaQA](http://nlp.cs.washington.edu/triviaqa/) before this the results will
be even better, but you will need to convert TriviaQA into the SQuAD json
format.