import gradio as gr
import torch  # Assuming you are using PyTorch for CUDA operations

def reset_cuda_memory():
    torch.cuda.empty_cache()
    return "CUDA memory reset successfully!"

def main_gui():
    with gr.Interface(fn=reset_cuda_memory, outputs="text", live=True) as interface:
        with gr.Accordion("RESET CUDA MEMORY"):
            reset_button = gr.Button("RESET")
            info = gr.Info("Waiting for user action...")
            interface.add_components([reset_button, info])
        
        reset_button.click(reset_cuda_memory, outputs=[info])

    interface.launch()

if __name__ == "__main__":
    main_gui()