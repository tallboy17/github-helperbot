Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Say you need to extract `title` from the following HTML code:  
```html
<span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title">some fancy title</span>
```  
The code for that task should look similar to:  
```python
title = self._search_regex(
r'<span[^>]+class="title"[^>]*>([^<]+)', webpage, 'title')
```  
Or even better:  
```python
title = self._search_regex(
r'<span[^>]+class=(["\'])title\1[^>]*>(?P<title>[^<]+)',
webpage, 'title', group='title')
```  
Note how you tolerate potential changes in the `style` attribute's value or switch from using double quotes to single for `class` attribute:  
The code definitely should not look like:  
```python
title = self._search_regex(
r'<span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title">(.*?)</span>',
webpage, 'title', group='title')
```