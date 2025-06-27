Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
The following provide support for impersonating browser requests. This may be required for some sites that employ TLS fingerprinting.  
* [**curl_cffi**](https://github.com/lexiforest/curl_cffi) (recommended) - Python binding for [curl-impersonate](https://github.com/lexiforest/curl-impersonate). Provides impersonation targets for Chrome, Edge and Safari. Licensed under [MIT](https://github.com/lexiforest/curl_cffi/blob/main/LICENSE)
* Can be installed with the `curl-cffi` group, e.g. `pip install "yt-dlp[default,curl-cffi]"`
* Currently included in `yt-dlp.exe`, `yt-dlp_linux` and `yt-dlp_macos` builds