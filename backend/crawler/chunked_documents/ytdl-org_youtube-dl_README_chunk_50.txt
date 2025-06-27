Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
When youtube-dl detects an HLS video, it can download it either with the built-in downloader or ffmpeg. Since many HLS streams are slightly invalid and ffmpeg/youtube-dl each handle some invalid cases better than the other, there is an option to switch the downloader if needed.  
When youtube-dl knows that one particular downloader works better for a given website, that downloader will be picked. Otherwise, youtube-dl will pick the best downloader for general compatibility, which at the moment happens to be ffmpeg. This choice may change in future versions of youtube-dl, with improvements of the built-in downloader and/or ffmpeg.  
In particular, the generic extractor (used when your website is not in the [list of supported sites by youtube-dl](https://ytdl-org.github.io/youtube-dl/supportedsites.html) cannot mandate one specific downloader.  
If you put either `--hls-prefer-native` or `--hls-prefer-ffmpeg` into your configuration, a different subset of videos will fail to download correctly. Instead, it is much better to [file an issue](https://yt-dl.org/bug) or a pull request which details why the native or the ffmpeg HLS downloader is a better choice for your use case.