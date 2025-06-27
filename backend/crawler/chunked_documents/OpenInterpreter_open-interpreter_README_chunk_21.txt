Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
In the interactive mode, you can use the below commands to enhance your experience. Here's a list of available commands:  
**Available Commands:**  
- `%verbose [true/false]`: Toggle verbose mode. Without arguments or with `true` it
enters verbose mode. With `false` it exits verbose mode.
- `%reset`: Resets the current session's conversation.
- `%undo`: Removes the previous user message and the AI's response from the message history.
- `%tokens [prompt]`: (_Experimental_) Calculate the tokens that will be sent with the next prompt as context and estimate their cost. Optionally calculate the tokens and estimated cost of a `prompt` if one is provided. Relies on [LiteLLM's `cost_per_token()` method](https://docs.litellm.ai/docs/completion/token_usage#2-cost_per_token) for estimated costs.
- `%help`: Show the help message.