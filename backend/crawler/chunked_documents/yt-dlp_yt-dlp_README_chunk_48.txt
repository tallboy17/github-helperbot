Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
Some extractors accept additional arguments which can be passed using `--extractor-args KEY:ARGS`. `ARGS` is a `;` (semicolon) separated string of `ARG=VAL1,VAL2`. E.g. `--extractor-args "youtube:player-client=tv,mweb;formats=incomplete" --extractor-args "twitter:api=syndication"`  
Note: In CLI, `ARG` can use `-` instead of `_`; e.g. `youtube:player-client"` becomes `youtube:player_client"`  
The following extractors use this feature: