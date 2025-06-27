Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
Most of the examples below assumes that you will be running training/evaluation
on your local machine, using a GPU like a Titan X or GTX 1080.  
However, if you have access to a Cloud TPU that you want to train on, just add
the following flags to `run_classifier.py` or `run_squad.py`:  
```
--use_tpu=True \
--tpu_name=$TPU_NAME
```  
Please see the
[Google Cloud TPU tutorial](https://cloud.google.com/tpu/docs/tutorials/mnist)
for how to use Cloud TPUs. Alternatively, you can use the Google Colab notebook
"[BERT FineTuning with Cloud TPUs](https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb)".  
On Cloud TPUs, the pretrained model and the output directory will need to be on
Google Cloud Storage. For example, if you have a bucket named `some_bucket`, you
might use the following flags instead:  
```
--output_dir=gs://some_bucket/my_output_dir/
```  
The unzipped pre-trained model files can also be found in the Google Cloud
Storage folder `gs://bert_models/2018_10_18`. For example:  
```
export BERT_BASE_DIR=gs://bert_models/2018_10_18/uncased_L-12_H-768_A-12
```