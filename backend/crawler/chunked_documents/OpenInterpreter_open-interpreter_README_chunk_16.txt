Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
Open Interpreter uses [LiteLLM](https://docs.litellm.ai/docs/providers/) to connect to hosted language models.  
You can change the model by setting the model parameter:  
```shell
interpreter --model gpt-3.5-turbo
interpreter --model claude-2
interpreter --model command-nightly
```  
In Python, set the model on the object:  
```python
interpreter.llm.model = "gpt-3.5-turbo"
```  
[Find the appropriate "model" string for your language model here.](https://docs.litellm.ai/docs/providers/)