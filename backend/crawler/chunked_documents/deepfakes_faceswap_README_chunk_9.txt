Repository: deepfakes/faceswap
Language: Python
Stars: 54142
Forks: 13417
-----
- All of the scripts mentioned have `-h`/`--help` options with arguments that they will accept. You're smart, you can figure out how this works, right?!  
NB: there is a conversion tool for video. This can be accessed by running `python tools.py effmpeg -h`. Alternatively, you can use [ffmpeg](https://www.ffmpeg.org) to convert video into photos, process images, and convert images back to the video.  
**Some tips:**  
Reusing existing models will train much faster than starting from nothing.
If there is not enough training data, start with someone who looks similar, then switch the data.