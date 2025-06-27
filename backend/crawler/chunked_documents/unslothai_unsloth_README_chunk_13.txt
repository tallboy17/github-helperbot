Repository: unslothai/unsloth
Language: Python
Stars: 40771
Forks: 3246
-----
`⚠️Only use Conda if you have it. If not, use Pip`. Select either `pytorch-cuda=11.8,12.1` for CUDA 11.8 or CUDA 12.1. We support `python=3.10,3.11,3.12`.
```bash
conda create --name unsloth_env \
python=3.11 \
pytorch-cuda=12.1 \
pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers \
-y
conda activate unsloth_env

pip install unsloth
```  
<details>
<summary>If you're looking to install Conda in a Linux environment, <a href="https://docs.anaconda.com/miniconda/">read here</a>, or run the below 🔽</summary>  
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
</details>