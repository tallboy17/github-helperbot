Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Swift in detail</summary><br><b>  
* Swift is Object Store service and is an highly available, distributed and consistent store designed for storing a lot of data
* Swift is distributing data across multiple servers while writing it to multiple disks
* One can choose to add additional servers to scale the cluster. All while swift maintaining integrity of the information and data replications.
</b></details>  
<details>
<summary>Can users store by default an object of 100GB in size?</summary><br><b>  
Not by default. Object Storage API limits the maximum to 5GB per object but it can be adjusted.
</b></details>  
<details>
<summary>Explain the following in regards to Swift:  
* Container
* Account
* Object
</summary><br><b>  
- Container - Defines a namespace for objects.
- Account - Defines a namespace for containers
- Object - Data content (e.g. image, document, ...)
</b></details>  
<details>
<summary>True or False? there can be two objects with the same name in the same container but not in two different containers</summary><br><b>  
False. Two objects can have the same name if they are in different containers.
</b></details>