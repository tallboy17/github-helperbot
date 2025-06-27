Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain what a "single point of failure" is. </summary><br><b>
A "single point of failure", in a system or organization, if it were to fail would cause the entire system to fail or significantly disrupt it's operation. In other words, it is a vulnerability where there
is no backup in place to compensate for the failure.
</b></details>  
<details>
<summary>What is CDN?</summary><br><b>  
CDN (Content Delivery Network) responsible for distributing content geographically. Part of it, is what is known as edge locations, aka cache proxies, that allows users to get their content quickly due to cache features and geographical distribution.
</b></details>  
<details>
<summary>Explain Multi-CDN</summary><br><b>  
In single CDN, the whole content is originated from content delivery network.<br>
In multi-CDN, content is distributed across multiple different CDNs, each might be on a completely different provider/cloud.
</b></details>  
<details>
<summary>What are the benefits of Multi-CDN over a single CDN?</summary><br><b>  
* Resiliency: Relying on one CDN means no redundancy. With multiple CDNs you don't need to worry about your CDN being down
* Flexibility in Costs: Using one CDN enforces you to specific rates of that CDN. With multiple CDNs you can take into consideration using less expensive CDNs to deliver the content.
* Performance: With Multi-CDN there is bigger potential in choosing better locations which more close to the client asking the content
* Scale: With multiple CDNs, you can scale services to support more extreme conditions
</b></details>  
<details>
<summary>Explain "3-Tier Architecture" (including pros and cons)</summary><br><b>
A "3-Tier Architecture" is a pattern used in software development for designing and structuring applications. It divides the application into 3 interconnected layers: Presentation, Business logic and Data storage.
PROS:
* Scalability
* Security
* Reusability
CONS:
* Complexity
* Performance overhead
* Cost and development time
</b></details>  
<details>
<summary>Explain Mono-repo vs. Multi-repo.What are the cons and pros of each approach?</summary><br><b>
In a Mono-repo, all the code for an organization is stored in a single,centralized repository.
PROS (Mono-repo):
* Unified tooling
* Code Sharing
CONS (Mono-repo):
* Increased complexity
* Slower cloning  
In a Multi-repo setup, each component is stored in it's own separate repository. Each repository has it's own version control history.
PROS (Multi-repo):
* Simpler to manage
* Different teams and developers can work on different parts of the project independently, making parallel development easier.
CONS (Multi-repo):
* Code duplication
* Integration challenges
</b></details>  
<details>
<summary>What are the drawbacks of monolithic architecture?</summary><br><b>  
* Not suitable for frequent code changes and the ability to deploy new features
* Not designed for today's infrastructure (like public clouds)
* Scaling a team to work monolithic architecture is more challenging
* If a single component in this architecture fails, then the entire application fails.
</b></details>  
<details>
<summary>What are the advantages of microservices architecture over a monolithic architecture?</summary><br><b>  
* Each of the services individually fail without escalating into an application-wide outage.
* Each service can be developed and maintained by a separate team and this team can choose its own tools and coding language
</b></details>  
<details>
<summary>What's a service mesh?</summary><br><b>
It is a layer that facilitates communication management and control between microservices in a containerized application. It handles tasks such as load balancing, encryption, and monitoring.
</b></details>  
<details>
<summary>Explain "Loose Coupling"</summary><br><b>
In "Loose Coupling", components of a system communicate with each other with a little understanding of each other's internal workings. This improves scalability and ease of modification in complex systems.
</b></details>  
<details>
<summary>What is a message queue? When is it used?</summary><br><b>
It is a communication mechanism used in distributed systems to enable asynchronous communication between different components. It is generally used when the systems use a microservices approach.
</b></details>