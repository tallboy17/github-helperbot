Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
With active-passive fail-over, heartbeats are sent between the active and the passive server on standby.  If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.  
The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby.  Only the active server handles traffic.  
Active-passive failover can also be referred to as master-slave failover.