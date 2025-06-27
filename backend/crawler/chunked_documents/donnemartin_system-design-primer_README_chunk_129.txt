Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
* When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database.  Cache-aside in conjunction with write through can mitigate this issue.
* Most data written might never be read, which can be minimized with a TTL.