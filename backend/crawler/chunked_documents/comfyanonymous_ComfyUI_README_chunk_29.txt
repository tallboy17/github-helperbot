Repository: comfyanonymous/ComfyUI
Language: Python
Stars: 80094
Forks: 8865
-----
Use ```--preview-method auto``` to enable previews.  
The default installation includes a fast latent preview method that's low-resolution. To enable higher-quality previews with [TAESD](https://github.com/madebyollin/taesd), download the [taesd_decoder.pth, taesdxl_decoder.pth, taesd3_decoder.pth and taef1_decoder.pth](https://github.com/madebyollin/taesd/) and place them in the `models/vae_approx` folder. Once they're installed, restart ComfyUI and launch it with `--preview-method taesd` to enable high-quality previews.