Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
Both masters serve reads and writes and coordinate with each other on writes.  If either master goes down, the system can continue to operate with both reads and writes.  
<p align="center">
<img src="images/krAHLGg.png">
<br/>
<i><a href=http://www.slideshare.net/jboner/scalability-availability-stability-patterns/>Source: Scalability, availability, stability, patterns</a></i>
</p>