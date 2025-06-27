Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
Whenever you query the database, hash the query as a key and store the result to the cache.  This approach suffers from expiration issues:  
* Hard to delete a cached result with complex queries
* If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell