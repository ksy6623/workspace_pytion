import os
from PIL import Image
from torch.utils.data import Dataset

class ImageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []

        original_dir = os.path.join(root_dir, "original")
        protected_dir = os.path.join(root_dir, "protected")

        for filename in os.listdir(original_dir):
            self.image_paths.append(os.path.join(original_dir, filename))
            self.labels.append(0)  # 원본: 라벨 0

        for filename in os.listdir(protected_dir):
            self.image_paths.append(os.path.join(protected_dir, filename))
            self.labels.append(1)  # 보호됨: 라벨 1

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, label
