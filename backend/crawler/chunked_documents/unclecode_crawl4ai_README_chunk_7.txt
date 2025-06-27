Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
For basic web crawling and scraping tasks:  
```bash
pip install crawl4ai
crawl4ai-setup # Setup the browser
```  
By default, this will install the asynchronous version of Crawl4AI, using Playwright for web crawling.  
👉 **Note**: When you install Crawl4AI, the `crawl4ai-setup` should automatically install and set up Playwright. However, if you encounter any Playwright-related errors, you can manually install it using one of these methods:  
1. Through the command line:  
```bash
playwright install
```  
2. If the above doesn't work, try this more specific command:  
```bash
python -m playwright install chromium
```  
This second method has proven to be more reliable in some cases.  
---