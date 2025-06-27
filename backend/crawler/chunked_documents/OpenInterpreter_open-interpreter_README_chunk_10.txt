Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
**Update:** The Generator Update (0.1.5) introduced streaming:  
```python
message = "What operating system are we on?"

for chunk in interpreter.chat(message, display=False, stream=True):
print(chunk)
```