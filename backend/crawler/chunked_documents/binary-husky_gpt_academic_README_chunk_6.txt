Repository: binary-husky/gpt_academic
Language: Python
Stars: 68796
Forks: 8352
-----
现在已可以通过UI中的`界面外观`菜单中的`自定义菜单`添加新的便捷按钮。如果需要在代码中定义，请使用任意文本编辑器打开`core_functional.py`，添加如下条目即可：  
```python
"超级英译中": {
# 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
"Prefix": "请翻译把下面一段内容成中文，然后用一个markdown表格逐一解释文中出现的专有名词：\n\n",

# 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来。
"Suffix": "",
},
```  
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226899272-477c2134-ed71-4326-810c-29891fe4a508.png" width="500" >
</div>