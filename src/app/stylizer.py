import torch
from app.config import IMAGE_SIZE
from PIL import Image

def ghibli_stylize(pipe, image, prompt, strength=0.6, guidance=8.0, steps=25):
    prompt = prompt or "A Studio Ghibli style portrait, anime, soft lighting, clean lines"
    image = image.convert("RGB").resize(IMAGE_SIZE)

    with torch.no_grad():
        result = pipe(
            prompt=prompt,
            image=image,
            strength=strength,
            guidance_scale=guidance,
            num_inference_steps=int(steps)
        ).images[0]

    return result
