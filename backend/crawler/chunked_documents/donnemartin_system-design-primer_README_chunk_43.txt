Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
After a write, reads will eventually see it (typically within milliseconds).  Data is replicated asynchronously.  
This approach is seen in systems such as DNS and email.  Eventual consistency works well in highly available systems.