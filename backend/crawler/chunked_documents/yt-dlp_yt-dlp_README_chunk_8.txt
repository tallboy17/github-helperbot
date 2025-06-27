Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* [**ffmpeg** and **ffprobe**](https://www.ffmpeg.org) - Required for [merging separate video and audio files](#format-selection), as well as for various [post-processing](#post-processing-options) tasks. License [depends on the build](https://www.ffmpeg.org/legal.html)  
There are bugs in ffmpeg that cause various issues when used alongside yt-dlp. Since ffmpeg is such an important dependency, we provide [custom builds](https://github.com/yt-dlp/FFmpeg-Builds#ffmpeg-static-auto-builds) with patches for some of these issues at [yt-dlp/FFmpeg-Builds](https://github.com/yt-dlp/FFmpeg-Builds). See [the readme](https://github.com/yt-dlp/FFmpeg-Builds#patches-applied) for details on the specific issues solved by these builds  
**Important**: What you need is ffmpeg *binary*, **NOT** [the Python package of the same name](https://pypi.org/project/ffmpeg)