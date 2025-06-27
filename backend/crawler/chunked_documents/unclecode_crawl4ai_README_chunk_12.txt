Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
Run a quick test (works for both Docker options):  
```python
import requests

# Submit a crawl job
response = requests.post(
"http://localhost:11235/crawl",
json={"urls": "https://example.com", "priority": 10}
)
task_id = response.json()["task_id"]

# Continue polling until the task is complete (status="completed")
result = requests.get(f"http://localhost:11235/task/{task_id}")
```  
For more examples, see our [Docker Examples](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_example.py). For advanced configuration, environment variables, and usage examples, see our [Docker Deployment Guide](https://docs.crawl4ai.com/basic/docker-deployment/).  
</details>