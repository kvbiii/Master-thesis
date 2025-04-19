import cv2
import numpy as np
from typing import Tuple, List


class RoomTypePreprocessing:
    def __init__(
        self,
        smallest_max_size: int,
        image_resolution: Tuple[int, int],
        mean: List[float],
        std: List[float],
    ) -> None:
        """
        Initializes the RoomTypePreprocessing class.

        Args:
            smallest_max_size (int): Maximum size of the smallest side of the image to which the image will be resized (aspect ratio is preserved).
            image_resolution (Tuple[int, int]): Resolution to resize the input image.
            mean (List[float]): Mean values for normalization.
            std (List[float]): Standard deviation values for normalization.
        """
        self.smallest_max_size = smallest_max_size
        self.image_resolution = image_resolution
        self.mean = mean
        self.std = std

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocesses the input image.

        Args:
            image (np.ndarray): Input image.

        Returns:
            np.ndarray: Preprocessed image.
        """
        image = self.check_and_convert_image(image)
        resized_image = self.resize_image(image, self.smallest_max_size)
        centered_image = self.center_crop_image(resized_image, self.image_resolution)
        normalized_image = self.normalize_image(centered_image)
        transposed_image = np.transpose(normalized_image, (2, 0, 1))
        image = np.expand_dims(transposed_image, axis=0)
        return image

    @staticmethod
    def check_and_convert_image(image: np.ndarray) -> np.ndarray:
        """
        Checks the image and converts it to the correct format (if image has 4 channels, converts it to 3 channels).

        Args:
            image (np.ndarray): Input image.

        Returns:
            np.ndarray: Converted image.
        """
        if image.shape == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        return image

    @staticmethod
    def resize_image(image: np.ndarray, max_size: int) -> np.ndarray:
        """
        Resizes the image to the specified width.

        Args:
            image (np.ndarray): Input image.
            max_size (int): maximum (new) size of smallest side (width or height) of the image, so that the aspect ratio is preserved.

        Returns:
            np.ndarray: Resized image.
        """
        image_shape = image.shape[:2]
        scale_ratio = max_size / float(min(image_shape))
        resized_height, resized_width = tuple(
            round(dim * scale_ratio) for dim in image_shape
        )
        return cv2.resize(
            image, (resized_width, resized_height), interpolation=cv2.INTER_AREA
        )

    @staticmethod
    def center_crop_image(image: np.ndarray, size: Tuple[int, int]) -> np.ndarray:
        """
        Center crops the image to size.

        Args:
            image (np.ndarray): Input image.
            size (Tuple[int, int]): Size to crop the image.

        Returns:
            np.ndarray: Center cropped image.
        """
        height, width = image.shape[:2]
        new_height, new_width = size
        top = (height - new_height) // 2
        left = (width - new_width) // 2
        bottom = top + new_height
        right = left + new_width
        return image[top:bottom, left:right]

    def normalize_image(self, image: np.ndarray) -> np.ndarray:
        """
        Normalizes the image.

        Args:
            image (np.ndarray): Input image.

        Returns:
            np.ndarray: Normalized image.
        """
        max_pixel_value = 255.0
        mean = (np.array(self.mean, dtype=np.float32) * max_pixel_value).reshape(-1, 1)
        std = (
            np.reciprocal(np.array(self.std, dtype=np.float32) * max_pixel_value)
        ).reshape(-1, 1)
        luts = (np.arange(0, max_pixel_value + 1, dtype=np.float32) - mean) * std
        return cv2.merge([cv2.LUT(image[:, :, i], luts[i]) for i in range(3)])
