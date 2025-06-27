Repository: coqui-ai/TTS
Language: Python
Stars: 40828
Forks: 5275
-----
For Fairseq models, use the following name format: `tts_models/<lang-iso_code>/fairseq/vits`.
You can find the language ISO codes [here](https://dl.fbaipublicfiles.com/mms/tts/all-tts-languages.html)
and learn about the Fairseq models [here](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).  
```python
# TTS with on the fly voice conversion
api = TTS("tts_models/deu/fairseq/vits")
api.tts_with_vc_to_file(
"Wie sage ich auf Italienisch, dass ich dich liebe?",
speaker_wav="target/speaker.wav",
file_path="output.wav"
)
```