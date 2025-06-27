Repository: minimaxir/big-list-of-naughty-strings
Language: Python
Stars: 47222
Forks: 2153
-----
Even multi-billion dollar companies with huge amounts of automated testing can't find every bad input. For example, look at what happens when you try to Tweet a [zero-width space](https://en.wikipedia.org/wiki/Zero-width_space) (U+200B) on Twitter:  
![](http://i.imgur.com/HyDg2eV.gif)  
Although this is not a malicious error, and typical users aren't Tweeting weird unicode, an "internal server error" for unexpected input is never a positive experience for the user, and may in fact be a symptom of deeper string-validation issues. The Big List of Naughty Strings is intended to help reveal such issues.