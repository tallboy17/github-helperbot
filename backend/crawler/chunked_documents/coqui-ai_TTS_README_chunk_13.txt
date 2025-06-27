Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
🐸TTS is tested on Ubuntu 18.04 with **python >= 3.9, < 3.12.**.  
If you are only interested in [synthesizing speech](https://tts.readthedocs.io/en/latest/inference.html) with the released 🐸TTS models, installing from PyPI is the easiest option.  
```bash
pip install TTS
```  
If you plan to code or train models, clone 🐸TTS and install it locally.  
```bash
git clone https://github.com/coqui-ai/TTS
pip install -e .[all,dev,notebooks]  # Select the relevant extras
```  
If you are on Ubuntu (Debian), you can also run following commands for installation.  
```bash
$ make system-deps  # intended to be used on Ubuntu (Debian). Let us know if you have a different OS.
$ make install
```  
If you are on Windows, 👑@GuyPaddock wrote installation instructions [here](https://stackoverflow.com/questions/66726331/how-can-i-run-mozilla-tts-coqui-tts-training-with-cuda-on-a-windows-system).