Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* `formats`: Formats to request from the API. Requested values should be in the format of `{protocol}_{codec}`, e.g. `hls_opus,http_aac`. The `*` character functions as a wildcard, e.g. `*_mp3`, and can be passed by itself to request all formats. Known protocols include `http`, `hls` and `hls-aes`; known codecs include `aac`, `opus` and `mp3`. Original `download` formats are always extracted. Default is `http_aac,hls_aac,http_opus,hls_opus,http_mp3,hls_mp3`