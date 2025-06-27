Repository: infiniflow/ragflow
Language: Python
Stars: 57089
Forks: 5604
-----
This image is approximately 2 GB in size and relies on external LLM and embedding services.  
```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build --platform linux/amd64 --build-arg LIGHTEN=1 -f Dockerfile -t infiniflow/ragflow:nightly-slim .
```