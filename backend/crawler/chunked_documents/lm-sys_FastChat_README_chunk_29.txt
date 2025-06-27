Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Vicuna is created by fine-tuning a Llama base model using approximately 125K user-shared conversations gathered from ShareGPT.com with public APIs. To ensure data quality, we convert the HTML back to markdown and filter out some inappropriate or low-quality samples. Additionally, we divide lengthy conversations into smaller segments that fit the model's maximum context length. For detailed instructions to clean the ShareGPT data, check out [here](docs/commands/data_cleaning.md).  
We will not release the ShareGPT dataset. If you would like to try the fine-tuning code, you can run it with some dummy conversations in [dummy_conversation.json](data/dummy_conversation.json). You can follow the same format and plug in your own data.