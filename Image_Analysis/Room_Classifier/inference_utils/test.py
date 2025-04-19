import onnxruntime
from tqdm import tqdm
import torch
from torch.utils.data import DataLoader
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from typing import Tuple
from timeit import default_timer as timer

from utils.config import Settings

settings = Settings()


class Test:
    def __init__(self, model_path: str) -> None:
        """
        Initializes the ONNX runtime inference session.

        Args:
            model_path (str): The path to the ONNX model.
            model_threads (int): The number of threads to use for inference.
        """
        sess_options = onnxruntime.SessionOptions()
        sess_options.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
        sess_options.graph_optimization_level = (
            onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
        )
        sess_options.intra_op_num_threads = settings.num_threads
        self.sess = onnxruntime.InferenceSession(
            model_path, sess_options=sess_options, providers=["CPUExecutionProvider"]
        )

    def measure_inference_time(self, iterations: int) -> float:
        """
        Measures the average inference time per sample.

        Args:
            iterations (int): The number of iterations to run.

        Returns:
            float: The average inference time per sample.
        """
        total_time = 0.0
        for i in range(iterations):
            with torch.no_grad():
                example_input = torch.rand(
                    1, settings.CHANNELS, settings.HEIGHT, settings.WIDTH
                )
                input_data = example_input.numpy()
                start_time = timer()
                outputs = self.sess.run(None, {"input": input_data})
            total_time += timer() - start_time
        average_time = total_time / iterations
        return average_time

    def test_model(
        self,
        model: torch.nn.Module,
        dataloader: DataLoader,
        dataloader_name: str,
        criterion: torch.nn.Module,
    ) -> Tuple[float, float, float, float, float, np.ndarray]:
        """
        Tests the given model on the given dataloader.

        Args:
            model (torch.nn.Module): The model to be tested.
            dataloader (DataLoader): The dataloader to be tested on.
            dataloader_name (str): The name of the dataloader.
            criterion (torch.nn.Module): The loss function.

        Returns:
            Tuple[float, float, float, float, float, np.ndarray]: The total loss, accuracy, precision, recall, F1 score, and confusion matrix.
        """
        header = f"Testing {dataloader_name} dataset"
        model.to(settings.device)
        model.eval()
        running_loss = 0.0
        all_labels, preds = torch.tensor([], dtype=torch.long).to(
            settings.device
        ), torch.tensor([], dtype=torch.long).to(settings.device)
        with tqdm(dataloader, desc=header) as pbar:
            for idx, (inputs, targets) in enumerate(pbar):
                inputs = torch.stack(inputs).to(settings.device)
                targets = torch.stack(targets).to(settings.device)
                with torch.no_grad():
                    outputs = model(inputs)
                    loss = criterion(outputs, targets)
                running_loss += loss.item() * inputs.size(0)
                all_labels = torch.cat((all_labels, targets), 0)
                preds = torch.cat((preds, torch.argmax(outputs, dim=1)), 0)
        total_loss = running_loss / len(dataloader.dataset)
        all_labels = all_labels.detach().cpu().numpy().tolist()
        preds = preds.detach().cpu().numpy().tolist()
        accuracy = accuracy_score(all_labels, preds)
        precision = precision_score(
            all_labels, preds, average="macro", zero_division=1.0
        )
        recall = recall_score(all_labels, preds, average="macro", zero_division=1.0)
        f1 = f1_score(all_labels, preds, average="macro", zero_division=1.0)
        cm = confusion_matrix(all_labels, preds)
        return total_loss, accuracy, precision, recall, f1, cm

    def test_model_onnx(
        self,
        dataloader: DataLoader,
        dataloader_name: str,
        criterion: torch.nn.Module,
    ) -> Tuple[float, float, float, float, float, np.ndarray]:
        """
        Tests the ONNX model.

        Args:
            dataloader (DataLoader): The dataloader to be tested on.
            dataloader_name (str): The name of the dataloader.
            criterion (torch.nn.Module): The loss function.

        Returns:
            Tuple[float, float, float, float, float, np.ndarray]: The total loss, accuracy, precision, recall, F1 score, and confusion matrix.
        """
        header = f"Testing {dataloader_name} dataset"
        running_loss = 0.0
        all_labels, preds = torch.tensor([], dtype=torch.long), torch.tensor(
            [], dtype=torch.long
        )
        with tqdm(dataloader, desc=header) as pbar:
            for idx, (inputs, targets) in enumerate(pbar):
                inputs = torch.stack(inputs).to("cpu")
                targets = torch.stack(targets).to("cpu")
                with torch.no_grad():
                    outputs = self.sess.run(None, {"input": inputs.numpy()})[0]
                    outputs = torch.from_numpy(outputs)
                    loss = criterion(outputs, targets)
                running_loss += loss.item() * inputs.size(0)
                all_labels = torch.cat((all_labels, targets), 0)
                preds = torch.cat((preds, torch.argmax(outputs, dim=1)), 0)
        total_loss = running_loss / len(dataloader.dataset)
        all_labels = all_labels.detach().numpy().tolist()
        preds = preds.detach().numpy().tolist()
        accuracy = accuracy_score(all_labels, preds)
        precision = precision_score(
            all_labels, preds, average="macro", zero_division=1.0
        )
        recall = recall_score(all_labels, preds, average="macro", zero_division=1.0)
        f1 = f1_score(all_labels, preds, average="macro", zero_division=1.0)
        cm = confusion_matrix(all_labels, preds)
        return total_loss, accuracy, precision, recall, f1, cm
