Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
After a write, reads will see it.  Data is replicated synchronously.  
This approach is seen in file systems and RDBMSes.  Strong consistency works well in systems that need transactions.