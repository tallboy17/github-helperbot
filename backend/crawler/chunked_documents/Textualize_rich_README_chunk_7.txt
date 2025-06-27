Repository: Textualize/rich
Language: Python
Stars: 52460
Forks: 1845
-----
Rich has an [inspect](https://rich.readthedocs.io/en/latest/reference/init.html?highlight=inspect#rich.inspect) function which can produce a report on any Python object, such as class, instance, or builtin.  
```python
>>> my_list = ["foo", "bar"]
>>> from rich import inspect
>>> inspect(my_list, methods=True)
```  
![Log](https://github.com/textualize/rich/raw/master/imgs/inspect.png)  
See the [inspect docs](https://rich.readthedocs.io/en/latest/reference/init.html#rich.inspect) for details.