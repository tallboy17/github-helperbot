Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
If you want to add support for a new site, first of all **make sure** this site is **not dedicated to [copyright infringement](README.md#can-you-add-support-for-this-anime-video-site-or-site-which-shows-current-movies-for-free)**. youtube-dl does **not support** such sites thus pull requests adding support for them **will be rejected**.  
After you have ensured this site is distributing its content legally, you can follow this quick list (assuming your service is called `yourextractor`):  
1. [Fork this repository](https://github.com/ytdl-org/youtube-dl/fork)
2. Check out the source code with:  
git clone git@github.com:YOUR_GITHUB_USERNAME/youtube-dl.git  
3. Start a new git branch with  
cd youtube-dl
git checkout -b yourextractor  
4. Start with this simple template and save it to `youtube_dl/extractor/yourextractor.py`:  
```python
# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class YourExtractorIE(InfoExtractor):
_VALID_URL = r'https?://(?:www\.)?yourextractor\.com/watch/(?P<id>[0-9]+)'
_TEST = {
'url': 'https://yourextractor.com/watch/42',
'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
'info_dict': {
'id': '42',
'ext': 'mp4',
'title': 'Video title goes here',
'thumbnail': r're:^https?://.*\.jpg$',
# TODO more properties, either as:
# * A value
# * MD5 checksum; start the string with md5:
# * A regular expression; start the string with re:
# * Any Python type (for example int or float)
}
}

def _real_extract(self, url):
video_id = self._match_id(url)
webpage = self._download_webpage(url, video_id)

# TODO more code goes here, for example ...
title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

return {
'id': video_id,
'title': title,
'description': self._og_search_description(webpage),
'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
# TODO more properties (see youtube_dl/extractor/common.py)
}
```
5. Add an import in [`youtube_dl/extractor/extractors.py`](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/extractors.py).
6. Run `python test/test_download.py TestDownload.test_YourExtractor`. This *should fail* at first, but you can continually re-run it until you're done. If you decide to add more than one test (actually, test case) then rename ``_TEST`` to ``_TESTS`` and make it into a list of dictionaries. The tests will then be named `TestDownload.test_YourExtractor`, `TestDownload.test_YourExtractor_1`, `TestDownload.test_YourExtractor_2`, etc. Note:
* the test names use the extractor class name **without the trailing `IE`**
* tests with `only_matching` key in test's dict are not counted.
8. Have a look at [`youtube_dl/extractor/common.py`](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/common.py) for possible helper methods and a [detailed description of what your extractor should and may return](https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303). Add tests and code for as many as you want.
9. Make sure your code follows [youtube-dl coding conventions](#youtube-dl-coding-conventions) and check the code with [flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart):  
$ flake8 youtube_dl/extractor/yourextractor.py  
9. Make sure your code works under all [Python](https://www.python.org/) versions claimed supported by youtube-dl, namely 2.6, 2.7, and 3.2+.
10. When the tests pass, [add](https://git-scm.com/docs/git-add) the new files and [commit](https://git-scm.com/docs/git-commit) them and [push](https://git-scm.com/docs/git-push) the result, like this:  
$ git add youtube_dl/extractor/extractors.py
$ git add youtube_dl/extractor/yourextractor.py
$ git commit -m '[yourextractor] Add new extractor'
$ git push origin yourextractor  
11. Finally, [create a pull request](https://help.github.com/articles/creating-a-pull-request). We'll then review and merge it.  
In any case, thank you very much for your contributions!