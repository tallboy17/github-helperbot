Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
The master serves reads and writes, replicating writes to one or more slaves, which serve only reads.  Slaves can also replicate to additional slaves in a tree-like fashion.  If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.  
<p align="center">
<img src="images/C9ioGtn.png">
<br/>
<i><a href=http://www.slideshare.net/jboner/scalability-availability-stability-patterns/>Source: Scalability, availability, stability, patterns</a></i>
</p>