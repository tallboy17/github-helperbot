Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
Our Python package gives you more control over each setting. To replicate and connect to LM Studio, use these settings:  
```python
from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "http://localhost:1234/v1" # Point this at any OpenAI compatible server

interpreter.chat()
```