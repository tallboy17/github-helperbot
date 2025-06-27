Repository: CorentinJ/Real-Time-Voice-Cloning
Language: Python
Stars: 54536
Forks: 9009
-----
This repository is an implementation of [Transfer Learning from Speaker Verification to
Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf) (SV2TTS) with a vocoder that works in real-time. This was my [master's thesis](https://matheo.uliege.be/handle/2268.2/6801).  
SV2TTS is a deep learning framework in three stages. In the first stage, one creates a digital representation of a voice from a few seconds of audio. In the second and third stages, this representation is used as reference to generate speech given arbitrary text.  
**Video demonstration** (click the picture):  
[![Toolbox demo](https://i.imgur.com/8lFUlgz.png)](https://www.youtube.com/watch?v=-O_hYhToKoA)