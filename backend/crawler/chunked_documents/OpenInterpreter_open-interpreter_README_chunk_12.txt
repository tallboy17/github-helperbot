Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
For more precise control, you can pass messages directly to `.chat(message)`:  
```python
interpreter.chat("Add subtitles to all videos in /videos.")

# ... Streams output to your terminal, completes task ...

interpreter.chat("These look great but can you make the subtitles bigger?")

# ...
```