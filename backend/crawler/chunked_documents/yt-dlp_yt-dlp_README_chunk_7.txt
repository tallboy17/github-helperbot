Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
Python versions 3.9+ (CPython) and 3.10+ (PyPy) are supported. Other versions and implementations may or may not work correctly.  
<!-- Python 3.5+ uses VC++14 and it is already embedded in the binary created
<!x-- https://www.microsoft.com/en-us/download/details.aspx?id=26999 --x>
On Windows, [Microsoft Visual C++ 2010 SP1 Redistributable Package (x86)](https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe) is also necessary to run yt-dlp. You probably already have this, but if the executable throws an error due to missing `MSVCR100.dll` you need to install it manually.
-->  
While all the other dependencies are optional, `ffmpeg` and `ffprobe` are highly recommended