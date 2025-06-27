Repository: lm-sys/FastChat
Language: Python
Stars: 38746
Forks: 4720
-----
1. Clone this repository and navigate to the FastChat folder
```bash
git clone https://github.com/lm-sys/FastChat.git
cd FastChat
```  
If you are running on Mac:
```bash
brew install rust cmake
```  
2. Install Package
```bash
pip3 install --upgrade pip  # enable PEP 660 support
pip3 install -e ".[model_worker,webui]"
```