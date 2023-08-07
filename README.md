# Text to Image by Stable Diffusion
Input text prompt to return image by Stable Diffusion, a latent diffusion model
UI is built with Gradio

## key setting
- OS: Windows 10 Pro
- GPU enabled: NVIDIA GEOFORCE RTX 2070 (8GB VRAM)
- Pytorch 2.0.1 + cuda 11.7
- Model: [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1)
  
## Note:
1. Just discovered a very popular stable diffusion UI repo (link below) after I built the backend. Well, a good practice for me  ¯\\_(ツ)_/¯ [1]
2. Pytorch 2 is much more optimized than Pytorch 1 and is arguably faster even without xformers. [2, 3]
3. xformers may not bring performance gain to Pytorch 2+ [3]

### Reference
- [1] [https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [2] Release note of Pytorch 2.0 https://github.com/pytorch/pytorch/releases/tag/v2.0.0
- [3] Optimization wiki for stable diffusion by AUTOMATIC1111 https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Optimizations/

## License
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion/blob/21f890f9da3cfbeaba8e2ac3c425ee9e998d5229/LICENSE) 
- [Gradio](https://github.com/gradio-app/gradio/blob/34f6b22efbfedfa569d452f3f99ed2e6593e3c21/LICENSE)

