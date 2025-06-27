Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
This model is also implemented and documented in `run_squad.py`.  
To run on SQuAD 2.0, you will first need to download the dataset. The necessary
files can be found here:  
*   [train-v2.0.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json)
*   [dev-v2.0.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json)
*   [evaluate-v2.0.py](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/)  
Download these to some directory `$SQUAD_DIR`.  
On Cloud TPU you can run with BERT-Large as follows:  
```shell
python run_squad.py \
--vocab_file=$BERT_LARGE_DIR/vocab.txt \
--bert_config_file=$BERT_LARGE_DIR/bert_config.json \
--init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
--do_train=True \
--train_file=$SQUAD_DIR/train-v2.0.json \
--do_predict=True \
--predict_file=$SQUAD_DIR/dev-v2.0.json \
--train_batch_size=24 \
--learning_rate=3e-5 \
--num_train_epochs=2.0 \
--max_seq_length=384 \
--doc_stride=128 \
--output_dir=gs://some_bucket/squad_large/ \
--use_tpu=True \
--tpu_name=$TPU_NAME \
--version_2_with_negative=True
```  
We assume you have copied everything from the output directory to a local
directory called ./squad/. The initial dev set predictions will be at
./squad/predictions.json and the differences between the score of no answer ("")
and the best non-null answer for each question will be in the file
./squad/null_odds.json  
Run this script to tune a threshold for predicting null versus non-null answers:  
python $SQUAD_DIR/evaluate-v2.0.py $SQUAD_DIR/dev-v2.0.json
./squad/predictions.json --na-prob-file ./squad/null_odds.json  
Assume the script outputs "best_f1_thresh" THRESH. (Typical values are between
-1.0 and -5.0). You can now re-run the model to generate predictions with the
derived threshold or alternatively you can extract the appropriate answers from
./squad/nbest_predictions.json.  
```shell
python run_squad.py \
--vocab_file=$BERT_LARGE_DIR/vocab.txt \
--bert_config_file=$BERT_LARGE_DIR/bert_config.json \
--init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
--do_train=False \
--train_file=$SQUAD_DIR/train-v2.0.json \
--do_predict=True \
--predict_file=$SQUAD_DIR/dev-v2.0.json \
--train_batch_size=24 \
--learning_rate=3e-5 \
--num_train_epochs=2.0 \
--max_seq_length=384 \
--doc_stride=128 \
--output_dir=gs://some_bucket/squad_large/ \
--use_tpu=True \
--tpu_name=$TPU_NAME \
--version_2_with_negative=True \
--null_score_diff_threshold=$THRESH
```