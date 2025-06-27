Repository: abi/screenshot-to-code
Language: Python
Stars: 70202
Forks: 8668
-----
The app has a React/Vite frontend and a FastAPI backend.  
Keys needed:  
- [OpenAI API key with access to GPT-4](https://github.com/abi/screenshot-to-code/blob/main/Troubleshooting.md) or Anthropic key (optional)
- Both are recommended so you can compare results from both Claude and GPT4o  
If you'd like to run the app with Ollama open source models (not recommended due to poor quality results), [follow this comment](https://github.com/abi/screenshot-to-code/issues/354#issuecomment-2435479853).  
Run the backend (I use Poetry for package management - `pip install --upgrade poetry` if you don't have it):  
```bash
cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
echo "ANTHROPIC_API_KEY=your-key" > .env
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001
```  
You can also set up the keys using the settings dialog on the front-end (click the gear icon after loading the frontend).  
Run the frontend:  
```bash
cd frontend
yarn
yarn dev
```  
Open http://localhost:5173 to use the app.  
If you prefer to run the backend on a different port, update VITE_WS_BACKEND_URL in `frontend/.env.local`  
For debugging purposes, if you don't want to waste GPT4-Vision credits, you can run the backend in mock mode (which streams a pre-recorded response):  
```bash
MOCK=true poetry run uvicorn main:app --reload --port 7001
```