# Text to Image by Stable Diffusion
Input text prompt to return image by Stable Diffusion, a latent diffusion model
UI is built with Gradio

<p align="center"><img src="https://github.com/er1czz/stable-diffusion-with-UI/blob/main/sd_UI_demo.png" style = "border:10px solid white"></p> 

## Main specs:
- OS: Windows 10 Pro
- GPU: TU106 (NVIDIA Geoforce RTX 2070, 8GB VRAM)
- ```conda create --name stablediffusion_p38 python=3.8```
- Pytorch 2.0.1 + cuda 11.7
- Model: [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1)
- The whole model is large (67.6 GB). Therefore, a local copy (e.g. "./model/stable-diffusion-2-1/") is loaded.
- All the installed packages: [demo_requirements.txt](https://github.com/er1czz/stable-diffusion-with-UI/blob/main/demo_requirements.txt)
  
## Note:
- Just discovered a very popular stable diffusion UI repo (link below) after I built the backend. Well, a good practice for me  ¯\\_(ツ)_/¯ <sup>1</sup>
- Pytorch 2 is much more optimized and arguably faster than Pytorch 1 even without xformers. <sup>2, 3</sup>
- [xformers](https://github.com/facebookresearch/xformers) may not improve performance of Pytorch 2+ <sup>3</sup>. Therefore, xformers is not installed in this work.

### Reference
- <sup>1</sup> [https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- <sup>2</sup> Release note of Pytorch 2.0 https://github.com/pytorch/pytorch/releases/tag/v2.0.0
- <sup>3</sup> Optimization wiki for stable diffusion by AUTOMATIC1111 https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Optimizations/

## License
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion/blob/21f890f9da3cfbeaba8e2ac3c425ee9e998d5229/LICENSE) 
- [Gradio](https://github.com/gradio-app/gradio/blob/34f6b22efbfedfa569d452f3f99ed2e6593e3c21/LICENSE)

