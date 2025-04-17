from typing import List, Tuple
import os
import numpy as np
import cv2
import torch
from torch.utils.data import Dataset
import albumentations as A
from albumentations.pytorch import ToTensorV2
from utils.config import Settings

settings = Settings()


class DatasetImageClassifier(Dataset):
    def __init__(
        self,
        dataset: List[Tuple[str, str]],
        readers: List[object] = [],
        transforms: A.Compose = None,
        name: str = "",
    ) -> None:
        """
        Initialize the dataset.

        Args:
            dataset (Union[str, List, pd.DataFrame]): A dataset path, list of data paths, or a DataFrame.
            readers (List[object]): A list of reader functions.
            transforms (A.Compose): A list of transforms.
            name (str, optional): The name of the dataset. Defaults to "".
        """
        self.dataset_ = dataset
        self.readers = readers
        self.transforms = transforms
        self.name = name

    def __len__(self):
        """
        Return the length of the dataset.

        Returns:
            int: Length of the dataset.
        """
        return len(self.dataset_)

    def process_data(self, data: List[str]) -> Tuple[np.ndarray, int]:
        """
        Process the data using readers, preprocessors, and augmentors.

        Args:
            data (List[str]): A list of data paths.

        Returns:
            Tuple[np.ndarray, int]: A tuple of image and label.
        """

        image, label = data
        for reader in self.readers:
            image, label = reader(image, label)
        if image.ndim == 2:
            image = np.expand_dims(image, axis=0)
        return image, label

    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Get a sample from the dataset.

        Args:
            index (int): Index of the sample.

        Returns:
            Tuple[torch.Tensor, torch.Tensor]: A tuple of image and target.
        """
        image, label = self.process_data(self.dataset_[index])
        target = torch.tensor(label, dtype=torch.int64)
        if self.transforms is not None:
            image = self.transforms(image=image)["image"]
            # image = (image / 255.0).detach().clone()
        return image, target


def collate_fn(batch):
    """
    Collate function for the dataset.

    Args:
        batch (List): A list of samples.

    Returns:
        Tuple: A tuple of images and targets.
    """
    return tuple(zip(*batch))


def load_data(data_dir: str) -> List[Tuple[str, str]]:
    """Load the data from the directory.

    Args:
        data_dir (str): A directory containing the data.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing image path and label category.
    """
    data = []
    for category in sorted(os.listdir(data_dir)):
        subfolder_path = os.path.join(data_dir, category)
        for file in sorted(os.listdir(subfolder_path)):
            file_path = os.path.join(subfolder_path, file)
            data.append((file_path, category))
    return data


data_transforms = {
    "train": A.Compose(
        [
            A.SmallestMaxSize(max_size=settings.HEIGHT, interpolation=cv2.INTER_AREA, p=1),
            A.CenterCrop(settings.HEIGHT, settings.WIDTH, p=1),
            A.Normalize(
                settings.MEAN,
                settings.STD,
                normalization="standard",
            ),
            ToTensorV2(),
        ]
    ),
    "train_augment": A.Compose(
        [
            A.RandomResizedCrop((settings.HEIGHT, settings.WIDTH), interpolation=cv2.INTER_AREA, p=1),
            #Random Resized Crop to 256x .
            # A.RandomCrop(settings.HEIGHT, settings.WIDTH, p=1),
            # A.SmallestMaxSize(max_size=settings.SMALLEST_MAX_SIZE, interpolation=cv2.INTER_AREA, p=1),
            # A.HorizontalFlip(p=0.5),
            # A.RandomRotate90(p=0.5),
            A.RandomBrightnessContrast(p=0.3),
            # A.Perspective(scale=0.2, p=0.5),
            A.MotionBlur(p=0.2),
            # A.GridDistortion(p=0.2),
            A.Normalize(
                settings.MEAN,
                settings.STD,
                normalization="standard",
            ),
            ToTensorV2(),
        ]
    ),

    "valid": A.Compose(
        [
            A.SmallestMaxSize(max_size=settings.SMALLEST_MAX_SIZE, interpolation=cv2.INTER_AREA, p=1),
            A.CenterCrop(settings.HEIGHT, settings.WIDTH, p=1),
            A.Normalize(
                settings.MEAN,
                settings.STD,
                normalization="standard",
            ),
            ToTensorV2(),
        ]
    ),
    "test": A.Compose(
        [
            A.SmallestMaxSize(max_size=settings.SMALLEST_MAX_SIZE, interpolation=cv2.INTER_AREA, p=1),
            A.CenterCrop(settings.HEIGHT, settings.WIDTH, p=1),
            A.Normalize(
                settings.MEAN,
                settings.STD,
                normalization="standard",
            ),
            ToTensorV2(),
        ]
    ),
}
