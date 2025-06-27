Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
<p align="center">
<img src="images/0vBc0hN.png">
<br/>
<i><a href=http://www.slideshare.net/jboner/scalability-availability-stability-patterns/>Source: Scalability, availability, stability, patterns</a></i>
</p>  
The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:  
* Application adds/updates entry in cache
* Cache synchronously writes entry to data store
* Return  
Application code:  
```python
set_user(12345, {"foo":"bar"})
```  
Cache code:  
```python
def set_user(user_id, values):
user = db.query("UPDATE Users WHERE id = {0}", user_id, values)
cache.set(user_id, user)
```  
Write-through is a slow overall operation due to the write operation, but subsequent reads of just written data are fast.  Users are generally more tolerant of latency when updating data than reading data.  Data in the cache is not stale.