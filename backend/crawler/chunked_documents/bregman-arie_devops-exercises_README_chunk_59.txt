Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Scalability</summary><br><b>  
The ability easily grow in size and capacity based on demand and usage.
</b></details>  
<details>
<summary>Explain Elasticity</summary><br><b>  
The ability to grow but also to reduce based on what is required
</b></details>  
<details>
<summary>Explain Disaster Recovery</summary><br><b>  
Disaster recovery is the process of restoring critical business systems and data after a disruptive event. The goal is to minimize the impact and resume normal business activities quickly. This involves creating a plan, testing it, backing up critical data, and storing it in safe locations. In case of a disaster, the plan is then executed, backups are restored, and systems are hopefully brought back online. The recovery process may take hours or days depending on the damages of infrastructure. This makes business planning important, as a well-designed and tested disaster recovery plan can minimize the impact of a disaster and keep operations going.
</b></details>  
<details>
<summary>Explain Fault Tolerance and High Availability</summary><br><b>  
Fault Tolerance - The ability to self-heal and return to normal capacity. Also the ability to withstand a failure and remain functional.  
High Availability - Being able to access a resource (in some use cases, using different platforms)
</b></details>  
<details>
<summary>What is the difference between high availability and Disaster Recovery?</summary><br><b>  
[wintellect.com](https://www.wintellect.com/high-availability-vs-disaster-recovery): "High availability, simply put, is eliminating single points of failure and disaster recovery is the process of getting a system back to an operational state when a system is rendered inoperative. In essence, disaster recovery picks up when high availability fails, so HA first."
</b></details>  
<details>
<summary>Explain Vertical Scaling</summary><br><b>  
Vertical Scaling is the process of adding resources to increase power of existing servers. For example, adding more CPUs, adding more RAM, etc.
</b></details>  
<details>
<summary>What are the disadvantages of Vertical Scaling?</summary><br><b>  
With vertical scaling alone, the component still remains a single point of failure.
In addition, it has hardware limit where if you don't have more resources, you might not be able to scale vertically.
</b></details>  
<details>
<summary>Which type of cloud services usually support vertical scaling?</summary><br><b>  
Databases, cache. It's common mostly for non-distributed systems.
</b></details>  
<details>
<summary>Explain Horizontal Scaling</summary><br><b>  
Horizontal Scaling is the process of adding more resources that will be able handle requests as one unit
</b></details>  
<details>
<summary>What is the disadvantage of Horizontal Scaling? What is often required in order to perform Horizontal Scaling?</summary><br><b>  
A load balancer. You can add more resources, but if you would like them to be part of the process, you have to serve them the requests/responses.
Also, data inconsistency is a concern with horizontal scaling.
</b></details>  
<details>
<summary>Explain in which use cases will you use vertical scaling and in which use cases you will use horizontal scaling</summary><br><b>
</b></details>  
<details>
<summary>Explain Resiliency and what ways are there to make a system more resilient</summary><br><b>
</b></details>  
<details>
<summary>Explain "Consistent Hashing"</summary><br><b>
</b></details>  
<details>
<summary>How would you update each of the services in the following drawing without having app (foo.com) downtime?<br>
<img src="images/design/cdn-no-downtime.png" width="300x;" height="400px;"/>
</summary><br><b>
</b></details>  
<details>
<summary>What is the problem with the following architecture and how would you fix it?<br>
<img src="images/design/producers_consumers_issue.png" width="400x;" height="300px;"/>
</summary><br><b>  
The load on the producers or consumers may be high which will then cause them to hang or crash.<br>
Instead of working in "push mode", the consumers can pull tasks only when they are ready to handle them. It can be fixed by using a streaming platform like Kafka, Kinesis, etc. This platform will make sure to handle the high load/traffic and pass tasks/messages to consumers only when the ready to get them.  
<img src="images/design/producers_consumers_fix.png" width="300x;" height="200px;"/>
</b></details>  
<details>
<summary>Users report that there is huge spike in process time when adding little bit more data to process as an input. What might be the problem?<br>
<img src="images/design/input-process-output.png" width="300x;" height="200px;"/>
</summary><br><b>
</b></details>  
<details>
<summary>How would you scale the architecture from the previous question to hundreds of users?</summary><br><b>
</b></details>