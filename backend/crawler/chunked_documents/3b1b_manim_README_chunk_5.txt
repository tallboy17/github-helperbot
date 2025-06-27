Repository: 3b1b/manim
Language: Python
Stars: 78210
Forks: 6743
-----
1. Install FFmpeg, LaTeX in terminal using homebrew.
```sh
brew install ffmpeg mactex
```  
2. If you are using an ARM-based processor, install Cairo.
```sh
arch -arm64 brew install pkg-config cairo
```  
3. Install latest version of manim using these command.
```sh
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
manimgl example_scenes.py OpeningManimExample (make sure to add manimgl to path first.)
```