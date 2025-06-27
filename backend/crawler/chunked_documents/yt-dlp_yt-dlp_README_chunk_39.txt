Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* Environment variables are normally specified as `${VARIABLE}`/`$VARIABLE` on UNIX and `%VARIABLE%` on Windows; but is always shown as `${VARIABLE}` in this documentation
* yt-dlp also allows using UNIX-style variables on Windows for path-like options; e.g. `--output`, `--config-location`
* If unset, `${XDG_CONFIG_HOME}` defaults to `~/.config` and `${XDG_CACHE_HOME}` to `~/.cache`
* On Windows, `~` points to `${HOME}` if present; or, `${USERPROFILE}` or `${HOMEDRIVE}${HOMEPATH}` otherwise
* On Windows, `${USERPROFILE}` generally points to `C:\Users\<user name>` and `${APPDATA}` to `${USERPROFILE}\AppData\Roaming`