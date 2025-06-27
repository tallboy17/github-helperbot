Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
In this example, various optional metadata values are extracted from the `.result.video[0]` member of the parsed JSON `response`, which is expected to be a JS object, parsed into a `dict`, with no crash if that isn't so, or if any of the target values are missing or invalid.  
```python
video = traverse_obj(response, ('result', 'video', 0, T(dict))) or {}
# formerly:
# video = try_get(response, lambda x: x['result']['video'][0], dict) or {}
description = video.get('summary')
duration = float_or_none(video.get('durationMs'), scale=1000)
view_count = int_or_none(video.get('views'))
```