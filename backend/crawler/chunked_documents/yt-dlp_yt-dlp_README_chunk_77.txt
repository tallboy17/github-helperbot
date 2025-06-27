Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
yt-dlp makes the best effort to be a good command-line program, and thus should be callable from any programming language.  
Your program should avoid parsing the normal stdout since they may change in future versions. Instead, they should use options such as `-J`, `--print`, `--progress-template`, `--exec` etc to create console output that you can reliably reproduce and parse.  
From a Python program, you can embed yt-dlp in a more powerful fashion, like this:  
```python
from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
with YoutubeDL() as ydl:
ydl.download(URLS)
```  
Most likely, you'll want to use various options. For a list of options available, have a look at [`yt_dlp/YoutubeDL.py`](yt_dlp/YoutubeDL.py#L183) or `help(yt_dlp.YoutubeDL)` in a Python shell. If you are already familiar with the CLI, you can use [`devscripts/cli_to_api.py`](https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/cli_to_api.py) to translate any CLI switches to `YoutubeDL` params.  
**Tip**: If you are porting your code from youtube-dl to yt-dlp, one important point to look out for is that we do not guarantee the return value of `YoutubeDL.extract_info` to be json serializable, or even be a dictionary. It will be dictionary-like, but if you want to ensure it is a serializable dictionary, pass it through `YoutubeDL.sanitize_info` as shown in the [example below](#extracting-information)