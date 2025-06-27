Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
While these options still work, their use is not recommended since there are other alternatives to achieve the same  
--force-generic-extractor        --ies generic,default
--exec-before-download CMD       --exec "before_dl:CMD"
--no-exec-before-download        --no-exec
--all-formats                    -f all
--all-subs                       --sub-langs all --write-subs
--print-json                     -j --no-simulate
--autonumber-size NUMBER         Use string formatting, e.g. %(autonumber)03d
--autonumber-start NUMBER        Use internal field formatting like %(autonumber+NUMBER)s
--id                             -o "%(id)s.%(ext)s"
--metadata-from-title FORMAT     --parse-metadata "%(title)s:FORMAT"
--hls-prefer-native              --downloader "m3u8:native"
--hls-prefer-ffmpeg              --downloader "m3u8:ffmpeg"
--list-formats-old               --compat-options list-formats (Alias: --no-list-formats-as-table)
--list-formats-as-table          --compat-options -list-formats [Default] (Alias: --no-list-formats-old)
--youtube-skip-dash-manifest     --extractor-args "youtube:skip=dash" (Alias: --no-youtube-include-dash-manifest)
--youtube-skip-hls-manifest      --extractor-args "youtube:skip=hls" (Alias: --no-youtube-include-hls-manifest)
--youtube-include-dash-manifest  Default (Alias: --no-youtube-skip-dash-manifest)
--youtube-include-hls-manifest   Default (Alias: --no-youtube-skip-hls-manifest)
--geo-bypass                     --xff "default"
--no-geo-bypass                  --xff "never"
--geo-bypass-country CODE        --xff CODE
--geo-bypass-ip-block IP_BLOCK   --xff IP_BLOCK