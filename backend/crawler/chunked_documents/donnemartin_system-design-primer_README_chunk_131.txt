Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
* There could be data loss if the cache goes down prior to its contents hitting the data store.
* It is more complex to implement write-behind than it is to implement cache-aside or write-through.