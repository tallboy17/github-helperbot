Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Good:  
```python
description = self._html_search_meta(
['og:description', 'description', 'twitter:description'],
webpage, 'description', default=None)
```  
Unwieldy:  
```python
description = (
self._og_search_description(webpage, default=None)
or self._html_search_meta('description', webpage, default=None)
or self._html_search_meta('twitter:description', webpage, default=None))
```  
Methods supporting list of patterns are: `_search_regex`, `_html_search_regex`, `_og_search_property`, `_html_search_meta`.