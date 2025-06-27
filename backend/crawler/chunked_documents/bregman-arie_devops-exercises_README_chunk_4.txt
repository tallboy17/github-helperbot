Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What does "control plane" refer to?</summary><br><b>  
The control plane is a part of the network that decides how to route and forward packets to a different location.
</b></details>  
<details>
<summary>What does "data plane" refer to?</summary><br><b>  
The data plane is a part of the network that actually forwards the data/packets.
</b></details>  
<details>
<summary>What does "management plane" refer to?</summary><br><b>  
It refers to monitoring and management functions.
</b></details>  
<details>
<summary>To which plane (data, control, ...) does creating routing tables belong to?</summary><br><b>  
Control Plane.
</b></details>  
<details>
<summary>Explain Spanning Tree Protocol (STP).</summary><br><b>
</b></details>  
<details>
<summary>What is link aggregation? Why is it used?</summary><br><b>
</b></details>  
<details>
<summary>What is Asymmetric Routing? How to deal with it?</summary><br><b>
</b></details>  
<details>
<summary>What overlay (tunnel) protocols are you familiar with?</summary><br><b>
</b></details>  
<details>
<summary>What is GRE? How does it work?</summary><br><b>
</b></details>  
<details>
<summary>What is VXLAN? How does it work?</summary><br><b>
</b></details>  
<details>
<summary>What is SNAT?</summary><br><b>
</b></details>  
<details>
<summary>Explain OSPF.</summary><br><b>  
OSPF (Open Shortest Path First) is a routing protocol that can be implemented on various types of routers. In general, OSPF is supported on most modern routers, including those from vendors such as Cisco, Juniper, and Huawei. The protocol is designed to work with IP-based networks, including both IPv4 and IPv6. Also, it uses a hierarchical network design, where routers are grouped into areas, with each area having its own topology map and routing table. This design helps to reduce the amount of routing information that needs to be exchanged between routers and improve network scalability.  
The OSPF 4 Types of routers are:
* Internal Router
* Area Border Routers
* Autonomous Systems Boundary Routers
* Backbone Routers  
Learn more about OSPF router types: https://www.educba.com/ospf-router-types/
</b></details>  
<details>
<summary>What is latency?</summary><br><b>  
Latency is the time taken for information to reach its destination from the source.
</b></details>  
<details>
<summary>What is bandwidth?</summary><br><b>  
Bandwidth is the capacity of a communication channel to measure how much data the latter can handle over a specific time period. More bandwidth would imply more traffic handling and thus more data transfer.
</b></details>  
<details>
<summary>What is throughput?</summary><br><b>  
Throughput refers to the measurement of the real amount of data transferred over a certain period of time across any transmission channel.
</b></details>  
<details>
<summary>When performing a search query, what is more important, latency or throughput? And how to ensure that we manage global infrastructure?
</summary><br><b>  
Latency. To have good latency, a search query should be forwarded to the closest data center.
</b></details>  
<details>
<summary>When uploading a video, what is more important, latency or throughput? And how to assure that?</summary><br><b>  
Throughput. To have good throughput, the upload stream should be routed to an underutilized link.
</b></details>  
<details>
<summary>What other considerations (except latency and throughput) are there when forwarding requests?</summary><br><b>  
* Keep caches updated (which means the request could be forwarded not to the closest data center)
</b></details>  
<details>
<summary>Explain Spine & Leaf</summary><br><b>
"Spine & Leaf" is a networking topology commonly used in data center environments to connect multiple switches and manage network traffic efficiently. It is also known as "spine-leaf" architecture or "leaf-spine" topology. This design provides high bandwidth, low latency, and scalability, making it ideal for modern data centers handling large volumes of data and traffic.  
Within a Spine & Leaf network there are two main tipology of switches:  
* Spine Switches: Spine switches are high-performance switches arranged in a spine layer. These switches act as the core of the network and are typically interconnected with each leaf switch. Each spine switch is connected to all the leaf switches in the data center.
* Leaf Switches: Leaf switches are connected to end devices like servers, storage arrays, and other networking equipment. Each leaf switch is connected to every spine switch in the data center. This creates a non-blocking, full-mesh connectivity between leaf and spine switches, ensuring any leaf switch can communicate with any other leaf switch with maximum throughput.  
The Spine & Leaf architecture has become increasingly popular in data centers due to its ability to handle the demands of modern cloud computing, virtualization, and big data applications, providing a scalable, high-performance, and reliable network infrastructure
</b></details>  
<details>
<summary>What is Network Congestion? What can cause it?</summary><br><b>  
Network congestion occurs when there is too much data to transmit on a network and it doesn't have enough capacity to handle the demand. </br>
This can lead to increased latency and packet loss. The causes can be multiple, such as high network usage, large file transfers, malware, hardware issues, or network design problems. </br>
To prevent network congestion, it's important to monitor your network usage and implement strategies to limit or manage the demand.
</b></details>  
<details>
<summary>What can you tell me about the UDP packet format? What about the TCP packet format? How is it different?</summary><br><b>
</b></details>  
<details>
<summary>What is the exponential backoff algorithm? Where is it used?</summary><br><b>
</b></details>  
<details>
<summary>Using Hamming code, what would be the code word for the following data word 100111010001101?</summary><br><b>  
00110011110100011101
</b></details>  
<details>
<summary>Give examples of protocols found in the application layer</summary><br><b>  
* Hypertext Transfer Protocol (HTTP) - used for the webpages on the internet
* Simple Mail Transfer Protocol (SMTP) - email transmission
* Telecommunications Network - (TELNET) - terminal emulation to allow a client access to a telnet server
* File Transfer Protocol (FTP) - facilitates the transfer of files between any two machines
* Domain Name System (DNS) - domain name translation
* Dynamic Host Configuration Protocol (DHCP) - allocates IP addresses, subnet masks, and gateways to hosts
* Simple Network Management Protocol (SNMP) - gathers data on devices on the network
</b></details>  
<details>
<summary>Give examples of protocols found in the Network Layer</summary><br><b>  
* Internet Protocol (IP) - assists in routing packets from one machine to another
* Internet Control Message Protocol (ICMP) - lets one know what is going such as error messages and debugging information
</b></details>  
<details>
<summary>What is HSTS?</summary><br><b>
HTTP Strict Transport Security is a web server directive that informs user agents and web browsers how to handle its connection through a response header sent at the very beginning and back to the browser. This forces connections over HTTPS encryption, disregarding any script's call to load any resource in that domain over HTTP.  
Read more [here](https://www.globalsign.com/en/blog/what-is-hsts-and-how-do-i-use-it#:~:text=HTTP%20Strict%20Transport%20Security%20(HSTS,and%20back%20to%20the%20browser.)
</b></details>