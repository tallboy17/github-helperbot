Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
- List provided models:  
```
$ tts --list_models
```  
- Get model info (for both tts_models and vocoder_models):  
- Query by type/name:
The model_info_by_name uses the name as it from the --list_models.
```
$ tts --model_info_by_name "<model_type>/<language>/<dataset>/<model_name>"
```
For example:
```
$ tts --model_info_by_name tts_models/tr/common-voice/glow-tts
$ tts --model_info_by_name vocoder_models/en/ljspeech/hifigan_v2
```
- Query by type/idx:
The model_query_idx uses the corresponding idx from --list_models.  
```
$ tts --model_info_by_idx "<model_type>/<model_query_idx>"
```  
For example:  
```
$ tts --model_info_by_idx tts_models/3
```  
- Query info for model info by full name:
```
$ tts --model_info_by_name "<model_type>/<language>/<dataset>/<model_name>"
```  
- Run TTS with default models:  
```
$ tts --text "Text for TTS" --out_path output/path/speech.wav
```  
- Run TTS and pipe out the generated TTS wav file data:  
```
$ tts --text "Text for TTS" --pipe_out --out_path output/path/speech.wav | aplay
```  
- Run a TTS model with its default vocoder model:  
```
$ tts --text "Text for TTS" --model_name "<model_type>/<language>/<dataset>/<model_name>" --out_path output/path/speech.wav
```  
For example:  
```
$ tts --text "Text for TTS" --model_name "tts_models/en/ljspeech/glow-tts" --out_path output/path/speech.wav
```  
- Run with specific TTS and vocoder models from the list:  
```
$ tts --text "Text for TTS" --model_name "<model_type>/<language>/<dataset>/<model_name>" --vocoder_name "<model_type>/<language>/<dataset>/<model_name>" --out_path output/path/speech.wav
```  
For example:  
```
$ tts --text "Text for TTS" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path output/path/speech.wav
```  
- Run your own TTS model (Using Griffin-Lim Vocoder):  
```
$ tts --text "Text for TTS" --model_path path/to/model.pth --config_path path/to/config.json --out_path output/path/speech.wav
```  
- Run your own TTS and Vocoder models:  
```
$ tts --text "Text for TTS" --model_path path/to/model.pth --config_path path/to/config.json --out_path output/path/speech.wav
--vocoder_path path/to/vocoder.pth --vocoder_config_path path/to/vocoder_config.json
```