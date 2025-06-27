Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
If you already have the URL of the exact resource you want, you can download it directly with:  
```
$ you-get https://stallman.org/rms.jpg
Site:       stallman.org
Title:      rms
Type:       JPEG Image (image/jpeg)
Size:       0.06 MiB (66482 Bytes)

Downloading rms.jpg ...
100% (  0.1/  0.1MB) ├████████████████████████████████████████┤[1/1]  127 kB/s
```  
Otherwise, `you-get` will scrape the web page and try to figure out if there's anything interesting to you:  
```
$ you-get https://kopasas.tumblr.com/post/69361932517
Site:       Tumblr.com
Title:      [tumblr] tumblr_mxhg13jx4n1sftq6do1_640
Type:       Portable Network Graphics (image/png)
Size:       0.11 MiB (118484 Bytes)

Downloading [tumblr] tumblr_mxhg13jx4n1sftq6do1_640.png ...
100% (  0.1/  0.1MB) ├████████████████████████████████████████┤[1/1]   22 MB/s
```  
**Note:**  
* This feature is an experimental one and far from perfect. It works best on scraping large-sized images from popular websites like Tumblr and Blogger, but there is really no universal pattern that can apply to any site on the Internet.