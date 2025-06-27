Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
OpenAI's release of [Code Interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter) with GPT-4 presents a fantastic opportunity to accomplish real-world tasks with ChatGPT.  
However, OpenAI's service is hosted, closed-source, and heavily restricted:  
- No internet access.
- [Limited set of pre-installed packages](https://wfhbrian.com/mastering-chatgpts-code-interpreter-list-of-python-packages/).
- 100 MB maximum upload, 120.0 second runtime limit.
- State is cleared (along with any generated files or links) when the environment dies.  
---  
Open Interpreter overcomes these limitations by running in your local environment. It has full access to the internet, isn't restricted by time or file size, and can utilize any package or library.  
This combines the power of GPT-4's Code Interpreter with the flexibility of your local development environment.