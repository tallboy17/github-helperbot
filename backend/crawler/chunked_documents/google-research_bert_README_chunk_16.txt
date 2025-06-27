Repository: google-research/bert
Language: Python
Stars: 39243
Forks: 9676
-----
*   **If using your own vocabulary, make sure to change `vocab_size` in
`bert_config.json`. If you use a larger vocabulary without changing this,
you will likely get NaNs when training on GPU or TPU due to unchecked
out-of-bounds access.**
*   If your task has a large domain-specific corpus available (e.g., "movie
reviews" or "scientific papers"), it will likely be beneficial to run
additional steps of pre-training on your corpus, starting from the BERT
checkpoint.
*   The learning rate we used in the paper was 1e-4. However, if you are doing
additional steps of pre-training starting from an existing BERT checkpoint,
you should use a smaller learning rate (e.g., 2e-5).
*   Current BERT models are English-only, but we do plan to release a
multilingual model which has been pre-trained on a lot of languages in the
near future (hopefully by the end of November 2018).
*   Longer sequences are disproportionately expensive because attention is
quadratic to the sequence length. In other words, a batch of 64 sequences of
length 512 is much more expensive than a batch of 256 sequences of
length 128. The fully-connected/convolutional cost is the same, but the
attention cost is far greater for the 512-length sequences. Therefore, one
good recipe is to pre-train for, say, 90,000 steps with a sequence length of
128 and then for 10,000 additional steps with a sequence length of 512. The
very long sequences are mostly needed to learn positional embeddings, which
can be learned fairly quickly. Note that this does require generating the
data twice with different values of `max_seq_length`.
*   If you are pre-training from scratch, be prepared that pre-training is
computationally expensive, especially on GPUs. If you are pre-training from
scratch, our recommended recipe is to pre-train a `BERT-Base` on a single
[preemptible Cloud TPU v2](https://cloud.google.com/tpu/docs/pricing), which
takes about 2 weeks at a cost of about $500 USD (based on the pricing in
October 2018). You will have to scale down the batch size when only training
on a single Cloud TPU, compared to what was used in the paper. It is
recommended to use the largest batch size that fits into TPU memory.