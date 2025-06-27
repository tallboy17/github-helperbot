Repository: OpenBB-finance/OpenBB
Language: Python
Stars: 42040
Forks: 3786
-----
<br />
<img src="https://github.com/OpenBB-finance/OpenBB/blob/develop/images/platform-light.svg?raw=true#gh-light-mode-only" alt="OpenBB Platform logo" width="600">
<img src="https://github.com/OpenBB-finance/OpenBB/blob/develop/images/platform-dark.svg?raw=true#gh-dark-mode-only" alt="OpenBB Platform logo" width="600">
<br />
<br />  
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/openbb_finance.svg?style=social&label=Follow%20%40openbb_finance)](https://x.com/openbb_finance)
[![Discord Shield](https://img.shields.io/discord/831165782750789672)](https://discord.com/invite/xPHTuHCmuV)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/OpenBB-finance/OpenBB)
<a href="https://codespaces.new/OpenBB-finance/OpenBB">
<img src="https://github.com/codespaces/badge.svg" height="20" />
</a>
<a target="_blank" href="https://colab.research.google.com/github/OpenBB-finance/OpenBB/blob/develop/examples/googleColab.ipynb">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
[![PyPI](https://img.shields.io/pypi/v/openbb?color=blue&label=PyPI%20Package)](https://pypi.org/project/openbb/)  
The first financial Platform that is open source.  
The OpenBB Platform offers access to equity, options, crypto, forex, macro economy, fixed income, and more while also offering a broad range of extensions to enhance the user experience according to their needs.  
Get started with: `pip install openbb`  
```python
from openbb import obb
output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
```  
You can sign up to the [OpenBB Hub](https://my.openbb.co/login) to get the most out of the OpenBB ecosystem.  
Data integrations available can be found here: <https://docs.openbb.co/platform/reference>  
---