Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
Wrap all extracted numeric data into safe functions from [`youtube_dl/utils.py`](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py): `int_or_none`, `float_or_none`. Use them for string to number conversions as well.  
Use `url_or_none` for safe URL processing.  
Use `traverse_obj` for safe metadata extraction from parsed JSON.  
Use `unified_strdate` for uniform `upload_date` or any `YYYYMMDD` meta field extraction, `unified_timestamp` for uniform `timestamp` extraction, `parse_filesize` for `filesize` extraction, `parse_count` for count meta fields extraction, `parse_resolution`, `parse_duration` for `duration` extraction, `parse_age_limit` for `age_limit` extraction.  
Explore [`youtube_dl/utils.py`](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py) for more useful convenience functions.