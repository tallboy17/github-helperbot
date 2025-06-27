Repository: bregman-arie/devops-exercises
Language: Python
Stars: 76756
Forks: 17234
-----
<details>
<summary>What is HTTP?</summary><br><b>  
[Avinetworks](https://avinetworks.com/glossary/layer-7/): HTTP stands for Hypertext Transfer Protocol. HTTP uses TCP port 80 to enable internet communication. It is part of the Application Layer (L7) in OSI Model.
</b></details>  
<details>
<summary>Describe HTTP request lifecycle</summary><br><b>  
* Resolve host by request to DNS resolver
* Client SYN
* Server SYN+ACK
* Client SYN
* HTTP request
* HTTP response
</b></details>  
<details>
<summary>True or False? HTTP is stateful</summary><br><b>  
False. It doesn't maintain state for incoming request.
</b></details>  
<details>
<summary>How HTTP request looks like?</summary><br><b>  
It consists of:  
* Request line - request type
* Headers - content info like length, encoding, etc.
* Body (not always included)
</b></details>  
<details>
<summary>What HTTP method types are there?</summary><br><b>  
* GET
* POST
* HEAD
* PUT
* DELETE
* CONNECT
* OPTIONS
* TRACE
</b></details>  
<details>
<summary>What HTTP response codes are there?</summary><br><b>  
* 1xx - informational
* 2xx - Success
* 3xx - Redirect
* 4xx - Error, client fault
* 5xx - Error, server fault
</b></details>  
<details>
<summary>What is HTTPS?</summary><br><b>  
HTTPS is a secure version of the HTTP protocol used to transfer data between a web browser and a web server. It encrypts the communication using SSL/TLS encryption to ensure that the data is private and secure.  
Learn more: https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/
</b></details>  
<details>
<summary>Explain HTTP Cookies</summary><br><b>  
HTTP is stateless. To share state, we can use Cookies.  
TODO: explain what is actually a Cookie
</b></details>  
<details>
<summary>What is HTTP Pipelining?</summary><br><b>
</b></details>  
<details>
<summary>You get "504 Gateway Timeout" error from an HTTP server. What does it mean?</summary><br><b>  
The server didn't receive a response from another server it communicates with in a timely manner.
</b></details>  
<details>
<summary>What is a proxy?</summary><br><b>  
A proxy is a server that acts as a middleman between a client device and a destination server. It can help improve privacy, security, and performance by hiding the client's IP address, filtering content, and caching frequently accessed data.
- Proxies can be used for load balancing, distributing traffic across multiple servers to help prevent server overload and improve website or application performance. They can also be used for data analysis, as they can log requests and traffic, providing useful insights into user behavior and preferences.
</b></details>  
<details>
<summary>What is a reverse proxy?</summary><br><b>  
A reverse proxy is a type of proxy server that sits between a client and a server, but it is used to manage traffic going in the opposite direction of a traditional forward proxy. In a forward proxy, the client sends requests to the proxy server, which then forwards them to the destination server. However, in a reverse proxy, the client sends requests to the destination server, but the requests are intercepted by the reverse proxy before they reach the server.
- They're commonly used to improve web server performance, provide high availability and fault tolerance, and enhance security by preventing direct access to the back-end server. They are often used in large-scale web applications and high-traffic websites to manage and distribute requests to multiple servers, resulting in improved scalability and reliability.
</b></details>  
<details>
<summary>When you publish a project, you usually publish it with a license. What types of licenses are you familiar with and which one do you prefer to use?</summary><br><b>
</b></details>  
<details>
<summary>Explain what is "X-Forwarded-For"</summary><br><b>  
[Wikipedia](https://en.wikipedia.org/wiki/X-Forwarded-For): "The X-Forwarded-For (XFF) HTTP header field is a common method for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer."
</b></details>