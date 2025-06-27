Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
![inpainting-stable2](assets/stable-inpainting/merged-leopards.png)  
[Download the SD 2.0-inpainting checkpoint](https://huggingface.co/stabilityai/stable-diffusion-2-inpainting) and run  
```
python scripts/gradio/inpainting.py configs/stable-diffusion/v2-inpainting-inference.yaml <path-to-checkpoint>
```  
or  
```
streamlit run scripts/streamlit/inpainting.py -- configs/stable-diffusion/v2-inpainting-inference.yaml <path-to-checkpoint>
```  
for a Gradio or Streamlit demo of the inpainting model.
This scripts adds invisible watermarking to the demo in the [RunwayML](https://github.com/runwayml/stable-diffusion/blob/main/scripts/inpaint_st.py) repository, but both should work interchangeably with the checkpoints/configs.