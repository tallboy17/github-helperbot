Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Correct:  
```python
lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
list)
```  
Incorrect:  
```python
lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
list,
)
```