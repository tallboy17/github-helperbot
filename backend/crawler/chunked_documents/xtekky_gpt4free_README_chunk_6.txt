Repository: xtekky/gpt4free
Language: Python
Stars: 64472
Forks: 13656
-----
1. **Install Docker:** [Download and install Docker](https://docs.docker.com/get-docker/).
2. **Set Up Directories:** Before running the container, make sure the necessary data directories exist or can be created. For example, you can create and set ownership on these directories by running:
```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_media
sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_media
```
3. **Run the Docker Container:** Use the following commands to pull the latest image and start the container (Only x64):
```bash
docker pull hlohaus789/g4f
docker run -p 8080:8080 -p 7900:7900 \
--shm-size="2g" \
-v ${PWD}/har_and_cookies:/app/har_and_cookies \
-v ${PWD}/generated_media:/app/generated_media \
hlohaus789/g4f:latest
```  
4. **Running the Slim Docker Image:** And use the following commands to run the Slim Docker image. This command also updates the `g4f` package at startup and installs any additional dependencies: (x64 and arm64)
```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_media
chown -R 1000:1000 ${PWD}/har_and_cookies ${PWD}/generated_media
docker run \
-p 1337:8080 -p 8080:8080 \
-v ${PWD}/har_and_cookies:/app/har_and_cookies \
-v ${PWD}/generated_media:/app/generated_media \
hlohaus789/g4f:latest-slim
```  
5. **Access the Client Interface:**
- **To use the included client, navigate to:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
- **Or set the API base for your client to:** [http://localhost:8080/v1](http://localhost:8080/v1)  
6. **(Optional) Provider Login:**
If required, you can access the container's desktop here: http://localhost:7900/?autoconnect=1&resize=scale&password=secret for provider login purposes.  
---