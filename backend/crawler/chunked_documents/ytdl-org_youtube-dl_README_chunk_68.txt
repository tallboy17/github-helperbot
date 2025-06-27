Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Correct:  
```python
title = self._html_search_regex(r'<title>([^<]+)</title>', webpage, 'title')
```  
Incorrect:  
```python
TITLE_RE = r'<title>([^<]+)</title>'
# ...some lines of code...
title = self._html_search_regex(TITLE_RE, webpage, 'title')
```