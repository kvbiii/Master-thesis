from typing import Any, Tuple, Union
import cv2
import numpy as np
import os
from utils.config import Settings

settings = Settings()


class ImageReader:
    def __call__(
        self, image: Union[str, np.ndarray], label: Any
    ) -> Tuple[np.ndarray, Any]:
        """
        Read image and label from path and convert image to numpy array.

        Args:
            image (Union[str, np.ndarray]): path to image or image as numpy array
            label (Any): label

        Returns:
            Tuple[np.ndarray, Any]: image as numpy array and label
        """
        if isinstance(image, str):
            if not os.path.exists(image):
                raise FileNotFoundError(f"File {image} not found.")
            image = cv2.imread(image)
            # By default OpenCV uses BGR color space for color images o we need to convert the image to RGB color space.
            image = image[:, :, ::-1]
        elif isinstance(image, np.ndarray):
            image = image
        else:
            raise ValueError(f"Unsupported type {type(image)}")
        return image, label


class LabelReader:
    def __call__(self, image: np.ndarray, label: str) -> Tuple[np.ndarray, int]:
        """
        Read image and label from path and convert label to classes.

        Args:
            image (np.ndarray): image as numpy array
            label (str): path to label file

        Returns:
            Tuple[np.ndarray, int]: image as numpy array and label as classes
        """
        if isinstance(label, str):
            if label in settings.class_labels:
                class_label = settings.class_labels[label]
        else:
            raise ValueError(f"Unsupported type {type(label)}")
        return image, class_label
