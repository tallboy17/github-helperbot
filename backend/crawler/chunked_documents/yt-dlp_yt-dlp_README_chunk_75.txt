Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
Plugins can be installed using various methods and locations.  
1. **Configuration directories**:
Plugin packages (containing a `yt_dlp_plugins` namespace folder) can be dropped into the following standard [configuration locations](#configuration):
* **User Plugins**
* `${XDG_CONFIG_HOME}/yt-dlp/plugins/<package name>/yt_dlp_plugins/` (recommended on Linux/macOS)
* `${XDG_CONFIG_HOME}/yt-dlp-plugins/<package name>/yt_dlp_plugins/`
* `${APPDATA}/yt-dlp/plugins/<package name>/yt_dlp_plugins/` (recommended on Windows)
* `${APPDATA}/yt-dlp-plugins/<package name>/yt_dlp_plugins/`
* `~/.yt-dlp/plugins/<package name>/yt_dlp_plugins/`
* `~/yt-dlp-plugins/<package name>/yt_dlp_plugins/`
* **System Plugins**
* `/etc/yt-dlp/plugins/<package name>/yt_dlp_plugins/`
* `/etc/yt-dlp-plugins/<package name>/yt_dlp_plugins/`
2. **Executable location**: Plugin packages can similarly be installed in a `yt-dlp-plugins` directory under the executable location (recommended for portable installations):
* Binary: where `<root-dir>/yt-dlp.exe`, `<root-dir>/yt-dlp-plugins/<package name>/yt_dlp_plugins/`
* Source: where `<root-dir>/yt_dlp/__main__.py`, `<root-dir>/yt-dlp-plugins/<package name>/yt_dlp_plugins/`  
3. **pip and other locations in `PYTHONPATH`**
* Plugin packages can be installed and managed using `pip`. See [yt-dlp-sample-plugins](https://github.com/yt-dlp/yt-dlp-sample-plugins) for an example.
* Note: plugin files between plugin packages installed with pip must have unique filenames.
* Any path in `PYTHONPATH` is searched in for the `yt_dlp_plugins` namespace folder.
* Note: This does not apply for Pyinstaller builds.  
`.zip`, `.egg` and `.whl` archives containing a `yt_dlp_plugins` namespace folder in their root are also supported as plugin packages.  
* e.g. `${XDG_CONFIG_HOME}/yt-dlp/plugins/mypluginpkg.zip` where `mypluginpkg.zip` contains `yt_dlp_plugins/<type>/myplugin.py`  
Run yt-dlp with `--verbose` to check if the plugin has been loaded.