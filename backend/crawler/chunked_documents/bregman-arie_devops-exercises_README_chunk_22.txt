Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>Explain Neutron in detail</summary><br><b>  
* One of the core component of OpenStack and a standalone project
* Neutron focused on delivering networking as a service
* With Neutron, users can set up networks in the cloud and configure and manage a variety of network services
* Neutron interacts with:
* Keystone - authorize API calls
* Nova - nova communicates with neutron to plug NICs into a network
* Horizon - supports networking entities in the dashboard and also provides topology view which includes networking details
</b></details>  
<details>
<summary>Explain each of the following components:  
- neutron-dhcp-agent
- neutron-l3-agent
- neutron-metering-agent
- neutron-*-agtent
- neutron-server</summary><br><b>  
* neutron-l3-agent - L3/NAT forwarding (provides external network access for VMs for example)
* neutron-dhcp-agent - DHCP services
* neutron-metering-agent - L3 traffic metering
* neutron-*-agtent - manages local vSwitch configuration on each compute (based on chosen plugin)
* neutron-server - exposes networking API and passes requests to other plugins if required
</b></details>  
<details>
<summary>Explain these network types:  
- Management Network
- Guest Network
- API Network
- External Network</summary><br><b>  
* Management Network - used for internal communication between OpenStack components. Any IP address in this network is accessible only within the datacetner
* Guest Network - used for communication between instances/VMs
* API Network - used for services API communication. Any IP address in this network is publicly accessible
* External Network - used for public communication. Any IP address in this network is accessible by anyone on the internet
</b></details>  
<details>
<summary>In which order should you remove the following entities:  
* Network
* Port
* Router
* Subnet</summary><br><b>  
- Port
- Subnet
- Router
- Network  
There are many reasons for that. One for example: you can't remove router if there are active ports assigned to it.
</b></details>  
<details>
<summary>What is a provider network?</summary><br><b>
</b></details>  
<details>
<summary>What components and services exist for L2 and L3?</summary><br><b>
</b></details>  
<details>
<summary>What is the ML2 plug-in? Explain its architecture</summary><br><b>
</b></details>  
<details>
<summary>What is the L2 agent? How does it works and what is it responsible for?</summary><br><b>
</b></details>  
<details>
<summary>What is the L3 agent? How does it works and what is it responsible for?</summary><br><b>
</b></details>  
<details>
<summary>Explain what the Metadata agent is responsible for</summary><br><b>
</b></details>  
<details>
<summary>What networking entities Neutron supports?</summary><br><b>
</b></details>  
<details>
<summary>How do you debug OpenStack networking issues? (tools, logs, ...)</summary><br><b>
</b></details>