Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
If you put youtube-dl and ffmpeg in the same directory that you're running the command from, it will work, but that's rather cumbersome.  
To make a different directory work - either for ffmpeg, or for youtube-dl, or for both - simply create the directory (say, `C:\bin`, or `C:\Users\<User name>\bin`), put all the executables directly in there, and then [set your PATH environment variable](https://www.java.com/en/download/help/path.xml) to include that directory.  
From then on, after restarting your shell, you will be able to access both youtube-dl and ffmpeg (and youtube-dl will be able to find ffmpeg) by simply typing `youtube-dl` or `ffmpeg`, no matter what directory you're in.