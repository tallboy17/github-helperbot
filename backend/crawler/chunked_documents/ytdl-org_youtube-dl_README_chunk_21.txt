Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
If you are using an output template inside a Windows batch file then you must escape plain percent characters (`%`) by doubling, so that `-o "%(title)s-%(id)s.%(ext)s"` should become `-o "%%(title)s-%%(id)s.%%(ext)s"`. However you should not touch `%`'s that are not plain characters, e.g. environment variables for expansion should stay intact: `-o "C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s"`.