Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Suppose you've extracted JSON like this into a Python data structure named `media_json` using, say, the `_download_json()` or `_parse_json()` methods of `InfoExtractor`:
```json
{
"title": "Example video",
"comment": "try extracting this",
"media": [{
"type": "bad",
"size": 320,
"url": "https://some.cdn.site/bad.mp4"
}, {
"type": "streaming",
"url": "https://some.cdn.site/hls.m3u8"
}, {
"type": "super",
"size": 1280,
"url": "https://some.cdn.site/good.webm"
}],
"moreStuff": "more values",
...
}
```  
Then extractor code like this can collect the various fields of the JSON:
```python
...
from ..utils import (
determine_ext,
int_or_none,
T,
traverse_obj,
txt_or_none,
url_or_none,
)
...
...
info_dict = {}
# extract title and description if valid and not empty
info_dict.update(traverse_obj(media_json, {
'title': ('title', T(txt_or_none)),
'description': ('comment', T(txt_or_none)),
}))

# extract any recognisable media formats
fmts = []
# traverse into "media" list, extract `dict`s with desired keys
for fmt in traverse_obj(media_json, ('media', Ellipsis, {
'format_id': ('type', T(txt_or_none)),
'url': ('url', T(url_or_none)),
'width': ('size', T(int_or_none)), })):
# bad `fmt` values were `None` and removed
if 'url' not in fmt:
continue
fmt_url = fmt['url']  # known to be valid URL
ext = determine_ext(fmt_url)
if ext == 'm3u8':
fmts.extend(self._extract_m3u8_formats(fmt_url, video_id, 'mp4', fatal=False))
else:
fmt['ext'] = ext
fmts.append(fmt)

# sort, raise if no formats
self._sort_formats(fmts)

info_dict['formats'] = fmts
...
```
The extractor raises an exception rather than random crashes if the JSON structure changes so that no formats are found.