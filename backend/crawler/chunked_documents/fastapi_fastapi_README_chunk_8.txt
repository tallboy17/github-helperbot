Repository: fastapi/fastapi
Language: Python
Stars: 86428
Forks: 7502
-----
Run the server with:  
<div class="termy">  
```console
$ fastapi dev main.py

╭────────── FastAPI CLI - Development mode ───────────╮
│                                                     │
│  Serving at: http://127.0.0.1:8000                  │
│                                                     │
│  API docs: http://127.0.0.1:8000/docs               │
│                                                     │
│  Running in development mode, for production use:   │
│                                                     │
│  fastapi run                                        │
│                                                     │
╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```  
</div>  
<details markdown="1">
<summary>About the command <code>fastapi dev main.py</code>...</summary>  
The command `fastapi dev` reads your `main.py` file, detects the **FastAPI** app in it, and starts a server using <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>.  
By default, `fastapi dev` will start with auto-reload enabled for local development.  
You can read more about it in the <a href="https://fastapi.tiangolo.com/fastapi-cli/" target="_blank">FastAPI CLI docs</a>.  
</details>