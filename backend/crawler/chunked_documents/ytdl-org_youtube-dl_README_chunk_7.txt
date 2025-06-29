Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
--playlist-start NUMBER              Playlist video to start at (default is
1)
--playlist-end NUMBER                Playlist video to end at (default is
last)
--playlist-items ITEM_SPEC           Playlist video items to download.
Specify indices of the videos in the
playlist separated by commas like: "--
playlist-items 1,2,5,8" if you want to
download videos indexed 1, 2, 5, 8 in
the playlist. You can specify range: "
--playlist-items 1-3,7,10-13", it will
download the videos at index 1, 2, 3,
7, 10, 11, 12 and 13.
--match-title REGEX                  Download only matching titles (regex or
caseless sub-string)
--reject-title REGEX                 Skip download for matching titles
(regex or caseless sub-string)
--max-downloads NUMBER               Abort after downloading NUMBER files
--min-filesize SIZE                  Do not download any videos smaller than
SIZE (e.g. 50k or 44.6m)
--max-filesize SIZE                  Do not download any videos larger than
SIZE (e.g. 50k or 44.6m)
--date DATE                          Download only videos uploaded in this
date
--datebefore DATE                    Download only videos uploaded on or
before this date (i.e. inclusive)
--dateafter DATE                     Download only videos uploaded on or
after this date (i.e. inclusive)
--min-views COUNT                    Do not download any videos with less
than COUNT views
--max-views COUNT                    Do not download any videos with more
than COUNT views
--match-filter FILTER                Generic video filter. Specify any key
(see the "OUTPUT TEMPLATE" for a list
of available keys) to match if the key
is present, !key to check if the key is
not present, key > NUMBER (like
"comment_count > 12", also works with
>=, <, <=, !=, =) to compare against a
number, key = 'LITERAL' (like "uploader
= 'Mike Smith'", also works with !=) to
match against a string literal and & to
require multiple matches. Values which
are not known are excluded unless you
put a question mark (?) after the
operator. For example, to only match
videos that have been liked more than
100 times and disliked less than 50
times (or the dislike functionality is
not available at the given service),
but who also have a description, use
--match-filter "like_count > 100 &
dislike_count <? 50 & description" .
--no-playlist                        Download only the video, if the URL
refers to a video and a playlist.
--yes-playlist                       Download the playlist, if the URL
refers to a video and a playlist.
--age-limit YEARS                    Download only videos suitable for the
given age
--download-archive FILE              Download only videos not listed in the
archive file. Record the IDs of all
downloaded videos in it.
--include-ads                        Download advertisements as well
(experimental)