Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
This way, you can clone voices by using any model in 🐸TTS.  
```python

tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_with_vc_to_file(
"Wie sage ich auf Italienisch, dass ich dich liebe?",
speaker_wav="target/speaker.wav",
file_path="output.wav"
)
```