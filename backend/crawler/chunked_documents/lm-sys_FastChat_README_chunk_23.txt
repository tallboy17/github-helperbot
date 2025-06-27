Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
Currently, Chatbot Arena is powered by FastChat. Here is how you can launch an instance of Chatbot Arena locally.  
FastChat supports popular API-based models such as OpenAI, Anthropic, Gemini, Mistral and more. To add a custom API, please refer to the model support [doc](./docs/model_support.md). Below we take OpenAI models as an example.  
Create a JSON configuration file `api_endpoint.json` with the api endpoints of the models you want to serve, for example:
```
{
"gpt-4o-2024-05-13": {
"model_name": "gpt-4o-2024-05-13",
"api_base": "https://api.openai.com/v1",
"api_type": "openai",
"api_key": [Insert API Key],
"anony_only": false
}
}
```
For Anthropic models, specify `"api_type": "anthropic_message"` with your Anthropic key. Similarly, for gemini model, specify `"api_type": "gemini"`. More details can be found in [api_provider.py](https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/api_provider.py).  
To serve your own model using local gpus, follow the instructions in [Serving with Web GUI](#serving-with-web-gui).  
Now you're ready to launch the server:
```
python3 -m fastchat.serve.gradio_web_server_multi --register-api-endpoint-file api_endpoint.json
```