Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
HTTP is a method for encoding and transporting data between a client and a server.  It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request.  HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.  
A basic HTTP request consists of a verb (method) and a resource (endpoint).  Below are common HTTP verbs:  
| Verb | Description | Idempotent* | Safe | Cacheable |
|---|---|---|---|---|
| GET | Reads a resource | Yes | Yes | Yes |
| POST | Creates a resource or trigger a process that handles data | No | No | Yes if response contains freshness info |
| PUT | Creates or replace a resource | Yes | No | No |
| PATCH | Partially updates a resource | No | No | Yes if response contains freshness info |
| DELETE | Deletes a resource | Yes | No | No |  
*Can be called many times without different outcomes.  
HTTP is an application layer protocol relying on lower-level protocols such as **TCP** and **UDP**.