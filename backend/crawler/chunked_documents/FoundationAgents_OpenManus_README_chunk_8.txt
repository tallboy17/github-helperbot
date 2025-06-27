Repository: FoundationAgents/OpenManus
Language: Python
Stars: 46956
Forks: 8199
-----
OpenManus requires configuration for the LLM APIs it uses. Follow these steps to set up your configuration:  
1. Create a `config.toml` file in the `config` directory (you can copy from the example):  
```bash
cp config/config.example.toml config/config.toml
```  
2. Edit `config/config.toml` to add your API keys and customize settings:  
```toml
# Global LLM configuration
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
max_tokens = 4096
temperature = 0.0

# Optional configuration for specific LLM models
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
```