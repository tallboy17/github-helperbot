Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* **`devscripts/install_deps.py`** - Install dependencies for yt-dlp.
* **`devscripts/update-version.py`** - Update the version number based on the current date.
* **`devscripts/set-variant.py`** - Set the build variant of the executable.
* **`devscripts/make_changelog.py`** - Create a markdown changelog using short commit messages and update `CONTRIBUTORS` file.
* **`devscripts/make_lazy_extractors.py`** - Create lazy extractors. Running this before building the binaries (any variant) will improve their startup performance. Set the environment variable `YTDLP_NO_LAZY_EXTRACTORS` to something nonempty to forcefully disable lazy extractor loading.  
Note: See their `--help` for more info.