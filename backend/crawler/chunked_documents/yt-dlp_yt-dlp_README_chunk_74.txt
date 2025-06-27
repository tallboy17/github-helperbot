Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
Note that **all** plugins are imported even if not invoked, and that **there are no checks** performed on plugin code. **Use plugins at your own risk and only if you trust the code!**  
Plugins can be of `<type>`s `extractor` or `postprocessor`.
- Extractor plugins do not need to be enabled from the CLI and are automatically invoked when the input URL is suitable for it.
- Extractor plugins take priority over built-in extractors.
- Postprocessor plugins can be invoked using `--use-postprocessor NAME`.  
Plugins are loaded from the namespace packages `yt_dlp_plugins.extractor` and `yt_dlp_plugins.postprocessor`.  
In other words, the file structure on the disk looks something like:  
yt_dlp_plugins/
extractor/
myplugin.py
postprocessor/
myplugin.py  
yt-dlp looks for these `yt_dlp_plugins` namespace folders in many locations (see below) and loads in plugins from **all** of them.
Set the environment variable `YTDLP_NO_PLUGINS` to something nonempty to disable loading plugins entirely.  
See the [wiki for some known plugins](https://github.com/yt-dlp/yt-dlp/wiki/Plugins)