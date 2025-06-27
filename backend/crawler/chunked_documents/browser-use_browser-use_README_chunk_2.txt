Repository: browser-use/browser-use
Language: Python
Stars: 63562
Forks: 7208
-----
With pip (Python>=3.11):  
```bash
pip install browser-use
```  
For memory functionality (requires Python<3.13 due to PyTorch compatibility):  
```bash
pip install "browser-use[memory]"
```  
Install the browser:
```bash
playwright install chromium --with-deps --no-shell
```  
Spin up your agent:  
```python
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
agent = Agent(
task="Compare the price of gpt-4o and DeepSeek-V3",
llm=ChatOpenAI(model="gpt-4o"),
)
await agent.run()

asyncio.run(main())
```  
Add your API keys for the provider you want to use to your `.env` file.  
```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
GOOGLE_API_KEY=
DEEPSEEK_API_KEY=
GROK_API_KEY=
NOVITA_API_KEY=
```  
For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).