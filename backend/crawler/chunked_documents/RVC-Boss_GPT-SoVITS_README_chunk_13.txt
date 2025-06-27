Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
Due to rapid development in the codebase and a slower Docker image release cycle, please:  
- Check [Docker Hub](https://hub.docker.com/r/xxxxrt666/gpt-sovits) for the latest available image tags
- Choose an appropriate image tag for your environment
- `Lite` means the Docker image **does not include** ASR models and UVR5 models. You can manually download the UVR5 models, while the program will automatically download the ASR models as needed
- The appropriate architecture image (amd64/arm64) will be automatically pulled during Docker Compose
- Docker Compose will mount **all files** in the current directory. Please switch to the project root directory and **pull the latest code** before using the Docker image
- Optionally, build the image locally using the provided Dockerfile for the most up-to-date changes