Repository: openai/whisper
Language: Python
Stars: 83554
Forks: 10152
-----
The following command will transcribe speech in audio files, using the `turbo` model:  
whisper audio.flac audio.mp3 audio.wav --model turbo  
The default setting (which selects the `turbo` model) works well for transcribing English. To transcribe an audio file containing non-English speech, you can specify the language using the `--language` option:  
whisper japanese.wav --language Japanese  
Adding `--task translate` will translate the speech into English:  
whisper japanese.wav --language Japanese --task translate  
Run the following to view all available options:  
whisper --help  
See [tokenizer.py](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py) for the list of all available languages.