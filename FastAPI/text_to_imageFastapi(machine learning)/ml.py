import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

def obtain_image(prompt):

    pipe = StableDiffusionPipeline.from_pretrained(
      "CompVis/stable-diffusion-v1-4", 
      revision="fp16",
      torch_dtype=torch.float32) 

    image = pipe(prompt).images[0]

    return image

