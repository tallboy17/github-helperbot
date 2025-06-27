Repository: openai/whisper
Language: Python
Stars: 83554
Forks: 10152
-----
![Approach](https://raw.githubusercontent.com/openai/whisper/main/approach.png)  
A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.