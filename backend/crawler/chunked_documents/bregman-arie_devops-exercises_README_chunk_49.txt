Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain each of the following load balancing techniques  
* Round Robin
* Weighted Round Robin
* Least Connection
* Weighted Least Connection
* Resource Based
* Fixed Weighting
* Weighted Response Time
* Source IP Hash
* URL Hash
</summary><br><b>
</b></details>  
<details>
<summary>Explain use case for connection draining?</summary><br><b>
To ensure that a Classic Load Balancer stops sending requests to instances that are de-registering or unhealthy, while keeping the existing connections open, use connection draining. This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy.  
The maximum timeout value can be set between 1 and 3,600 seconds on both GCP and AWS.  
</b></details>