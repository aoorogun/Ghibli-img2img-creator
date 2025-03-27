import torch
from diffusers import StableDiffusionImg2ImgPipeline
from app.config import BASE_MODEL, LORA_PATH
import os


def load_pipeline():
    print("Loading Stable Diffusion Img2Img Pipeline...")
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float32
    ).to("cpu")

    # 🔒 Ensure LORA_PATH is absolute and local
    if os.path.isfile(LORA_PATH):
        print(f"Loading Ghibli-style LoRA from {LORA_PATH}...")
        pipe.load_lora_weights(LORA_PATH)
    else:
        raise FileNotFoundError(f"LoRA file not found: {LORA_PATH}")

    return pipe
