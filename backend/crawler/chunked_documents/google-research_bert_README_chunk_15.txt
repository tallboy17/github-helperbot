Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
We are releasing code to do "masked LM" and "next sentence prediction" on an
arbitrary text corpus. Note that this is *not* the exact code that was used for
the paper (the original code was written in C++, and had some additional
complexity), but this code does generate pre-training data as described in the
paper.  
Here's how to run the data generation. The input is a plain text file, with one
sentence per line. (It is important that these be actual sentences for the "next
sentence prediction" task). Documents are delimited by empty lines. The output
is a set of `tf.train.Example`s serialized into `TFRecord` file format.  
You can perform sentence segmentation with an off-the-shelf NLP toolkit such as
[spaCy](https://spacy.io/). The `create_pretraining_data.py` script will
concatenate segments until they reach the maximum sequence length to minimize
computational waste from padding (see the script for more details). However, you
may want to intentionally add a slight amount of noise to your input data (e.g.,
randomly truncate 2% of input segments) to make it more robust to non-sentential
input during fine-tuning.  
This script stores all of the examples for the entire input file in memory, so
for large data files you should shard the input file and call the script
multiple times. (You can pass in a file glob to `run_pretraining.py`, e.g.,
`tf_examples.tf_record*`.)  
The `max_predictions_per_seq` is the maximum number of masked LM predictions per
sequence. You should set this to around `max_seq_length` * `masked_lm_prob` (the
script doesn't do that automatically because the exact value needs to be passed
to both scripts).  
```shell
python create_pretraining_data.py \
--input_file=./sample_text.txt \
--output_file=/tmp/tf_examples.tfrecord \
--vocab_file=$BERT_BASE_DIR/vocab.txt \
--do_lower_case=True \
--max_seq_length=128 \
--max_predictions_per_seq=20 \
--masked_lm_prob=0.15 \
--random_seed=12345 \
--dupe_factor=5
```  
Here's how to run the pre-training. Do not include `init_checkpoint` if you are
pre-training from scratch. The model configuration (including vocab size) is
specified in `bert_config_file`. This demo code only pre-trains for a small
number of steps (20), but in practice you will probably want to set
`num_train_steps` to 10000 steps or more. The `max_seq_length` and
`max_predictions_per_seq` parameters passed to `run_pretraining.py` must be the
same as `create_pretraining_data.py`.  
```shell
python run_pretraining.py \
--input_file=/tmp/tf_examples.tfrecord \
--output_dir=/tmp/pretraining_output \
--do_train=True \
--do_eval=True \
--bert_config_file=$BERT_BASE_DIR/bert_config.json \
--init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
--train_batch_size=32 \
--max_seq_length=128 \
--max_predictions_per_seq=20 \
--num_train_steps=20 \
--num_warmup_steps=10 \
--learning_rate=2e-5
```  
This will produce an output like this:  
```
***** Eval results *****
global_step = 20
loss = 0.0979674
masked_lm_accuracy = 0.985479
masked_lm_loss = 0.0979328
next_sentence_accuracy = 1.0
next_sentence_loss = 3.45724e-05
```  
Note that since our `sample_text.txt` file is very small, this example training
will overfit that data in only a few steps and produce unrealistically high
accuracy numbers.