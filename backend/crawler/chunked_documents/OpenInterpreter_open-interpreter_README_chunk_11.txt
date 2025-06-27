Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
To start an interactive chat in your terminal, either run `interpreter` from the command line:  
```shell
interpreter
```  
Or `interpreter.chat()` from a .py file:  
```python
interpreter.chat()
```  
**You can also stream each chunk:**  
```python
message = "What operating system are we on?"

for chunk in interpreter.chat(message, display=False, stream=True):
print(chunk)
```