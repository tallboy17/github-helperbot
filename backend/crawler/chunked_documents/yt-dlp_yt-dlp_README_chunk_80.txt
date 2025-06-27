Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
```python
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

ydl_opts = {
'format': 'm4a/bestaudio/best',
# ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
'postprocessors': [{  # Extract audio using ffmpeg
'key': 'FFmpegExtractAudio',
'preferredcodec': 'm4a',
}]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
error_code = ydl.download(URLS)
```