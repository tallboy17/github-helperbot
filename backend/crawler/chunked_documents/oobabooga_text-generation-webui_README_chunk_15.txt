Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
Models should be placed in the folder `text-generation-webui/user_data/models`. They are usually downloaded from [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads&search=gguf).  
To check if a GGUF model will fit in your hardware before downloading it, you can use this tool I created:  
[Accurate GGUF VRAM Calculator](https://huggingface.co/spaces/oobabooga/accurate-gguf-vram-calculator)  
* GGUF models are a single file and should be placed directly into `user_data/models`. Example:  
```
text-generation-webui
└── user_data
└── models
└── llama-2-13b-chat.Q4_K_M.gguf
```  
* The remaining model types (like 16-bit Transformers models and EXL2 models) are made of several files and must be placed in a subfolder. Example:  
```
text-generation-webui
└── user_data
└── models
└── lmsys_vicuna-33b-v1.3
├── config.json
├── generation_config.json
├── pytorch_model-00001-of-00007.bin
├── pytorch_model-00002-of-00007.bin
├── pytorch_model-00003-of-00007.bin
├── pytorch_model-00004-of-00007.bin
├── pytorch_model-00005-of-00007.bin
├── pytorch_model-00006-of-00007.bin
├── pytorch_model-00007-of-00007.bin
├── pytorch_model.bin.index.json
├── special_tokens_map.json
├── tokenizer_config.json
└── tokenizer.model
```  
In both cases, you can use the "Model" tab of the UI to download the model from Hugging Face automatically. It is also possible to download it via the command-line with:  
```
python download-model.py organization/model
```  
Run `python download-model.py --help` to see all the options.