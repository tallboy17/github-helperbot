Repository: microsoft/autogen
Language: Python
Stars: 46193
Forks: 7005
-----
Create a group chat team with a web surfer agent and a user proxy agent
for web browsing tasks. You need to install [playwright](https://playwright.dev/python/docs/library).  
```python
# pip install -U autogen-agentchat autogen-ext[openai,web-surfer]
# playwright install
import asyncio
from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer

async def main() -> None:
model_client = OpenAIChatCompletionClient(model="gpt-4o")
# The web surfer will open a Chromium browser window to perform web browsing tasks.
web_surfer = MultimodalWebSurfer("web_surfer", model_client, headless=False, animate_actions=True)
# The user proxy agent is used to get user input after each step of the web surfer.
# NOTE: you can skip input by pressing Enter.
user_proxy = UserProxyAgent("user_proxy")
# The termination condition is set to end the conversation when the user types 'exit'.
termination = TextMentionTermination("exit", sources=["user_proxy"])
# Web surfer and user proxy take turns in a round-robin fashion.
team = RoundRobinGroupChat([web_surfer, user_proxy], termination_condition=termination)
try:
# Start the team and wait for it to terminate.
await Console(team.run_stream(task="Find information about AutoGen and write a short summary."))
finally:
await web_surfer.close()
await model_client.close()

asyncio.run(main())
```