Repository: Stability-AI/stablediffusion
Language: Python
Stars: 41162
Forks: 5254
-----
![upscaling-x4](assets/stable-samples/upscaling/merged-dog.png)
After [downloading the weights](https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler), run
```
python scripts/gradio/superresolution.py configs/stable-diffusion/x4-upscaling.yaml <path-to-checkpoint>
```  
or  
```
streamlit run scripts/streamlit/superresolution.py -- configs/stable-diffusion/x4-upscaling.yaml <path-to-checkpoint>
```  
for a Gradio or Streamlit demo of the text-guided x4 superresolution model.
This model can be used both on real inputs and on synthesized examples. For the latter, we recommend setting a higher
`noise_level`, e.g. `noise_level=100`.