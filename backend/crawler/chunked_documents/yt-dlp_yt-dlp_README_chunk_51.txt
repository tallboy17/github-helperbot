Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* `skip`: One or more of `webpage` (skip initial webpage download), `authcheck` (allow the download of playlists requiring authentication when no initial webpage is downloaded. This may cause unwanted behavior, see [#1122](https://github.com/yt-dlp/yt-dlp/pull/1122) for more details)
* `approximate_date`: Extract approximate `upload_date` and `timestamp` in flat-playlist. This may cause date-based filters to be slightly off