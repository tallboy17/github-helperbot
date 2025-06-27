Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
`interpreter.chat()` returns a List of messages, which can be used to resume a conversation with `interpreter.messages = messages`:  
```python
messages = interpreter.chat("My name is Killian.") # Save messages to 'messages'
interpreter.messages = [] # Reset interpreter ("Killian" will be forgotten)

interpreter.messages = messages # Resume chat from 'messages' ("Killian" will be remembered)
```