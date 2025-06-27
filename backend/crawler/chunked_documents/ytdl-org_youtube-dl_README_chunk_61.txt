Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Say `meta` from the previous example has a `title` and you are about to extract it. Since `title` is a mandatory meta field you should end up with something like:  
```python
title = meta['title']
```  
If `title` disappears from `meta` in future due to some changes on the hoster's side the extraction would fail since `title` is mandatory. That's expected.  
Assume that you have some another source you can extract `title` from, for example `og:title` HTML meta of a `webpage`. In this case you can provide a fallback scenario:  
```python
title = meta.get('title') or self._og_search_title(webpage)
```  
This code will try to extract from `meta` first and if it fails it will try extracting `og:title` from a `webpage`.