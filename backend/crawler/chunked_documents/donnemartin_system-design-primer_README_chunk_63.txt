Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
* CDN costs could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.
* Content might be stale if it is updated before the TTL expires it.
* CDNs require changing URLs for static content to point to the CDN.