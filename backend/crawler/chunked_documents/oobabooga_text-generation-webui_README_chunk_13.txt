Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
```
For NVIDIA GPU:
ln -s docker/{nvidia/Dockerfile,nvidia/docker-compose.yml,.dockerignore} .
For AMD GPU:
ln -s docker/{amd/Dockerfile,amd/docker-compose.yml,.dockerignore} .
For Intel GPU:
ln -s docker/{intel/Dockerfile,amd/docker-compose.yml,.dockerignore} .
For CPU only
ln -s docker/{cpu/Dockerfile,cpu/docker-compose.yml,.dockerignore} .
cp docker/.env.example .env
#Create logs/cache dir :
mkdir -p user_data/logs user_data/cache
# Edit .env and set:
#   TORCH_CUDA_ARCH_LIST based on your GPU model
#   APP_RUNTIME_GID      your host user's group id (run `id -g` in a terminal)
#   BUILD_EXTENIONS      optionally add comma separated list of extensions to build
# Edit user_data/CMD_FLAGS.txt and add in it the options you want to execute (like --listen --cpu)
#
docker compose up --build
```  
* You need to have Docker Compose v2.17 or higher installed. See [this guide](https://github.com/oobabooga/text-generation-webui/wiki/09-%E2%80%90-Docker) for instructions.
* For additional docker files, check out [this repository](https://github.com/Atinoda/text-generation-webui-docker).