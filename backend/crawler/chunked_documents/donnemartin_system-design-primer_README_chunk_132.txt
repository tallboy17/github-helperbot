Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
<p align="center">
<img src="images/kxtjqgE.png">
<br/>
<i><a href=http://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast>Source: From cache to in-memory data grid</a></i>
</p>  
You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.  
Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.