Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* [**avconv** and **avprobe**](https://www.libav.org) - Now **deprecated** alternative to ffmpeg. License [depends on the build](https://libav.org/legal)
* [**sponskrub**](https://github.com/faissaloo/SponSkrub) - For using the now **deprecated** [sponskrub options](#sponskrub-options). Licensed under [GPLv3+](https://github.com/faissaloo/SponSkrub/blob/master/LICENCE.md)
* [**rtmpdump**](http://rtmpdump.mplayerhq.hu) - For downloading `rtmp` streams. ffmpeg can be used instead with `--downloader ffmpeg`. Licensed under [GPLv2+](http://rtmpdump.mplayerhq.hu)
* [**mplayer**](http://mplayerhq.hu/design7/info.html) or [**mpv**](https://mpv.io) - For downloading `rstp`/`mms` streams. ffmpeg can be used instead with `--downloader ffmpeg`. Licensed under [GPLv2+](https://github.com/mpv-player/mpv/blob/master/Copyright)  
To use or redistribute the dependencies, you must agree to their respective licensing terms.  
The standalone release binaries are built with the Python interpreter and the packages marked with **\*** included.  
If you do not have the necessary dependencies for a task you are attempting, yt-dlp will warn you. All the currently available dependencies are visible at the top of the `--verbose` output