Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
In active-active, both servers are managing traffic, spreading the load between them.  
If the servers are public-facing, the DNS would need to know about the public IPs of both servers.  If the servers are internal-facing, application logic would need to know about both servers.  
Active-active failover can also be referred to as master-master failover.