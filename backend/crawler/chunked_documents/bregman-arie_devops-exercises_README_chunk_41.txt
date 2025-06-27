Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Highly Available "Hello World" | [Exercise](topics/devops/ha_hello_world.md) | [Solution](topics/devops/solutions/ha_hello_world.md)  
<details>
<summary>What happens when you type in a URL in an address bar in a browser?</summary><br><b>  
1. The browser searches for the record of the domain name IP address in the DNS in the following order:
* Browser cache
* Operating system cache
* The DNS server configured on the user's system (can be ISP DNS, public DNS, ...)
2. If it couldn't find a DNS record locally, a full DNS resolution is started.
3. It connects to the server using the TCP protocol
4. The browser sends an HTTP request to the server
5. The server sends an HTTP response back to the browser
6. The browser renders the response (e.g. HTML)
7. The browser then sends subsequent requests as needed to the server to get the embedded links, javascript, images in the HTML and then steps 3 to 5 are repeated.  
TODO: add more details!
</b></details>