Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
<p align="center">
<img src="images/rgSrvjG.png">
<br/>
<i><a href=http://www.slideshare.net/jboner/scalability-availability-stability-patterns/>Source: Scalability, availability, stability, patterns</a></i>
</p>  
In write-behind, the application does the following:  
* Add/update entry in cache
* Asynchronously write entry to the data store, improving write performance