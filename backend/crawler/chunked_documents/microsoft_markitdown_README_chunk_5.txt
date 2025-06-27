Repository: microsoft/markitdown
Language: Python
Stars: 59294
Forks: 3083
-----
```bash
markitdown path-to-file.pdf > document.md
```  
Or use `-o` to specify the output file:  
```bash
markitdown path-to-file.pdf -o document.md
```  
You can also pipe content:  
```bash
cat path-to-file.pdf | markitdown
```