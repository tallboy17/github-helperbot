Repository: hpcaitech/ColossalAI
Language: Python
Stars: 40976
Forks: 4521
-----
[[GPU Cloud Playground]](https://cloud.luchentech.com/)
[[LLaMA3 Image]](https://cloud.luchentech.com/doc/docs/image/llama)  
- 7B: One half-day of training using a few hundred dollars yields similar results to mainstream large models, open-source and commercial-free domain-specific LLM solution.
[[code]](https://github.com/hpcaitech/ColossalAI/tree/main/applications/Colossal-LLaMA-2)
[[blog]](https://www.hpc-ai.tech/blog/one-half-day-of-training-using-a-few-hundred-dollars-yields-similar-results-to-mainstream-large-models-open-source-and-commercial-free-domain-specific-llm-solution)
[[HuggingFace model weights]](https://huggingface.co/hpcai-tech/Colossal-LLaMA-2-7b-base)
[[Modelscope model weights]](https://www.modelscope.cn/models/colossalai/Colossal-LLaMA-2-7b-base/summary)  
- 13B: Construct refined 13B private model with just $5000 USD.
[[code]](https://github.com/hpcaitech/ColossalAI/tree/main/applications/Colossal-LLaMA-2)
[[blog]](https://hpc-ai.com/blog/colossal-llama-2-13b)
[[HuggingFace model weights]](https://huggingface.co/hpcai-tech/Colossal-LLaMA-2-13b-base)
[[Modelscope model weights]](https://www.modelscope.cn/models/colossalai/Colossal-LLaMA-2-13b-base/summary)  
|              Model              |  Backbone  | Tokens Consumed |     MMLU (5-shot)    | CMMLU (5-shot)| AGIEval (5-shot) | GAOKAO (0-shot) | CEval (5-shot)  |
| :-----------------------------: | :--------: | :-------------: | :------------------: | :-----------: | :--------------: | :-------------: | :-------------: |
|          Baichuan-7B            |     -      |      1.2T       |    42.32 (42.30)     | 44.53 (44.02) |        38.72     |       36.74     |       42.80     |
|       Baichuan-13B-Base         |     -      |      1.4T       |    50.51 (51.60)     | 55.73 (55.30) |        47.20     |       51.41     |       53.60     |
|       Baichuan2-7B-Base         |     -      |      2.6T       |    46.97 (54.16)     | 57.67 (57.07) |        45.76     |       52.60     |       54.00     |
|       Baichuan2-13B-Base        |     -      |      2.6T       |    54.84 (59.17)     | 62.62 (61.97) |        52.08     |       58.25     |       58.10     |
|           ChatGLM-6B            |     -      |      1.0T       |    39.67 (40.63)     |   41.17 (-)   |        40.10     |       36.53     |       38.90     |
|          ChatGLM2-6B            |     -      |      1.4T       |    44.74 (45.46)     |   49.40 (-)   |        46.36     |       45.49     |       51.70     |
|          InternLM-7B            |     -      |      1.6T       |    46.70 (51.00)     |   52.00 (-)   |        44.77     |       61.64     |       52.80     |
|            Qwen-7B              |     -      |      2.2T       |    54.29 (56.70)     | 56.03 (58.80) |        52.47     |       56.42     |       59.60     |
|           Llama-2-7B            |     -      |      2.0T       |    44.47 (45.30)     |   32.97 (-)   |        32.60     |       25.46     |         -       |
| Linly-AI/Chinese-LLaMA-2-7B-hf  | Llama-2-7B |      1.0T       |        37.43         |     29.92     |        32.00     |       27.57     |         -       |
| wenge-research/yayi-7b-llama2   | Llama-2-7B |        -        |        38.56         |     31.52     |        30.99     |       25.95     |         -       |
| ziqingyang/chinese-llama-2-7b   | Llama-2-7B |        -        |        33.86         |     34.69     |        34.52     |       25.18     |        34.2     |
| TigerResearch/tigerbot-7b-base  | Llama-2-7B |      0.3T       |        43.73         |     42.04     |        37.64     |       30.61     |         -       |
|  LinkSoul/Chinese-Llama-2-7b    | Llama-2-7B |        -        |        48.41         |     38.31     |        38.45     |       27.72     |         -       |
|       FlagAlpha/Atom-7B         | Llama-2-7B |      0.1T       |        49.96         |     41.10     |        39.83     |       33.00     |         -       |
| IDEA-CCNL/Ziya-LLaMA-13B-v1.1   | Llama-13B  |      0.11T      |        50.25         |     40.99     |        40.04     |       30.54     |         -       |
|  **Colossal-LLaMA-2-7b-base**   | Llama-2-7B |   **0.0085T**   |        53.06         |     49.89     |        51.48     |       58.82     |        50.2     |
|  **Colossal-LLaMA-2-13b-base**  | Llama-2-13B |   **0.025T**    |        56.42         |     61.80     |        54.69     |       69.53     |        60.3     |