import gradio as gr
from app.stylizer import ghibli_stylize

def create_interface(pipe):
    with gr.Blocks() as demo:
        gr.Markdown("## 🖼️ Photo to Studio Ghibli Style")
        gr.Markdown("Upload a photo and get a Ghibli-style version using Stable Diffusion & LoRA")

        with gr.Row():
            with gr.Column():
                input_image = gr.Image(label="Upload Photo", type="pil")
                prompt_input = gr.Textbox(label="Prompt (optional)")
                strength_slider = gr.Slider(0.3, 0.9, value=0.6, label="Style Strength")
                guidance_slider = gr.Slider(1, 15, value=8.0, label="Guidance Scale")
                step_slider = gr.Slider(10, 50, value=25, label="Inference Steps")
                run_btn = gr.Button("🎨 Stylize")

            with gr.Column():
                output_image = gr.Image(label="Ghibli-Styled Output")

        run_btn.click(
            fn=lambda img, p, s, g, st: ghibli_stylize(pipe, img, p, s, g, st),
            inputs=[input_image, prompt_input, strength_slider, guidance_slider, step_slider],
            outputs=output_image
        )

    return demo
