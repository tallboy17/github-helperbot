Repository: microsoft/markitdown
Language: Python
Stars: 59294
Forks: 3083
-----
MarkItDown also supports 3rd-party plugins. Plugins are disabled by default. To list installed plugins:  
```bash
markitdown --list-plugins
```  
To enable plugins use:  
```bash
markitdown --use-plugins path-to-file.pdf
```  
To find available plugins, search GitHub for the hashtag `#markitdown-plugin`. To develop a plugin, see `packages/markitdown-sample-plugin`.