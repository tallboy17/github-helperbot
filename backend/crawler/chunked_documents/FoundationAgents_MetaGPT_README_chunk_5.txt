Repository: FoundationAgents/MetaGPT
Language: Python
Stars: 56527
Forks: 6778
-----
You can init the config of MetaGPT by running the following command, or manually create `~/.metagpt/config2.yaml` file:
```bash
# Check https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html for more details
metagpt --init-config  # it will create ~/.metagpt/config2.yaml, just modify it to your needs
```  
You can configure `~/.metagpt/config2.yaml` according to the [example](https://github.com/geekan/MetaGPT/blob/main/config/config2.example.yaml) and [doc](https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html):  
```yaml
llm:
api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options
model: "gpt-4-turbo"  # or gpt-3.5-turbo
base_url: "https://api.openai.com/v1"  # or forward url / other llm url
api_key: "YOUR_API_KEY"
```