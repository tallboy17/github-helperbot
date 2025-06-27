Repository: fastapi/fastapi
Language: Python
Stars: 86428
Forks: 7502
-----
When you install FastAPI with `pip install "fastapi[standard]"` it comes with the `standard` group of optional dependencies:  
Used by Pydantic:  
* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - for email validation.  
Used by Starlette:  
* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Required if you want to use the `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Required if you want to use the default template configuration.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Required if you want to support form <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, with `request.form()`.  
Used by FastAPI / Starlette:  
* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - for the server that loads and serves your application. This includes `uvicorn[standard]`, which includes some dependencies (e.g. `uvloop`) needed for high performance serving.
* `fastapi-cli` - to provide the `fastapi` command.