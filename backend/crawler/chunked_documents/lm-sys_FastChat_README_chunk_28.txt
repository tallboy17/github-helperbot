Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
We use MT-bench, a set of challenging multi-turn open-ended questions to evaluate models.
To automate the evaluation process, we prompt strong LLMs like GPT-4 to act as judges and assess the quality of the models' responses.
See instructions for running MT-bench at [fastchat/llm_judge](fastchat/llm_judge).  
MT-bench is the new recommended way to benchmark your models. If you are still looking for the old 80 questions used in the vicuna blog post, please go to [vicuna-blog-eval](https://github.com/lm-sys/vicuna-blog-eval).