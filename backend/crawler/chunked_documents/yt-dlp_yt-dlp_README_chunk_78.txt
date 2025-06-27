Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
```python
import json
import yt_dlp

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
info = ydl.extract_info(URL, download=False)

# ℹ️ ydl.sanitize_info makes the info json-serializable
print(json.dumps(ydl.sanitize_info(info)))
```