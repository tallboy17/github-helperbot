Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
For extraction to work youtube-dl relies on metadata your extractor extracts and provides to youtube-dl expressed by an [information dictionary](https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303) or simply *info dict*. Only the following meta fields in the *info dict* are considered mandatory for a successful extraction process by youtube-dl:  
- `id` (media identifier)
- `title` (media title)
- `url` (media download URL) or `formats`  
In fact only the last option is technically mandatory (i.e. if you can't figure out the download location of the media the extraction does not make any sense). But by convention youtube-dl also treats `id` and `title` as mandatory. Thus the aforementioned metafields are the critical data that the extraction does not make any sense without and if any of them fail to be extracted then the extractor is considered completely broken.  
[Any field](https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L188-L303) apart from the aforementioned ones are considered **optional**. That means that extraction should be **tolerant** to situations when sources for these fields can potentially be unavailable (even if they are always available at the moment) and **future-proof** in order not to break the extraction of general purpose mandatory fields.