Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
Since `face_recognition` depends on `dlib` which is written in C++, it can be tricky to deploy an app
using it to a cloud hosting provider like Heroku or AWS.  
To make things easier, there's an example Dockerfile in this repo that shows how to run an app built with
`face_recognition` in a [Docker](https://www.docker.com/) container. With that, you should be able to deploy
to any service that supports Docker images.  
You can try the Docker image locally by running: `docker-compose up --build`  
There are also [several prebuilt Docker images.](docker/README.md)  
Linux users with a GPU (drivers >= 384.81) and [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker) installed can run the example on the GPU: Open the [docker-compose.yml](docker-compose.yml) file and uncomment the `dockerfile: Dockerfile.gpu` and `runtime: nvidia` lines.