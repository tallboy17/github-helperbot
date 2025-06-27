Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
You can inspect and configure Open Interpreter's system message to extend its functionality, modify permissions, or give it more context.  
```python
interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
print(interpreter.system_message)
```