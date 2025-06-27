Repository: infiniflow/ragflow
Language: Python
Stars: 57089
Forks: 5604
-----
1. Install uv, or skip this step if it is already installed:  
```bash
pipx install uv pre-commit
```  
2. Clone the source code and install Python dependencies:  
```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
uv sync --python 3.10 --all-extras # install RAGFlow dependent python modules
uv run download_deps.py
pre-commit install
```  
3. Launch the dependent services (MinIO, Elasticsearch, Redis, and MySQL) using Docker Compose:  
```bash
docker compose -f docker/docker-compose-base.yml up -d
```  
Add the following line to `/etc/hosts` to resolve all hosts specified in **docker/.env** to `127.0.0.1`:  
```
127.0.0.1       es01 infinity mysql minio redis sandbox-executor-manager
```  
4. If you cannot access HuggingFace, set the `HF_ENDPOINT` environment variable to use a mirror site:  
```bash
export HF_ENDPOINT=https://hf-mirror.com
```  
5. If your operating system does not have jemalloc, please install it as follows:  
```bash
# ubuntu
sudo apt-get install libjemalloc-dev
# centos
sudo yum install jemalloc
```  
6. Launch backend service:  
```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
bash docker/launch_backend_service.sh
```  
7. Install frontend dependencies:  
```bash
cd web
npm install
```  
8. Launch frontend service:  
```bash
npm run dev
```  
_The following output confirms a successful launch of the system:_  
![](https://github.com/user-attachments/assets/0daf462c-a24d-4496-a66f-92533534e187)  
9. Stop RAGFlow front-end and back-end service after development is complete:  
```bash
pkill -f "ragflow_server.py|task_executor.py"
```