Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Can you describe Horizon in detail?</summary><br><b>  
* Django-based project focusing on providing an OpenStack dashboard and the ability to create additional customized dashboards
* You can use it to access the different OpenStack services resources - instances, images, networks, ...
* By accessing the dashboard, users can use it to list, create, remove and modify the different resources
* It's also highly customizable and you can modify or add to it based on your needs
</b></details>  
<details>
<summary>What can you tell about Horizon architecture?</summary><br><b>  
* API is backward compatible
* There are three type of dashboards: user, system and settings
* It provides core support for all OpenStack core projects such as Neutron, Nova, etc. (out of the box, no need to install extra packages or plugins)
* Anyone can extend the dashboards and add new components
* Horizon provides templates and core classes from which one can build its own dashboard
</b></details>