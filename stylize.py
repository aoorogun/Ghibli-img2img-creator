import torch
from torchvision import transforms
from PIL import Image
import os
from model import Generator

# === Paths ===
CHECKPOINT = 'weights/face_paint_512_v2.pt'  # Choose from available weights
INPUT_IMAGE = 'input.jpg'
OUTPUT_IMAGE = 'output.jpg'

# === Preprocessing ===
def load_image(path, size=512):
    img = Image.open(path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x * 2 - 1)
    ])
    return transform(img).unsqueeze(0)

def save_image(tensor, path):
    transform = transforms.Compose([
        transforms.Lambda(lambda x: (x + 1) / 2),
        transforms.ToPILImage()
    ])
    image = transform(tensor.squeeze(0).cpu())
    image.save(path)

# === Stylization ===
def stylize(input_path, output_path, checkpoint_path):
    print("Loading model...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = Generator().to(device)
    model.load_state_dict(torch.load(checkpoint_path, map_location=device))
    model.eval()

    print("Loading image...")
    img = load_image(input_path).to(device)

    print("Generating stylized output...")
    with torch.no_grad():
        out = model(img)

    save_image(out, output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    stylize(INPUT_IMAGE, OUTPUT_IMAGE, CHECKPOINT)
