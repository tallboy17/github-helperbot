Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
[![Build Status](https://github.com/soimort/you-get/workflows/develop/badge.svg)](https://github.com/soimort/you-get/actions)
[![PyPI version](https://img.shields.io/pypi/v/you-get.svg)](https://pypi.python.org/pypi/you-get/)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/soimort/you-get?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)  
**NOTICE (30 May 2022): Support for Python 3.5, 3.6 and 3.7 will eventually be dropped. ([see details here](https://github.com/soimort/you-get/wiki/TLS-1.3-post-handshake-authentication-(PHA)))**  
**NOTICE (8 Mar 2019): Read [this](https://github.com/soimort/you-get/blob/develop/CONTRIBUTING.md) if you are looking for the conventional "Issues" tab.**  
---  
[You-Get](https://you-get.org/) is a tiny command-line utility to download media contents (videos, audios, images) from the Web, in case there is no other handy way to do it.  
Here's how you use `you-get` to download a video from [YouTube](https://www.youtube.com/watch?v=jNQXAC9IVRw):  
```console
$ you-get 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
site:                YouTube
title:               Me at the zoo
stream:
- itag:          43
container:     webm
quality:       medium
size:          0.5 MiB (564215 bytes)
# download-with: you-get --itag=43 [URL]

Downloading Me at the zoo.webm ...
100% (  0.5/  0.5MB) ├██████████████████████████████████┤[1/1]    6 MB/s

Saving Me at the zoo.en.srt ... Done.
```  
And here's why you might want to use it:  
* You enjoyed something on the Internet, and just want to download them for your own pleasure.
* You watch your favorite videos online from your computer, but you are prohibited from saving them. You feel that you have no control over your own computer. (And it's not how an open Web is supposed to work.)
* You want to get rid of any closed-source technology or proprietary JavaScript code, and disallow things like Flash running on your computer.
* You are an adherent of hacker culture and free software.  
What `you-get` can do for you:  
* Download videos / audios from popular websites such as YouTube, Youku, Niconico, and a bunch more. (See the [full list of supported sites](#supported-sites))
* Stream an online video in your media player. No web browser, no more ads.
* Download images (of interest) by scraping a web page.
* Download arbitrary non-HTML contents, i.e., binary files.  
Interested? [Install it](#installation) now and [get started by examples](#getting-started).  
Are you a Python programmer? Then check out [the source](https://github.com/soimort/you-get) and fork it!  
![](https://i.imgur.com/GfthFAz.png)