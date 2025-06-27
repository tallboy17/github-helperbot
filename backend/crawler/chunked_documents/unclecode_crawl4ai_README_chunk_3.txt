Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
1. Install Crawl4AI:
```bash
# Install the package
pip install -U crawl4ai

# For pre release versions
pip install crawl4ai --pre

# Run post-installation setup
crawl4ai-setup

# Verify your installation
crawl4ai-doctor
```  
If you encounter any browser-related issues, you can install them manually:
```bash
python -m playwright install --with-deps chromium
```  
2. Run a simple web crawl with Python:
```python
import asyncio
from crawl4ai import *

async def main():
async with AsyncWebCrawler() as crawler:
result = await crawler.arun(
url="https://www.nbcnews.com/business",
)
print(result.markdown)

if __name__ == "__main__":
asyncio.run(main())
```  
3. Or use the new command-line interface:
```bash
# Basic crawl with markdown output
crwl https://www.nbcnews.com/business -o markdown

# Deep crawl with BFS strategy, max 10 pages
crwl https://docs.crawl4ai.com --deep-crawl bfs --max-pages 10

# Use LLM extraction with a specific question
crwl https://www.example.com/products -q "Extract all product prices"
```