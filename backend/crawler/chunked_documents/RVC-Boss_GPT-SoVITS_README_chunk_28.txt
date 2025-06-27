Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
New Features:  
1. Version 4 fixes the issue of metallic artifacts in Version 3 caused by non-integer multiple upsampling, and natively outputs 48k audio to prevent muffled sound (whereas Version 3 only natively outputs 24k audio). The author considers Version 4 a direct replacement for Version 3, though further testing is still needed.
[more details](<https://github.com/RVC-Boss/GPT-SoVITS/wiki/GPT%E2%80%90SoVITS%E2%80%90v3v4%E2%80%90features-(%E6%96%B0%E7%89%B9%E6%80%A7)>)  
Use v4 from v1/v2/v3 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v4 pretrained models (gsv-v4-pretrained/s2v4.ckpt, and gsv-v4-pretrained/vocoder.pth) from [huggingface](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) and put them into `GPT_SoVITS/pretrained_models`.