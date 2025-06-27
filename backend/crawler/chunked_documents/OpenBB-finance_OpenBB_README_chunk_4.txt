Repository: OpenBB-finance/OpenBB
Language: Python
Stars: 42040
Forks: 3786
-----
- Install the packages.  
```sh
pip install "openbb[all]"
```  
- Start the API server over localhost.  
```sh
openbb-api
```  
This will launch a FastAPI server, via Uvicorn, at `127.0.0.1:6900`.  
You can check that it works by going to <http://127.0.0.1:6900>.