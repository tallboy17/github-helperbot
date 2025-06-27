Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
You can also try TTS without install with the docker image.
Simply run the following command and you will be able to run TTS without installing it.  
```bash
docker run --rm -it -p 5002:5002 --entrypoint /bin/bash ghcr.io/coqui-ai/tts-cpu
python3 TTS/server/server.py --list_models #To get the list of available models
python3 TTS/server/server.py --model_name tts_models/en/vctk/vits # To start a server
```  
You can then enjoy the TTS server [here](http://[::1]:5002/)
More details about the docker images (like GPU support) can be found [here](https://tts.readthedocs.io/en/latest/docker_images.html)