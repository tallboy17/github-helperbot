Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
There is a soft limit to keep lines of code under 80 characters long. This means it should be respected if possible and if it does not make readability and code maintenance worse.  
For example, you should **never** split long string literals like URLs or some other often copied entities over multiple lines to fit this limit:  
Correct:  
```python
'https://www.youtube.com/watch?v=FqZTN594JQw&list=PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'
```  
Incorrect:  
```python
'https://www.youtube.com/watch?v=FqZTN594JQw&list='
'PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'
```