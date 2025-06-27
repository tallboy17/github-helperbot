Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is Virtualization?</summary><br><b>  
Virtualization uses software to create an abstraction layer over computer hardware, that allows the hardware elements of a single computer - processors, memory, storage and more - to be divided into multiple virtual computers, commonly called virtual machines (VMs).
</b></details>  
<details>
<summary>What is a hypervisor?</summary><br><b>  
Red Hat: "A hypervisor is software that creates and runs virtual machines (VMs). A hypervisor, sometimes called a virtual machine monitor (VMM), isolates the hypervisor operating system and resources from the virtual machines and enables the creation and management of those VMs."  
Read more [here](https://www.redhat.com/en/topics/virtualization/what-is-a-hypervisor)
</b></details>  
<details>
<summary>What types of hypervisors are there?</summary><br><b>  
Hosted hypervisors and bare-metal hypervisors.
</b></details>  
<details>
<summary>What are the advantages and disadvantges of bare-metal hypervisor over a hosted hypervisor?</summary><br><b>  
Due to having its own drivers and a direct access to hardware components, a baremetal hypervisor will often have better performances along with stability and scalability.  
On the other hand, there will probably be some limitation regarding loading (any) drivers so a hosted hypervisor will usually benefit from having a better hardware compatibility.
</b></details>  
<details>
<summary>What types of virtualization are there?</summary><br><b>  
Operating system virtualization
Network functions virtualization
Desktop virtualization
</b></details>  
<details>
<summary>Is containerization is a type of Virtualization?</summary><br><b>  
Yes, it's a operating-system-level virtualization, where the kernel is shared and allows to use multiple isolated user-spaces instances.
</b></details>  
<details>
<summary>How the introduction of virtual machines changed the industry and the way applications were deployed?</summary><br><b>  
The introduction of virtual machines allowed companies to deploy multiple business applications on the same hardware, while each application is separated from each other in secured way, where each is running on its own separate operating system.
</b></details>