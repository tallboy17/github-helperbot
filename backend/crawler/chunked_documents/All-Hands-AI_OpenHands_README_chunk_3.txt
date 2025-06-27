Repository: All-Hands-AI/OpenHands
Language: Python
Stars: 58667
Forks: 6754
-----
OpenHands can also run on your local system using Docker.
See the [Running OpenHands](https://docs.all-hands.dev/usage/installation) guide for
system requirements and more information.  
> [!WARNING]
> On a public network? See our [Hardened Docker Installation Guide](https://docs.all-hands.dev/usage/runtimes/docker#hardened-docker-installation)
> to secure your deployment by restricting network binding and implementing additional security measures.  
```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.44-nikolaik

docker run -it --rm --pull=always \
-e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.44-nikolaik \
-e LOG_ALL_EVENTS=true \
-v /var/run/docker.sock:/var/run/docker.sock \
-v ~/.openhands:/.openhands \
-p 3000:3000 \
--add-host host.docker.internal:host-gateway \
--name openhands-app \
docker.all-hands.dev/all-hands-ai/openhands:0.44
```  
> **Note**: If you used OpenHands before version 0.44, you may want to run `mv ~/.openhands-state ~/.openhands` to migrate your conversation history to the new location.  
You'll find OpenHands running at [http://localhost:3000](http://localhost:3000)!  
When you open the application, you'll be asked to choose an LLM provider and add an API key.
[Anthropic's Claude Sonnet 4](https://www.anthropic.com/api) (`anthropic/claude-sonnet-4-20250514`)
works best, but you have [many options](https://docs.all-hands.dev/usage/llms).