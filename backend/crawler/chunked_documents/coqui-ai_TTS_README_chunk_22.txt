Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
- List the available speakers and choose a <speaker_id> among them:  
```
$ tts --model_name "<language>/<dataset>/<model_name>"  --list_speaker_idxs
```  
- Run the multi-speaker TTS model with the target speaker ID:  
```
$ tts --text "Text for TTS." --out_path output/path/speech.wav --model_name "<language>/<dataset>/<model_name>"  --speaker_idx <speaker_id>
```  
- Run your own multi-speaker TTS model:  
```
$ tts --text "Text for TTS" --out_path output/path/speech.wav --model_path path/to/model.pth --config_path path/to/config.json --speakers_file_path path/to/speaker.json --speaker_idx <speaker_id>
```