Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
In certain cases, rather than fine-tuning the entire pre-trained model
end-to-end, it can be beneficial to obtained *pre-trained contextual
embeddings*, which are fixed contextual representations of each input token
generated from the hidden layers of the pre-trained model. This should also
mitigate most of the out-of-memory issues.  
As an example, we include the script `extract_features.py` which can be used
like this:  
```shell
# Sentence A and Sentence B are separated by the ||| delimiter for sentence
# pair tasks like question answering and entailment.
# For single sentence inputs, put one sentence per line and DON'T use the
# delimiter.
echo 'Who was Jim Henson ? ||| Jim Henson was a puppeteer' > /tmp/input.txt

python extract_features.py \
--input_file=/tmp/input.txt \
--output_file=/tmp/output.jsonl \
--vocab_file=$BERT_BASE_DIR/vocab.txt \
--bert_config_file=$BERT_BASE_DIR/bert_config.json \
--init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
--layers=-1,-2,-3,-4 \
--max_seq_length=128 \
--batch_size=8
```  
This will create a JSON file (one line per line of input) containing the BERT
activations from each Transformer layer specified by `layers` (-1 is the final
hidden layer of the Transformer, etc.)  
Note that this script will produce very large output files (by default, around
15kb for every input token).  
If you need to maintain alignment between the original and tokenized words (for
projecting training labels), see the [Tokenization](#tokenization) section
below.  
**Note:** You may see a message like `Could not find trained model in model_dir:
/tmp/tmpuB5g5c, running initialization to predict.` This message is expected, it
just means that we are using the `init_from_checkpoint()` API rather than the
saved model API. If you don't specify a checkpoint or specify an invalid
checkpoint, this script will complain.