Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
Responses return the most readily available version of the data available on any node, which might not be the latest.  Writes might take some time to propagate when the partition is resolved.  
AP is a good choice if the business needs to allow for [eventual consistency](#eventual-consistency) or when the system needs to continue working despite external errors.