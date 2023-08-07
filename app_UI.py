"""
https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/README.md
"""
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import time
import gradio as gr

def main(prompt="a photo of an astronaut riding a horse on mars"):
    start_time = time.time()
    model_directory = "./model/stable-diffusion-2-1"

    """ 
    Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
    - from_pretrained method that accepts 
    1) a Hugging Face Hub repository id, e.g. runwayml/stable-diffusion-v1-5 
    2) or a path to a local directory
    """
    pipe = StableDiffusionPipeline.from_pretrained(model_directory, local_files_only=True)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    image = pipe(prompt).images[0]

    run_time = round((time.time() - start_time),2)
    return run_time, image

demo = gr.Interface(fn=main,
                    inputs= [gr.Text(
                                label='What is in your mind', 
                                placeholder='a photo of an astronaut riding a horse on mars'
                             )],
                    outputs=[gr.Text(label='run time'),
                             gr.Image()],   
                    title="Convert Text to Image by Stable Diffusion",
                    allow_flagging="never")
    
if __name__ == "__main__":
    demo.launch(share=False)

    
    