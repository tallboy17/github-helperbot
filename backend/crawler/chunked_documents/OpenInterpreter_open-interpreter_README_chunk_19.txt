Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
You can modify the `max_tokens` and `context_window` (in tokens) of locally running models.  
For local mode, smaller context windows will use less RAM, so we recommend trying a much shorter window (~1000) if it's failing / if it's slow. Make sure `max_tokens` is less than `context_window`.  
```shell
interpreter --local --max_tokens 1000 --context_window 3000
```