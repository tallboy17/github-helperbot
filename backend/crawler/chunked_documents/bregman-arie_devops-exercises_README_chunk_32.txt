Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is Puppet? How does it works?</summary><br><b>  
* Puppet is a configuration management tool ensuring that all systems are configured to a desired and predictable state.
</b></details>
<details>
<summary>Explain Puppet architecture</summary><br><b>  
* Puppet has a primary-secondary node architecture. The clients are distributed across the network and communicate with the primary-secondary environment where Puppet modules are present. The client agent sends a certificate with its ID to the server; the server then signs that certificate and sends it back to the client. This authentication allows for secure and verifiable communication between the client and the master.
</b></details>  
<details>
<summary>Can you compare Puppet to other configuration management tools? Why did you chose to use Puppet?</summary><br><b>  
* Puppet is often compared to other configuration management tools like Chef, Ansible, SaltStack, and cfengine. The choice to use Puppet often depends on an organization's needs, such as ease of use, scalability, and community support.
</b></details>  
<details>
<summary>Explain the following:  
* Module
* Manifest
* Node
</summary><br><b>  
* Modules - are a collection of manifests, templates, and files
* Manifests - are the actual codes for configuring the clients
* Node - allows you to assign specific configurations to specific nodes
</b></details>  
<details>
<summary>Explain Facter</summary><br><b>  
* Facter is a standalone tool in Puppet that collects information about a system and its configuration, such as the operating system, IP addresses, memory, and network interfaces. This information can be used in Puppet manifests to make decisions about how resources should be managed, and to customize the behavior of Puppet based on the characteristics of the system. Facter is integrated into Puppet, and its facts can be used within Puppet manifests to make decisions about resource management.
</b></details>  
<details>
<summary>What is MCollective?</summary><br><b>  
* MCollective is a middleware system that integrates with Puppet to provide orchestration, remote execution, and parallel job execution capabilities.
</b></details>  
<details>
<summary>Do you have experience with writing modules? Which module have you created and for what?</summary><br><b>
</b></details>  
<details>
<summary>Explain what is Hiera</summary><br><b>  
* Hiera is a hierarchical data store in Puppet that is used to separate data from code, allowing data to be more easily separated, managed, and reused.
</b></details>