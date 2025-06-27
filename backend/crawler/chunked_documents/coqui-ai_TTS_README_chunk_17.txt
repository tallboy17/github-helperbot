Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
Converting the voice in `source_wav` to the voice of `target_wav`  
```python
tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False).to("cuda")
tts.voice_conversion_to_file(source_wav="my/source.wav", target_wav="my/target.wav", file_path="output.wav")
```