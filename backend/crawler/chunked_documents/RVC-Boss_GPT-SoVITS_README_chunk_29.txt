Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
New Features:  
1. Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed.
[more details](<https://github.com/RVC-Boss/GPT-SoVITS/wiki/GPT%E2%80%90SoVITS%E2%80%90features-(%E5%90%84%E7%89%88%E6%9C%AC%E7%89%B9%E6%80%A7)>)  
2.v1/v2 and the v2Pro series share the same characteristics, while v3/v4 have similar features. For training sets with average audio quality, v1/v2/v2Pro can deliver decent results, but v3/v4 cannot. Additionally, the synthesized tone and timebre of v3/v4 lean more toward the reference audio rather than the overall training set.  
Use v2Pro from v1/v2/v3/v4 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v2Pro pretrained models (v2Pro/s2Dv2Pro.pth, v2Pro/s2Gv2Pro.pth, v2Pro/s2Dv2ProPlus.pth, v2Pro/s2Gv2ProPlus.pth, and sv/pretrained_eres2netv2w24s4ep4.ckpt) from [huggingface](https://huggingface.co/lj1995/GPT-SoVITS/tree/main) and put them into `GPT_SoVITS/pretrained_models`.