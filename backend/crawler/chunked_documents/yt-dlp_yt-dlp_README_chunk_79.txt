Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
```python
import yt_dlp

INFO_FILE = 'path/to/video.info.json'

with yt_dlp.YoutubeDL() as ydl:
error_code = ydl.download_with_info_file(INFO_FILE)

print('Some videos failed to download' if error_code
else 'All videos successfully downloaded')
```