Repository: pallets/flask
Language: Python
Stars: 69788
Forks: 16471
-----
```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
return "Hello, World!"
```  
```
$ flask run
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```