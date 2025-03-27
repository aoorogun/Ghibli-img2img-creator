
#  Ghibli-img2img-creator

A **Gradio app** for transforming real photos into **Studio Ghibli-style illustrations** using **Stable Diffusion** and a **LoRA fine-tuned model**.

## ✨ Features

-  Upload any photo (portrait or scene)  
-  Stylize it using a Studio Ghibli-inspired LoRA  
-  Adjustable settings for strength, steps, and guidance  
-  Runs entirely on CPU (M1/M2 Mac compatible)  
-  Modular codebase for easy customization  

##  Project Structure

```
Ghibli-img2img-creator/
├── run_app.py                     # Main launcher
├── weights/                      # Local LoRA model file
│   └── StudioGhibliRedmond-*.safetensors
├── src/
│   └── app/
│       ├── config.py             # Config paths and model names
│       ├── model_loader.py       # Loads SD + LoRA pipeline
│       ├── stylizer.py           # Core stylization logic
│       └── interface.py          # Gradio app UI
├── requirements.txt
├── README.md
└── setup.py
```

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/aoorogun/Ghibli-img2img-creator.git
cd Ghibli-img2img-creator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the LoRA weights

Place your LoRA `.safetensors` file inside the `weights/` folder.  
Example: `weights/StudioGhibliRedmond-15V-LiberteRedmond-StdGBRedmAF-StudioGhibli.safetensors`

## 🖼 Run the App

```bash
python run_app.py
```

Visit the local app at: [http://localhost:7860](http://localhost:7860)

##  Configurable Parameters

- **Prompt** – Describe the Ghibli-style scene  
- **Style Strength** – Degree of stylization (0.3 to 0.9)  
- **Guidance Scale** – How closely it follows the prompt (1 to 15)  
