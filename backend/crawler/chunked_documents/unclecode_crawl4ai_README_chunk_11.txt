Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
```bash
# Pull and run the latest release candidate
docker pull unclecode/crawl4ai:0.6.0-rN # Use your favorite revision number
docker run -d -p 11235:11235 --name crawl4ai --shm-size=1g unclecode/crawl4ai:0.6.0-rN # Use your favorite revision number

# Visit the playground at http://localhost:11235/playground
```  
For complete documentation, see our [Docker Deployment Guide](https://docs.crawl4ai.com/core/docker-deployment/).  
</details>  
---