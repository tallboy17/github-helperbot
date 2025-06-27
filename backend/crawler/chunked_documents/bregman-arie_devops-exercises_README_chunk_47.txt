Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is a load balancer?</summary><br><b>  
A load balancer accepts (or denies) incoming network traffic from a client, and based on some criteria (application related, network, etc.) it distributes those communications out to servers (at least one).
</b></details>  
<details>
<summary>Why to used a load balancer?</summary><br><b>  
* Scalability - using a load balancer, you can possibly add more servers in the backend to handle more requests/traffic from the clients, as opposed to using one server.
* Redundancy - if one server in the backend dies, the load balancer will keep forwarding the traffic/requests to the second server so users won't even notice one of the servers in the backend is down.
</b></details>  
<details>
<summary>What load balancer techniques/algorithms are you familiar with?</summary><br><b>  
* Round Robin
* Weighted Round Robin
* Least Connection
* Weighted Least Connection
* Resource Based
* Fixed Weighting
* Weighted Response Time
* Source IP Hash
* URL Hash
</b></details>  
<details>
<summary>What are the drawbacks of round robin algorithm in load balancing?</summary><br><b>  
* A simple round robin algorithm knows nothing about the load and the spec of each server it forwards the requests to. It is possible, that multiple heavy workloads requests will get to the same server while other servers will got only lightweight requests which will result in one server doing most of the work, maybe even crashing at some point because it unable to handle all the heavy workloads requests by its own.
* Each request from the client creates a whole new session. This might be a problem for certain scenarios where you would like to perform multiple operations where the server has to know about the result of operation so basically, being sort of aware of the history it has with the client. In round robin, first request might hit server X, while second request might hit server Y and ask to continue processing the data that was processed on server X already.
</b></details>  
<details>
<summary>What is an Application Load Balancer?</summary><br><b>
</b></details>  
<details>
<summary>In which scenarios would you use ALB?</summary><br><b>
</b></details>  
<details>
<summary>At what layers a load balancer can operate?</summary><br><b>  
L4 and L7
</b></details>  
<details>
<summary>Can you perform load balancing without using a dedicated load balancer instance?</summary><br><b>  
Yes, you can use DNS for performing load balancing.
</b></details>  
<details>
<summary>What is DNS load balancing? What its advantages? When would you use it?</summary><br><b>
</b></details>