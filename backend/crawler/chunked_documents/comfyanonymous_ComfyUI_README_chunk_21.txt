Repository: comfyanonymous/ComfyUI
Language: Python
Stars: 80094
Forks: 8865
-----
You can install ComfyUI in Apple Mac silicon (M1 or M2) with any recent macOS version.  
1. Install pytorch nightly. For instructions, read the [Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/) Apple Developer guide (make sure to install the latest pytorch nightly).
1. Follow the [ComfyUI manual installation](#manual-install-windows-linux) instructions for Windows and Linux.
1. Install the ComfyUI [dependencies](#dependencies). If you have another Stable Diffusion UI [you might be able to reuse the dependencies](#i-already-have-another-ui-for-stable-diffusion-installed-do-i-really-have-to-install-all-of-these-dependencies).
1. Launch ComfyUI by running `python main.py`  
> **Note**: Remember to add your models, VAE, LoRAs etc. to the corresponding Comfy folders, as discussed in [ComfyUI manual installation](#manual-install-windows-linux).