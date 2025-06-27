Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
The configuration files are decoded according to the UTF BOM if present, and in the encoding from system locale otherwise.  
If you want your file to be decoded differently, add `# coding: ENCODING` to the beginning of the file (e.g. `# coding: shift-jis`). There must be no characters before that, even spaces or BOM.