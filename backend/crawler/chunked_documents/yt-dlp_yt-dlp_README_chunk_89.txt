Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
While these options are redundant, they are still expected to be used due to their ease of use  
--get-description                --print description
--get-duration                   --print duration_string
--get-filename                   --print filename
--get-format                     --print format
--get-id                         --print id
--get-thumbnail                  --print thumbnail
-e, --get-title                  --print title
-g, --get-url                    --print urls
--match-title REGEX              --match-filters "title ~= (?i)REGEX"
--reject-title REGEX             --match-filters "title !~= (?i)REGEX"
--min-views COUNT                --match-filters "view_count >=? COUNT"
--max-views COUNT                --match-filters "view_count <=? COUNT"
--break-on-reject                Use --break-match-filters
--user-agent UA                  --add-headers "User-Agent:UA"
--referer URL                    --add-headers "Referer:URL"
--playlist-start NUMBER          -I NUMBER:
--playlist-end NUMBER            -I :NUMBER
--playlist-reverse               -I ::-1
--no-playlist-reverse            Default
--no-colors                      --color no_color