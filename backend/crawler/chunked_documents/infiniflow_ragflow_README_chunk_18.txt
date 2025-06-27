Repository: infiniflow/ragflow
Language: Python
Stars: 57089
Forks: 5604
-----
This image is approximately 9 GB in size. As it includes embedding models, it relies on external LLM services only.  
```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build --platform linux/amd64 -f Dockerfile -t infiniflow/ragflow:nightly .
```