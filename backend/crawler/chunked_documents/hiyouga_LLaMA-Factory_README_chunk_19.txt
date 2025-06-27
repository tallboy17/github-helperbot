Repository: hiyouga/LLaMA-Factory
Language: Python
Stars: 52604
Forks: 6439
-----
You need to manually install the GPU version of PyTorch on the Windows platform. Please refer to the [official website](https://pytorch.org/get-started/locally/) and the following command to install PyTorch with CUDA support:  
```bash
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
python -c "import torch; print(torch.cuda.is_available())"
```  
If you see `True` then you have successfully installed PyTorch with CUDA support.  
Try `dataloader_num_workers: 0` if you encounter `Can't pickle local object` error.