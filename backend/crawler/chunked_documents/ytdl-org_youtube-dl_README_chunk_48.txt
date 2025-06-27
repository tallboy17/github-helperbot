Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
You will first need to tell youtube-dl to stream media to stdout with `-o -`, and also tell your media player to read from stdin (it must be capable of this for streaming) and then pipe former to latter. For example, streaming to [vlc](https://www.videolan.org/) can be achieved with:  
youtube-dl -o - "https://www.youtube.com/watch?v=BaW_jenozKcj" | vlc -