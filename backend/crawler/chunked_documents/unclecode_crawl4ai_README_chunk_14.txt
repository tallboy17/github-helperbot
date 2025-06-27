Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
- **🌎 World-aware Crawling**: Set geolocation, language, and timezone for authentic locale-specific content:
```python
crun_cfg = CrawlerRunConfig(
url="https://browserleaks.com/geo",          # test page that shows your location
locale="en-US",                              # Accept-Language & UI locale
timezone_id="America/Los_Angeles",           # JS Date()/Intl timezone
geolocation=GeolocationConfig(                 # override GPS coords
latitude=34.0522,
longitude=-118.2437,
accuracy=10.0,
)
)
```  
- **📊 Table-to-DataFrame Extraction**: Extract HTML tables directly to CSV or pandas DataFrames:
```python
crawler = AsyncWebCrawler(config=browser_config)
await crawler.start()

try:
# Set up scraping parameters
crawl_config = CrawlerRunConfig(
table_score_threshold=8,  # Strict table detection
)

# Execute market data extraction
results: List[CrawlResult] = await crawler.arun(
url="https://coinmarketcap.com/?page=1", config=crawl_config
)

# Process results
raw_df = pd.DataFrame()
for result in results:
if result.success and result.media["tables"]:
raw_df = pd.DataFrame(
result.media["tables"][0]["rows"],
columns=result.media["tables"][0]["headers"],
)
break
print(raw_df.head())

finally:
await crawler.stop()
```  
- **🚀 Browser Pooling**: Pages launch hot with pre-warmed browser instances for lower latency and memory usage  
- **🕸️ Network and Console Capture**: Full traffic logs and MHTML snapshots for debugging:
```python
crawler_config = CrawlerRunConfig(
capture_network=True,
capture_console=True,
mhtml=True
)
```  
- **🔌 MCP Integration**: Connect to AI tools like Claude Code through the Model Context Protocol
```bash
# Add Crawl4AI to Claude Code
claude mcp add --transport sse c4ai-sse http://localhost:11235/mcp/sse
```  
- **🖥️ Interactive Playground**: Test configurations and generate API requests with the built-in web interface at `http://localhost:11235//playground`  
- **🐳 Revamped Docker Deployment**: Streamlined multi-architecture Docker image with improved resource efficiency  
- **📱 Multi-stage Build System**: Optimized Dockerfile with platform-specific performance enhancements  
Read the full details in our [0.6.0 Release Notes](https://docs.crawl4ai.com/blog/releases/0.6.0.html) or check the [CHANGELOG](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md).