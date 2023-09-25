import modules.scripts as scripts
import gradio as gr
import torch
import os
import contextlib

class ExtensionTemplateScript(scripts.Script):
    def title(self):
        return "RESET CUDA MEMORY"

    def show(info, is_img2img):
        return scripts.AlwaysVisible

    def reset_cuda_memory(self):  # Přidání 'self' jako prvního argumentu
        torch.cuda.empty_cache()
        return "CUDA memory reset successfully!"

    def ui(self, is_img2img):
        with gr.Accordion("RESET CUDA MEMORY", open=False):
            with gr.Row():
                reset_button = gr.Button("RESET")
                info = gr.Info("Waiting for user action...")

        with contextlib.suppress(AttributeError):
            if is_img2img:
                reset_button.click(self.reset_cuda_memory, outputs=[info])  # Použití self.reset_cuda_memory
            else:
                reset_button.click(self.reset_cuda_memory, outputs=[info])

        return [reset_button, info]
