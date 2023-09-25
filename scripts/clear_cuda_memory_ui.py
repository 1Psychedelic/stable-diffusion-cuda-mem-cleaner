import modules.scripts as scripts
import gradio as gr
import os
import torch

from modules import images, script_callbacks
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

class ExtensionTemplateScript(scripts.Script):
        def title(self):
                return "Extension Template"

        def show(self, is_img2img):
                return scripts.AlwaysVisible
        
        def reset_cuda_memory(self):
                torch.cuda.empty_cache()
                print('CUDA memory reset successfully!')
                return "CUDA memory reset successfully!"

        # Setup menu ui detail
        def ui(self, is_img2img):
                with gr.Accordion('CUDA memory reset', open=False, elem_id=("cuda_reset")):
                        with gr.Row():
                                cuda_reset_button = gr.Button(value="RESET")
                                cuda_reset_button.click(self.reset_cuda_memory)
                return [cuda_reset_button]

        def run(self, p, cuda_reset_button):
                proc = process_images(p)
                return proc

