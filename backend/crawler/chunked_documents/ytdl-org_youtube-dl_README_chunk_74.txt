Repository: ytdl-org/youtube-dl
Language: Python
Stars: 136117
Forks: 10373
-----
When processing complex JSON, as often returned by site API requests or stashed in web pages for "hydration", you can use the `traverse_obj()` utility function to handle multiple fallback values and to ensure the expected type of metadata items. The function's docstring defines how the function works: also review usage in the codebase for more examples.  
In this example, a text `description`, or `None`, is pulled from the `.result.video[0].summary` member of the parsed JSON `response`, if available.  
```python
description = traverse_obj(response, ('result', 'video', 0, 'summary', T(compat_str)))
```
`T(...)` is a shorthand for a set literal; if you hate people who still run Python 2.6, `T(type_or_transformation)` could be written as a set literal `{type_or_transformation}`.  
Some extractors use the older and less capable `try_get()` function in the same way.  
```python
description = try_get(response, lambda x: x['result']['video'][0]['summary'], compat_str)
```