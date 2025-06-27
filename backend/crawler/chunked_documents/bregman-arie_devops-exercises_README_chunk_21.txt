Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Can you describe Nova in detail?</summary><br><b>  
* Used to provision and manage virtual instances
* It supports Multi-Tenancy in different levels - logging, end-user control, auditing, etc.
* Highly scalable
* Authentication can be done using internal system or LDAP
* Supports multiple types of block storage
* Tries to be hardware and hypervisor agnostice
</b></details>  
<details>
<summary>What do you know about Nova architecture and components?</summary><br><b>  
* nova-api - the server which serves metadata and compute APIs
* the different Nova components communicate by using a queue (Rabbitmq usually) and a database
* a request for creating an instance is inspected by nova-scheduler which determines where the instance will be created and running
* nova-compute is the component responsible for communicating with the hypervisor for creating the instance and manage its lifecycle
</b></details>