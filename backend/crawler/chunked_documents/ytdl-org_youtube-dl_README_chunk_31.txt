Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Most people asking this question are not aware that youtube-dl now defaults to downloading the highest available quality as reported by YouTube, which will be 1080p or 720p in some cases, so you no longer need the `-b` option. For some specific videos, maybe YouTube does not report them to be available in a specific high quality format you're interested in. In that case, simply request it with the `-f` option and youtube-dl will try to download it.