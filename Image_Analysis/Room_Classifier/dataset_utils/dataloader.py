from torch.utils.data import DataLoader, ConcatDataset, RandomSampler, SequentialSampler
from typing import Dict

from dataset_utils.dataset import (
    DatasetImageClassifier,
    load_data,
    collate_fn,
    data_transforms,
)
from dataset_utils.readers import ImageReader, LabelReader
from utils.config import Settings

settings = Settings()


class DataLoaderUtils:
    """
    Utility class for creating dataloaders.
    """

    def __init__(self) -> None:
        self.image_datasets = self.get_image_datasets()
        self.dataloaders = self.get_dataloaders(self.image_datasets)
        self.dataset_sizes = self.get_dataset_sizes(self.image_datasets)

    @staticmethod
    def get_image_datasets() -> Dict[str, DatasetImageClassifier]:
        """
        Returns the image datasets.

        Returns:
            Dict[str, DatasetImageClassifier]: The image datasets.
        """
        return {
            "train": DataLoaderUtils.online_augmentation(),
            "valid": DatasetImageClassifier(
                load_data(settings.valid_dir),
                readers=[ImageReader(), LabelReader()],
                transforms=data_transforms["valid"],
                name="valid",
            ),
            "test": DatasetImageClassifier(
                load_data(settings.test_dir),
                readers=[ImageReader(), LabelReader()],
                transforms=data_transforms["test"],
                name="test",
            ),
        }

    @staticmethod
    def offline_augmentation() -> ConcatDataset:
        """
        Returns the concatenated dataset with three augmented datasets.

        Returns:
            ConcatDataset: The concatenated dataset.
        """
        datasets = []
        for _ in range(0, 3):
            datasets.append(
                DatasetImageClassifier(
                    load_data(settings.train_dir),
                    readers=[ImageReader(), LabelReader()],
                    transforms=data_transforms["train_augment"],
                    name="train",
                )
            )
        return ConcatDataset(datasets)

    @staticmethod
    def online_augmentation() -> DatasetImageClassifier:
        """
        Returns the dataset with online augmentation.

        Returns:
            DatasetImageClassifier: The dataset with online augmentation.
        """
        return DatasetImageClassifier(
            load_data(settings.train_dir),
            readers=[ImageReader(), LabelReader()],
            transforms=data_transforms["train_augment"],
            name="train",
        )

    @staticmethod
    def no_augmentation() -> DatasetImageClassifier:
        """
        Returns the dataset without augmentation.

        Returns:
            DatasetImageClassifier: The dataset without augmentation.
        """
        return DatasetImageClassifier(
            load_data(settings.train_dir),
            readers=[ImageReader(), LabelReader()],
            transforms=data_transforms["train"],
            name="train",
        )

    @staticmethod
    def get_dataloaders(
        image_datasets: Dict[str, DatasetImageClassifier]
    ) -> Dict[str, DataLoader]:
        """
        Returns the dataloaders.

        Args:
            image_datasets (dict): The image datasets.

        Returns:
            Dict[str, DataLoader]: The dataloaders.
        """
        return {
            "train": DataLoader(
                image_datasets["train"],
                batch_size=settings.batch_size,
                sampler=RandomSampler(image_datasets["train"]),
                collate_fn=collate_fn,
            ),
            "valid": DataLoader(
                image_datasets["valid"],
                batch_size=settings.batch_size,
                sampler=SequentialSampler(image_datasets["valid"]),
                collate_fn=collate_fn,
            ),
            "test": DataLoader(
                image_datasets["test"],
                batch_size=1,
                sampler=SequentialSampler(image_datasets["test"]),
                collate_fn=collate_fn,
            ),
        }

    @staticmethod
    def get_dataset_sizes(image_datasets: Dict[str, DatasetImageClassifier]) -> Dict[str, int]:
        """
        Returns the dataset sizes.

        Args:
            image_datasets (Dict[str, DatasetImageClassifier]): The image datasets.

        Returns:
            Dict[str, int]: The dataset sizes.
        """
        return {
            "train": len(image_datasets["train"]),
            "valid": len(image_datasets["valid"]),
            "test": len(image_datasets["test"]),
        }
