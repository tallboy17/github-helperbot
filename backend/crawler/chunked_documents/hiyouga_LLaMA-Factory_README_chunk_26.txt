Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
For CUDA users:  
```bash
cd docker/docker-cuda/
docker compose up -d
docker compose exec llamafactory bash
```  
For Ascend NPU users:  
```bash
cd docker/docker-npu/
docker compose up -d
docker compose exec llamafactory bash
```  
For AMD ROCm users:  
```bash
cd docker/docker-rocm/
docker compose up -d
docker compose exec llamafactory bash
```  
<details><summary>Build without Docker Compose</summary>  
For CUDA users:  
```bash
docker build -f ./docker/docker-cuda/Dockerfile \
--build-arg PIP_INDEX=https://pypi.org/simple \
--build-arg EXTRAS=metrics \
-t llamafactory:latest .

docker run -dit --ipc=host --gpus=all \
-p 7860:7860 \
-p 8000:8000 \
--name llamafactory \
llamafactory:latest

docker exec -it llamafactory bash
```  
For Ascend NPU users:  
```bash
docker build -f ./docker/docker-npu/Dockerfile \
--build-arg PIP_INDEX=https://pypi.org/simple \
--build-arg EXTRAS=torch-npu,metrics \
-t llamafactory:latest .

docker run -dit --ipc=host \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-p 7860:7860 \
-p 8000:8000 \
--device /dev/davinci0 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
--name llamafactory \
llamafactory:latest

docker exec -it llamafactory bash
```  
For AMD ROCm users:  
```bash
docker build -f ./docker/docker-rocm/Dockerfile \
--build-arg PIP_INDEX=https://pypi.org/simple \
--build-arg EXTRAS=metrics \
-t llamafactory:latest .

docker run -dit --ipc=host \
-p 7860:7860 \
-p 8000:8000 \
--device /dev/kfd \
--device /dev/dri \
--name llamafactory \
llamafactory:latest

docker exec -it llamafactory bash
```  
</details>  
<details><summary>Use Docker volumes</summary>  
You can uncomment `VOLUME [ "/root/.cache/huggingface", "/app/shared_data", "/app/output" ]` in the Dockerfile to use data volumes.  
When building the Docker image, use `-v ./hf_cache:/root/.cache/huggingface` argument to mount the local directory to the container. The following data volumes are available.  
- `hf_cache`: Utilize Hugging Face cache on the host machine.
- `shared_data`: The directionary to store datasets on the host machine.
- `output`: Set export dir to this location so that the merged result can be accessed directly on the host machine.  
</details>