Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
youtube-dl works fine on its own on most sites. However, if you want to convert video/audio, you'll need [avconv](https://libav.org/) or [ffmpeg](https://www.ffmpeg.org/). On some sites - most notably YouTube - videos can be retrieved in a higher quality format without sound. youtube-dl will detect whether avconv/ffmpeg is present and automatically pick the best option.  
Videos or video formats streamed via RTMP protocol can only be downloaded when [rtmpdump](https://rtmpdump.mplayerhq.hu/) is installed. Downloading MMS and RTSP videos requires either [mplayer](https://mplayerhq.hu/) or [mpv](https://mpv.io/) to be installed.