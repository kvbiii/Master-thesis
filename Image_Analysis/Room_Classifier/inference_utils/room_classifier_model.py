from typing import Dict, Union, Tuple, List
import onnxruntime
import numpy as np

from inference_utils.room_classifier_preprocessing import RoomTypePreprocessing


class RoomTypeClassification:
    ROOM_TYPE_DICT: Dict[int, str] = {
        0: "kitchen",
        1: "living_room",
        2: "bedroom",
        3: "bathroom",
        4: "dining_room",
        5: "outside_building",
        6: "urban_environment",
    }

    def __init__(
        self,
        model_path: str,
        model_threads: int,
        smallest_max_size: int,
        image_resolution: Tuple[int, int],
        mean: List[float],
        std: List[float],
    ) -> None:
        """
        Initializes the RoomTypeClassification class.

        Args:
            model_path (str): Path to the ONNX model.
            model_threads (int): Number of threads to use for the model.
            smallest_max_size (int): Maximum size of the smallest side of the image to which the image will be resized (aspect ratio is preserved).
            image_resolution (Tuple[int, int]): Resolution to resize the input image.
            mean (List[float]): Mean values for normalization.
            std (List[float]): Standard deviation values for normalization.
        """
        self.image_preprocessor = RoomTypePreprocessing(
            smallest_max_size, image_resolution, mean, std
        )

        sess_options = onnxruntime.SessionOptions()
        sess_options.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
        sess_options.graph_optimization_level = (
            onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
        )
        sess_options.intra_op_num_threads = model_threads
        self.sess = onnxruntime.InferenceSession(
            model_path, sess_options=sess_options, providers=["CPUExecutionProvider"]
        )

    def predict(self, image: np.ndarray) -> Dict[str, Union[str, float]]:
        """
        Predicts room type based on the input image.

        Args:
            image (np.ndarray): Input image.

        Returns:
            Dict[str, Union[str, float]]: Dictionary containing the predicted room type and its probability.
        """
        image = self.image_preprocessor.preprocess(image)
        outputs = self.sess.run(None, {"input": image})[0]
        room_category, room_category_prob, probabilities = (
            self.determine_category_and_prob(outputs)
        )
        return {
            "room_type": room_category,
            "probability": room_category_prob,
            "probabilities": probabilities,
        }

    def determine_category_and_prob(self, outputs: np.ndarray) -> Tuple[str, float]:
        """
        Determines the category and probability of the model output.

        Args:
            outputs (np.ndarray): Model outputs.

        Returns:
            Tuple[str, float]: Room category and its probability.
        """
        probabilities = self.softmax(outputs)
        room_category = np.argmax(probabilities, axis=1).item()
        room_category_prob = probabilities[0][room_category].item()
        room_category = self.ROOM_TYPE_DICT[room_category]
        return room_category, room_category_prob, probabilities

    @staticmethod
    def softmax(logits: np.ndarray) -> np.ndarray:
        """
        Computes the softmax function.

        Args:
            logits (np.ndarray): Input logits.

        Returns:
            np.ndarray: Softmax probabilities.
        """
        exps = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
        return exps / np.sum(exps, axis=-1, keepdims=True)
