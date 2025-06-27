Repository: pytorch/pytorch
Language: Python
Stars: 90893
Forks: 24473
-----
You can also pull a pre-built docker image from Docker Hub and run with docker v19.03+  
```bash
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```  
Please note that PyTorch uses shared memory to share data between processes, so if torch multiprocessing is used (e.g.
for multithreaded data loaders) the default shared memory segment size that container runs with is not enough, and you
should increase shared memory size either with `--ipc=host` or `--shm-size` command line options to `nvidia-docker run`.