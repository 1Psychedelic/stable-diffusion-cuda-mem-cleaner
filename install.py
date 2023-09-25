import os
import shutil
import subprocess

def install(app_dir):
    # Získání aktuálního umístění skriptu
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Kopírování souborů rozšíření do cílové složky v aplikaci
    src_scripts_dir = os.path.join(current_directory, "scripts")
    dst_dir = os.path.join(app_dir, 'extensions', 'clear_cuda_memory')
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    shutil.copy(os.path.join(src_scripts_dir, 'clear_cuda_memory_ui.py'), dst_dir)

    # Přidání rozšíření do seznamu rozšíření aplikace (pokud aplikace takový seznam má)
    # Toto je jen příklad a může vyžadovat úpravy podle toho, jak je vaše aplikace konfigurována.
    with open(os.path.join(app_dir, 'extensions', 'extensions.txt'), 'a') as f:
        f.write('clear_cuda_memory.clear_cuda_memory_extension.ClearCudaMemoryExtension\n')

if __name__ == "__main__":
    # Zde můžete upravit cestu k vaší aplikaci, pokud je potřeba
    app_directory = "/sctipts/clear_cuda_memory_ui.py"
    install(app_directory)
