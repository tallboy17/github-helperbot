Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
To build the standalone executable, you must have Python and `pyinstaller` (plus any of yt-dlp's [optional dependencies](#dependencies) if needed). The executable will be built for the same CPU architecture as the Python used.  
You can run the following commands:  
```
python3 devscripts/install_deps.py --include pyinstaller
python3 devscripts/make_lazy_extractors.py
python3 -m bundle.pyinstaller
```  
On some systems, you may need to use `py` or `python` instead of `python3`.  
`python -m bundle.pyinstaller` accepts any arguments that can be passed to `pyinstaller`, such as `--onefile/-F` or `--onedir/-D`, which is further [documented here](https://pyinstaller.org/en/stable/usage.html#what-to-generate).  
**Note**: Pyinstaller versions below 4.4 [do not support](https://github.com/pyinstaller/pyinstaller#requirements-and-tested-platforms) Python installed from the Windows store without using a virtual environment.  
**Important**: Running `pyinstaller` directly **instead of** using `python -m bundle.pyinstaller` is **not** officially supported. This may or may not work correctly.