Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
You can check the project structure in the directory [https://github.com/unclecode/crawl4ai/docs/examples](docs/examples). Over there, you can find a variety of examples; here, some popular examples are shared.  
<details>
<summary>📝 <strong>Heuristic Markdown Generation with Clean and Fit Markdown</strong></summary>  
```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
browser_config = BrowserConfig(
headless=True,
verbose=True,
)
run_config = CrawlerRunConfig(
cache_mode=CacheMode.ENABLED,
markdown_generator=DefaultMarkdownGenerator(
content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed", min_word_threshold=0)
),
# markdown_generator=DefaultMarkdownGenerator(
#     content_filter=BM25ContentFilter(user_query="WHEN_WE_FOCUS_BASED_ON_A_USER_QUERY", bm25_threshold=1.0)
# ),
)

async with AsyncWebCrawler(config=browser_config) as crawler:
result = await crawler.arun(
url="https://docs.micronaut.io/4.7.6/guide/",
config=run_config
)
print(len(result.markdown.raw_markdown))
print(len(result.markdown.fit_markdown))

if __name__ == "__main__":
asyncio.run(main())
```  
</details>  
<details>
<summary>🖥️ <strong>Executing JavaScript & Extract Structured Data without LLMs</strong></summary>  
```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json

async def main():
schema = {
"name": "KidoCode Courses",
"baseSelector": "section.charge-methodology .w-tab-content > div",
"fields": [
{
"name": "section_title",
"selector": "h3.heading-50",
"type": "text",
},
{
"name": "section_description",
"selector": ".charge-content",
"type": "text",
},
{
"name": "course_name",
"selector": ".text-block-93",
"type": "text",
},
{
"name": "course_description",
"selector": ".course-content-text",
"type": "text",
},
{
"name": "course_icon",
"selector": ".image-92",
"type": "attribute",
"attribute": "src"
}
}
}

extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

browser_config = BrowserConfig(
headless=False,
verbose=True
)
run_config = CrawlerRunConfig(
extraction_strategy=extraction_strategy,
js_code=["""(async () => {const tabs = document.querySelectorAll("section.charge-methodology .tabs-menu-3 > div");for(let tab of tabs) {tab.scrollIntoView();tab.click();await new Promise(r => setTimeout(r, 500));}})();"""],
cache_mode=CacheMode.BYPASS
)

async with AsyncWebCrawler(config=browser_config) as crawler:

result = await crawler.arun(
url="https://www.kidocode.com/degrees/technology",
config=run_config
)

companies = json.loads(result.extracted_content)
print(f"Successfully extracted {len(companies)} companies")
print(json.dumps(companies[0], indent=2))


if __name__ == "__main__":
asyncio.run(main())
```  
</details>  
<details>
<summary>📚 <strong>Extracting Structured Data with LLMs</strong></summary>  
```python
import os
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel, Field

class OpenAIModelFee(BaseModel):
model_name: str = Field(..., description="Name of the OpenAI model.")
input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
output_fee: str = Field(..., description="Fee for output token for the OpenAI model.")

async def main():
browser_config = BrowserConfig(verbose=True)
run_config = CrawlerRunConfig(
word_count_threshold=1,
extraction_strategy=LLMExtractionStrategy(
# Here you can use any provider that Litellm library supports, for instance: ollama/qwen2
# provider="ollama/qwen2", api_token="no-token",
llm_config = LLMConfig(provider="openai/gpt-4o", api_token=os.getenv('OPENAI_API_KEY')),
schema=OpenAIModelFee.schema(),
extraction_type="schema",
instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens.
Do not miss any models in the entire content. One extracted model JSON format should look like this:
{"model_name": "GPT-4", "input_fee": "US$10.00 / 1M tokens", "output_fee": "US$30.00 / 1M tokens"}."""
),
cache_mode=CacheMode.BYPASS,
)

async with AsyncWebCrawler(config=browser_config) as crawler:
result = await crawler.arun(
url='https://openai.com/api/pricing/',
config=run_config
)
print(result.extracted_content)

if __name__ == "__main__":
asyncio.run(main())
```  
</details>  
<details>
<summary>🤖 <strong>Using You own Browser with Custom User Profile</strong></summary>  
```python
import os, sys
from pathlib import Path
import asyncio, time
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def test_news_crawl():
# Create a persistent user data directory
user_data_dir = os.path.join(Path.home(), ".crawl4ai", "browser_profile")
os.makedirs(user_data_dir, exist_ok=True)

browser_config = BrowserConfig(
verbose=True,
headless=True,
user_data_dir=user_data_dir,
use_persistent_context=True,
)
run_config = CrawlerRunConfig(
cache_mode=CacheMode.BYPASS
)

async with AsyncWebCrawler(config=browser_config) as crawler:
url = "ADDRESS_OF_A_CHALLENGING_WEBSITE"

result = await crawler.arun(
url,
config=run_config,
magic=True,
)

print(f"Successfully crawled {url}")
print(f"Content length: {len(result.markdown)}")
```  
</details>