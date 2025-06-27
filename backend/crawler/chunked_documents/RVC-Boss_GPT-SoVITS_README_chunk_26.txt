Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
New Features:  
1. Support Korean and Cantonese  
2. An optimized text frontend  
3. Pre-trained model extended from 2k hours to 5k hours  
4. Improved synthesis quality for low-quality reference audio  
[more details](<https://github.com/RVC-Boss/GPT-SoVITS/wiki/GPT%E2%80%90SoVITS%E2%80%90v2%E2%80%90features-(%E6%96%B0%E7%89%B9%E6%80%A7)>)  
Use v2 from v1 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v2 pretrained models from [huggingface](https://huggingface.co/lj1995/GPT-SoVITS/tree/main/gsv-v2final-pretrained) and put them into `GPT_SoVITS/pretrained_models/gsv-v2final-pretrained`.  
Chinese v2 additional: [G2PWModel.zip(HF)](https://huggingface.co/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/G2PWModel.zip)| [G2PWModel.zip(ModelScope)](https://www.modelscope.cn/models/XXXXRT/GPT-SoVITS-Pretrained/resolve/master/G2PWModel.zip)(Download G2PW models, unzip and rename to `G2PWModel`, and then place them in `GPT_SoVITS/text`.)