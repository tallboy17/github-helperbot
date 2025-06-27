Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Say you have some source dictionary `meta` that you've fetched as JSON with HTTP request and it has a key `summary`:  
```python
meta = self._download_json(url, video_id)
```  
Assume at this point `meta`'s layout is:  
```python
{
...
"summary": "some fancy summary text",
...
}
```  
Assume you want to extract `summary` and put it into the resulting info dict as `description`. Since `description` is an optional meta field you should be ready that this key may be missing from the `meta` dict, so that you should extract it like:  
```python
description = meta.get('summary')  # correct
```  
and not like:  
```python
description = meta['summary']  # incorrect
```  
The latter will break extraction process with `KeyError` if `summary` disappears from `meta` at some later time but with the former approach extraction will just go ahead with `description` set to `None` which is perfectly fine (remember `None` is equivalent to the absence of data).  
Similarly, you should pass `fatal=False` when extracting optional data from a webpage with `_search_regex`, `_html_search_regex` or similar methods, for instance:  
```python
description = self._search_regex(
r'<span[^>]+id="title"[^>]*>([^<]+)<',
webpage, 'description', fatal=False)
```  
With `fatal` set to `False` if `_search_regex` fails to extract `description` it will emit a warning and continue extraction.  
You can also pass `default=<some fallback value>`, for example:  
```python
description = self._search_regex(
r'<span[^>]+id="title"[^>]*>([^<]+)<',
webpage, 'description', default=None)
```  
On failure this code will silently continue the extraction with `description` set to `None`. That is useful for metafields that may or may not be present.