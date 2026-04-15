import torch
from torch import nn
from pathlib import Path
from torchvision import datasets, transforms

CUR_DIR = Path.cwd()
DATA_DIR = Path.cwd().parent.parent / "traffic_signs"

dataset = datasets.ImageFolder(DATA_DIR, transform=transforms)


def create_full_dataset(data_dir: str, image_size: int = 32):
    pass


# print(dataset)


cuda = "Cuda" if torch.cuda.is_available() else "cpu"
print(cuda)
