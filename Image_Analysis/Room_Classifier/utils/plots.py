import plotly.graph_objects as go
import plotly.express as px
# import seaborn as sns
from utils.config import Settings
from typing import List, Tuple
import numpy as np
import re

settings = Settings()


class Plots:
    @staticmethod
    def parse_training_log(
        log_file: str,
    ) -> Tuple[
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        List[float],
        int,
    ]:
        """
        Parses the training log data to extract training and validation losses and metrics.

        Args:
            log_file (str): String containing the training log data.

        Returns:
            (Tuple[List[float], List[float], List[float], List[float], List[float], List[float], int):
            - List of training losses.
            - List of training accuracies.
            - List of training precisions.
            - List of training recalls.
            - List of training f1 scores.
            - List of validation losses.
            - List of validation accuracies.
            - List of validation precisions.
            - List of validation recalls.
            - List of validation f1 scores.
            - The best epoch.
        """
        train_loss = [float(i) for i in re.findall(r"Train_loss: (\d+\.\d+)", log_file)]
        train_accuracy = [
            float(i) for i in re.findall(r"Train_accuracy: (\d+\.\d+)", log_file)
        ]
        train_precision = [
            float(i) for i in re.findall(r"Train_precision: (\d+\.\d+)", log_file)
        ]
        train_recall = [
            float(i) for i in re.findall(r"Train_recall: (\d+\.\d+)", log_file)
        ]
        train_f1 = [float(i) for i in re.findall(r"Train_f1: (\d+\.\d+)", log_file)]
        valid_loss = [float(i) for i in re.findall(r"Valid_loss: (\d+\.\d+)", log_file)]
        valid_accuracy = [
            float(i) for i in re.findall(r"Valid_accuracy: (\d+\.\d+)", log_file)
        ]
        valid_precision = [
            float(i) for i in re.findall(r"Valid_precision: (\d+\.\d+)", log_file)
        ]
        valid_recall = [
            float(i) for i in re.findall(r"Valid_recall: (\d+\.\d+)", log_file)
        ]
        valid_f1 = [float(i) for i in re.findall(r"Valid_f1: (\d+\.\d+)", log_file)]
        best_epoch = int(re.findall(r"Epoch (\d+)", log_file)[-1])
        if re.search(r"early stopping", log_file):
            best_epoch = best_epoch - settings.early_stopping_patience
        return (
            train_loss,
            train_accuracy,
            train_precision,
            train_recall,
            train_f1,
            valid_loss,
            valid_accuracy,
            valid_precision,
            valid_recall,
            valid_f1,
            best_epoch,
        )

    @staticmethod
    def plot_losses(train_loss: List[float], valid_loss: List[float]) -> go.Figure:
        """
        Plots training and validation loss over epochs.

        Args:
            train_loss (List[float]): List of training losses.
            valid_loss (List[float]): List of validation losses.

        Returns:
            go.Figure: The plot figure.
        """
        fig = go.Figure()
        epochs = [i for i in range(1, len(train_loss) + 1)]
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=train_loss,
                mode="lines+markers",
                line=dict(color="blue"),
                marker=dict(size=5),
                name="Training Loss",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=valid_loss,
                mode="lines+markers",
                line=dict(color="red"),
                marker=dict(size=5),
                name="Validation Loss",
                showlegend=True,
            )
        )
        fig.update_layout(
            template="simple_white",
            width=1200,
            height=600,
            yaxis_title="Loss",
            xaxis_title="Epochs",
            title=f"<b>Training and Validation Loss<b>",
            title_x=0.5,
            font=dict(family="Times New Roman", size=16, color="Black"),
        )
        fig.write_image(f"{settings.LOGGED_MODELS_PATH}/loss.png")
        return fig

    @staticmethod
    def plot_accuracy(
        train_accuracy: List[float], valid_accuracy: List[float]
    ) -> go.Figure:
        """
        Plots training and validation accuracy over epochs.

        Args:
            train_accuracy (List[float]): List of training accuracies.
            valid_accuracy (List[float]): List of validation accuracies.

        Returns:
            go.Figure: The plot figure.
        """
        fig = go.Figure()
        epochs = [i for i in range(1, len(train_accuracy) + 1)]
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=train_accuracy,
                mode="lines+markers",
                line=dict(color="blue"),
                marker=dict(size=5),
                name="Training Accuracy",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=valid_accuracy,
                mode="lines+markers",
                line=dict(color="red"),
                marker=dict(size=5),
                name="Validation Accuracy",
                showlegend=True,
            )
        )
        fig.update_layout(
            template="simple_white",
            width=1200,
            height=600,
            yaxis_title="Accuracy",
            xaxis_title="Epochs",
            title=f"<b>Training and Validation Accuracy<b>",
            title_x=0.5,
            font=dict(family="Times New Roman", size=16, color="Black"),
        )
        fig.write_image(f"{settings.LOGGED_MODELS_PATH}/accuracy.png")
        return fig

    @staticmethod
    def plot_precision_and_recall(train_precision: List[float], valid_precision: List[float], train_recall: List[float], valid_recall: List[float]) -> go.Figure:
        """
        Plots training and validation recall over epochs.

        Args:
            train_precision (List[float]): List of training precisions.
            valid_precision (List[float]): List of validation precisions.
            train_recall (List[float]): List of training recalls.
            valid_recall (List[float]): List of validation recalls.

        Returns:
            go.Figure: The plot figure.
        """
        fig = go.Figure()
        epochs = [i for i in range(1, len(train_precision) + 1)]
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=train_precision,
                mode="lines+markers",
                line=dict(color="blue"),
                marker=dict(size=5),
                name="Training Precision",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=valid_precision,
                mode="lines+markers",
                line=dict(color="red"),
                marker=dict(size=5),
                name="Validation Precision",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=train_recall,
                mode="lines+markers",
                line=dict(color="green"),
                marker=dict(size=5),
                name="Training Recall",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=valid_recall,
                mode="lines+markers",
                line=dict(color="orange"),
                marker=dict(size=5),
                name="Validation Recall",
                showlegend=True,
            )
        )
        fig.update_layout(
            template="simple_white",
            width=1200,
            height=600,
            yaxis_title="Precision and Recall",
            xaxis_title="Epochs",
            title=f"<b>Training and Validation Precision and Recall<b>",
            title_x=0.5,
            font=dict(family="Times New Roman", size=16, color="Black"),
        )
        fig.write_image(f"{settings.LOGGED_MODELS_PATH}/precision_recall.png")
        return fig

    @staticmethod
    def plot_f1(train_f1: List[float], valid_f1: List[float]) -> go.Figure:
        """
        Plots training and validation f1 score over epochs.

        Args:
            train_f1 (List[float]): List of training f1 scores.
            valid_f1 (List[float]): List of validation f1 scores.

        Returns:
            go.Figure: The plot figure.
        """
        fig = go.Figure()
        epochs = [i for i in range(1, len(train_f1) + 1)]
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=train_f1,
                mode="lines+markers",
                line=dict(color="blue"),
                marker=dict(size=5),
                name="Training F1 Score",
                showlegend=True,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=epochs,
                y=valid_f1,
                mode="lines+markers",
                line=dict(color="red"),
                marker=dict(size=5),
                name="Validation F1 Score",
                showlegend=True,
            )
        )
        fig.update_layout(
            template="simple_white",
            width=1200,
            height=600,
            yaxis_title="F1 Score",
            xaxis_title="Epochs",
            title=f"<b>Training and Validation F1 Score<b>",
            title_x=0.5,
            font=dict(family="Times New Roman", size=16, color="Black"),
        )
        fig.write_image(f"{settings.LOGGED_MODELS_PATH}/f1_score.png")
        return fig
