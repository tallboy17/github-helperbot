Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
The generator update enables Open Interpreter to be controlled via HTTP REST endpoints:  
```python
# server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from interpreter import interpreter

app = FastAPI()

@app.get("/chat")
def chat_endpoint(message: str):
def event_stream():
for result in interpreter.chat(message, stream=True):
yield f"data: {result}\n\n"

return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
return interpreter.messages
```  
```shell
pip install fastapi uvicorn
uvicorn server:app --reload
```  
You can also start a server identical to the one above by simply running `interpreter.server()`.