Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
```bash
python3 -m fastchat.serve.model_worker --model-path lmsys/vicuna-7b-v1.5
```
Wait until the process finishes loading the model and you see "Uvicorn running on ...". The model worker will register itself to the controller .  
To ensure that your model worker is connected to your controller properly, send a test message using the following command:
```bash
python3 -m fastchat.serve.test_message --model-name vicuna-7b-v1.5
```
You will see a short output.