Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
<p align="center">
<img src="images/h9TAuGI.jpg">
<br/>
<i><a href=https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/>Source: Why use a CDN</a></i>
</p>  
A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user.  Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content.  The site's DNS resolution will tell clients which server to contact.  
Serving content from CDNs can significantly improve performance in two ways:  
* Users receive content from data centers close to them
* Your servers do not have to serve requests that the CDN fulfills