Repository: OpenInterpreter/open-interpreter
Language: Python
Stars: 59703
Forks: 5081
-----
Open Interpreter can use OpenAI-compatible server to run models locally. (LM Studio, jan.ai, ollama etc)  
Simply run `interpreter` with the api_base URL of your inference server (for LM studio it is `http://localhost:1234/v1` by default):  
```shell
interpreter --api_base "http://localhost:1234/v1" --api_key "fake_key"
```  
Alternatively you can use Llamafile without installing any third party software just by running  
```shell
interpreter --local
```  
for a more detailed guide check out [this video by Mike Bird](https://www.youtube.com/watch?v=CEs51hGWuGU?si=cN7f6QhfT4edfG5H)  
**How to run LM Studio in the background.**  
1. Download [https://lmstudio.ai/](https://lmstudio.ai/) then start it.
2. Select a model then click **↓ Download**.
3. Click the **↔️** button on the left (below 💬).
4. Select your model at the top, then click **Start Server**.  
Once the server is running, you can begin your conversation with Open Interpreter.  
> **Note:** Local mode sets your `context_window` to 3000, and your `max_tokens` to 1000. If your model has different requirements, set these parameters manually (see below).