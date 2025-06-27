Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
```bash
# Interpret the title as "Artist - Title"
$ yt-dlp --parse-metadata "title:%(artist)s - %(title)s"

# Regex example
$ yt-dlp --parse-metadata "description:Artist - (?P<artist>.+)"

# Set title as "Series name S01E05"
$ yt-dlp --parse-metadata "%(series)s S%(season_number)02dE%(episode_number)02d:%(title)s"

# Prioritize uploader as the "artist" field in video metadata
$ yt-dlp --parse-metadata "%(uploader|)s:%(meta_artist)s" --embed-metadata

# Set "comment" field in video metadata using description instead of webpage_url,
# handling multiple lines correctly
$ yt-dlp --parse-metadata "description:(?s)(?P<meta_comment>.+)" --embed-metadata

# Do not set any "synopsis" in the video metadata
$ yt-dlp --parse-metadata ":(?P<meta_synopsis>)"

# Remove "formats" field from the infojson by setting it to an empty string
$ yt-dlp --parse-metadata "video::(?P<formats>)" --write-info-json

# Replace all spaces and "_" in title and uploader with a `-`
$ yt-dlp --replace-in-metadata "title,uploader" "[ _]" "-"

```