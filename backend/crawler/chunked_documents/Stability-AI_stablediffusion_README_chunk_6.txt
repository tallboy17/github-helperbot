Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
Stable Diffusion v2 refers to a specific configuration of the model
architecture that uses a downsampling-factor 8 autoencoder with an 865M UNet
and OpenCLIP ViT-H/14 text encoder for the diffusion model. The _SD 2-v_ model produces 768x768 px outputs.  
Evaluations with different classifier-free guidance scales (1.5, 2.0, 3.0, 4.0,
5.0, 6.0, 7.0, 8.0) and 50 DDIM sampling steps show the relative improvements of the checkpoints:  
![sd evaluation results](assets/model-variants.jpg)