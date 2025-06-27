Repository: hpcaitech/ColossalAI
Language: Python
Stars: 40976
Forks: 4521
-----
Run the following command to build a docker image from Dockerfile provided.  
> Building Colossal-AI from scratch requires GPU support, you need to use Nvidia Docker Runtime as the default when doing `docker build`. More details can be found [here](https://stackoverflow.com/questions/59691207/docker-build-with-nvidia-runtime).
> We recommend you install Colossal-AI from our [project page](https://www.colossalai.org) directly.  
```bash
cd ColossalAI
docker build -t colossalai ./docker
```  
Run the following command to start the docker container in interactive mode.  
```bash
docker run -ti --gpus all --rm --ipc=host colossalai bash
```  
<p align="right">(<a href="#top">back to top</a>)</p>