Repository: RVC-Boss/GPT-SoVITS
Language: Python
Stars: 47839
Forks: 5265
-----
**Note: The models trained with GPUs on Macs result in significantly lower quality compared to those trained on other devices, so we are temporarily using CPUs instead.**  
Install the program by running the following commands:  
```bash
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits
bash install.sh --device <MPS|CPU> --source <HF|HF-Mirror|ModelScope> [--download-uvr5]
```