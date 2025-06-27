Repository: abi/screenshot-to-code
Language: Python
Stars: 70202
Forks: 8668
-----
If you have Docker installed on your system, in the root directory, run:  
```bash
echo "OPENAI_API_KEY=sk-your-key" > .env
docker-compose up -d --build
```  
The app will be up and running at http://localhost:5173. Note that you can't develop the application with this setup as the file changes won't trigger a rebuild.