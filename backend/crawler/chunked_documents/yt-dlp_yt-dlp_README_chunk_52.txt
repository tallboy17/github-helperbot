Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* `fragment_query`: Passthrough any query in mpd/m3u8 manifest URLs to their fragments if no value is provided, or else apply the query string given as `fragment_query=VALUE`. Note that if the stream has an HLS AES-128 key, then the query parameters will be passed to the key URI as well, unless the `key_query` extractor-arg is passed, or unless an external key URI is provided via the `hls_key` extractor-arg. Does not apply to ffmpeg
* `variant_query`: Passthrough the master m3u8 URL query to its variant playlist URLs if no value is provided, or else apply the query string given as `variant_query=VALUE`
* `key_query`: Passthrough the master m3u8 URL query to its HLS AES-128 decryption key URI if no value is provided, or else apply the query string given as `key_query=VALUE`. Note that this will have no effect if the key URI is provided via the `hls_key` extractor-arg. Does not apply to ffmpeg
* `hls_key`: An HLS AES-128 key URI *or* key (as hex), and optionally the IV (as hex), in the form of `(URI|KEY)[,IV]`; e.g. `generic:hls_key=ABCDEF1234567980,0xFEDCBA0987654321`. Passing any of these values will force usage of the native HLS downloader and override the corresponding values found in the m3u8 playlist
* `is_live`: Bypass live HLS detection and manually set `live_status` - a value of `false` will set `not_live`, any other value (or no value) will set `is_live`
* `impersonate`: Target(s) to try and impersonate with the initial webpage request; e.g. `generic:impersonate=safari,chrome-110`. Use `generic:impersonate` to impersonate any available target, and use `generic:impersonate=false` to disable impersonation (default)