Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
**March 24, 2023**  
*Stable UnCLIP 2.1*  
- New stable diffusion finetune (_Stable unCLIP 2.1_, [Hugging Face](https://huggingface.co/stabilityai/)) at 768x768 resolution,  based on SD2.1-768. This model allows for image variations and mixing operations as described in [*Hierarchical Text-Conditional Image Generation with CLIP Latents*](https://arxiv.org/abs/2204.06125), and, thanks to its modularity, can be combined with other models such as [KARLO](https://github.com/kakaobrain/karlo). Comes in two variants: [*Stable unCLIP-L*](https://huggingface.co/stabilityai/stable-diffusion-2-1-unclip/blob/main/sd21-unclip-l.ckpt) and [*Stable unCLIP-H*](https://huggingface.co/stabilityai/stable-diffusion-2-1-unclip/blob/main/sd21-unclip-h.ckpt), which are conditioned on CLIP ViT-L and ViT-H image embeddings, respectively. Instructions are available [here](doc/UNCLIP.MD).  
- A public demo of SD-unCLIP is already available at [clipdrop.co/stable-diffusion-reimagine](https://clipdrop.co/stable-diffusion-reimagine)  
**December 7, 2022**  
*Version 2.1*  
- New stable diffusion model (_Stable Diffusion 2.1-v_, [Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-2-1)) at 768x768 resolution and (_Stable Diffusion 2.1-base_, [HuggingFace](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)) at 512x512 resolution, both based on the same number of parameters and architecture as 2.0 and fine-tuned on 2.0, on a less restrictive NSFW filtering of the [LAION-5B](https://laion.ai/blog/laion-5b/) dataset.
Per default, the attention operation of the model is evaluated at full precision when `xformers` is not installed. To enable fp16 (which can cause numerical instabilities with the vanilla attention module on the v2.1 model) , run your script with `ATTN_PRECISION=fp16 python <thescript.py>`  
**November 24, 2022**  
*Version 2.0*  
- New stable diffusion model (_Stable Diffusion 2.0-v_) at 768x768 resolution. Same number of parameters in the U-Net as 1.5, but uses [OpenCLIP-ViT/H](https://github.com/mlfoundations/open_clip) as the text encoder and is trained from scratch. _SD 2.0-v_ is a so-called [v-prediction](https://arxiv.org/abs/2202.00512) model.
- The above model is finetuned from _SD 2.0-base_, which was trained as a standard noise-prediction model on 512x512 images and is also made available.
- Added a [x4 upscaling latent text-guided diffusion model](#image-upscaling-with-stable-diffusion).
- New [depth-guided stable diffusion model](#depth-conditional-stable-diffusion), finetuned from _SD 2.0-base_. The model is conditioned on monocular depth estimates inferred via [MiDaS](https://github.com/isl-org/MiDaS) and can be used for structure-preserving img2img and shape-conditional synthesis.  
![d2i](assets/stable-samples/depth2img/depth2img01.png)
- A [text-guided inpainting model](#image-inpainting-with-stable-diffusion), finetuned from SD _2.0-base_.  
We follow the [original repository](https://github.com/CompVis/stable-diffusion) and provide basic inference scripts to sample from the models.  
________________
*The original Stable Diffusion model was created in a collaboration with [CompVis](https://arxiv.org/abs/2202.00512) and [RunwayML](https://runwayml.com/) and builds upon the work:*  
[**High-Resolution Image Synthesis with Latent Diffusion Models**](https://ommer-lab.com/research/latent-diffusion-models/)<br/>
[Robin Rombach](https://github.com/rromb)\*,
[Andreas Blattmann](https://github.com/ablattmann)\*,
[Dominik Lorenz](https://github.com/qp-qp)\,
[Patrick Esser](https://github.com/pesser),
[Björn Ommer](https://hci.iwr.uni-heidelberg.de/Staff/bommer)<br/>
_[CVPR '22 Oral](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) |
[GitHub](https://github.com/CompVis/latent-diffusion) | [arXiv](https://arxiv.org/abs/2112.10752) | [Project page](https://ommer-lab.com/research/latent-diffusion-models/)_  
and [many others](#shout-outs).  
Stable Diffusion is a latent text-to-image diffusion model.
________________________________