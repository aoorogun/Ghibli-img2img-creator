import multiprocessing
import torch
from app.model_loader import load_pipeline
from app.interface import create_interface

torch.set_num_threads(1)
multiprocessing.set_start_method("fork", force=True)

if __name__ == "__main__":
    pipe = load_pipeline()
    app = create_interface(pipe)
    app.launch(debug=True)
