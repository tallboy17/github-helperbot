Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Don't capture id attribute name here since you can't use it for anything anyway.  
Correct:  
```python
r'(?:id|ID)=(?P<id>\d+)'
```  
Incorrect:
```python
r'(id|ID)=(?P<id>\d+)'
```