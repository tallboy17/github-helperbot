Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
* Scaling horizontally introduces complexity and involves cloning servers
* Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
* Sessions can be stored in a centralized data store such as a [database](#database) (SQL, NoSQL) or a persistent [cache](#cache) (Redis, Memcached)
* Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out