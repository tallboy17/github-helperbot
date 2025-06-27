Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
Use the `--player`/`-p` option to feed the video into your media player of choice, e.g. `mpv` or `vlc`, instead of downloading it:  
```
$ you-get -p vlc 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
```  
Or, if you prefer to watch the video in a browser, just without ads or comment section:  
```
$ you-get -p chromium 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
```  
**Tips:**  
* It is possible to use the `-p` option to start another download manager, e.g., `you-get -p uget-gtk 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`, though they may not play together very well.