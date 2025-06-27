Repository: fastapi/fastapi
Language: Python
Stars: 86428
Forks: 7502
-----
Open your browser at <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.  
You will see the JSON response as:  
```JSON
{"item_id": 5, "q": "somequery"}
```  
You already created an API that:  
* Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
* Both _paths_ take `GET` <em>operations</em> (also known as HTTP _methods_).
* The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
* The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.