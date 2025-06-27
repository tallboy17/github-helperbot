Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
New Features:  
1. The timbre similarity is higher, requiring less training data to approximate the target speaker (the timbre similarity is significantly improved using the base model directly without fine-tuning).  
2. GPT model is more stable, with fewer repetitions and omissions, and it is easier to generate speech with richer emotional expression.  
[more details](<https://github.com/RVC-Boss/GPT-SoVITS/wiki/GPT%E2%80%90SoVITS%E2%80%90v3v4%E2%80%90features-(%E6%96%B0%E7%89%B9%E6%80%A7)>)  
Use v3 from v2 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v3 pretrained models (s1v3.ckpt, s2Gv3.pth and models--nvidia--bigvgan_v2_24khz_100band_256x folder) from [huggingface](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) and put them into `GPT_SoVITS/pretrained_models`.  
additional: for Audio Super Resolution model, you can read [how to download](./tools/AP_BWE_main/24kto48k/readme.txt)