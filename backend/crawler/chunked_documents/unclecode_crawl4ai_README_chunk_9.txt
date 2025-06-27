Repository: unclecode/crawl4ai
Language: Python
Stars: 45928
Forks: 4368
-----
For contributors who plan to modify the source code:  
```bash
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai
pip install -e .                    # Basic installation in editable mode
```  
Install optional features:  
```bash
pip install -e ".[torch]"           # With PyTorch features
pip install -e ".[transformer]"     # With Transformer features
pip install -e ".[cosine]"          # With cosine similarity features
pip install -e ".[sync]"            # With synchronous crawling (Selenium)
pip install -e ".[all]"             # Install all optional features
```  
</details>  
<details>
<summary>🐳 <strong>Docker Deployment</strong></summary>  
> 🚀 **Now Available!** Our completely redesigned Docker implementation is here! This new solution makes deployment more efficient and seamless than ever.