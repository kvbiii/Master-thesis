import torch
from torch.utils.data import DataLoader
from timeit import default_timer as timer
from typing import Tuple, Any
from tqdm import tqdm
import gc
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from utils.config import Settings

settings = Settings()


class Train:
    def train_model(
        self,
        train_loader: DataLoader,
        valid_loader: DataLoader,
        model: torch.nn.Module,
        crtierion: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        scheduler: torch.optim.lr_scheduler,
        early_stopping: Any,
        num_epochs: int,
        folder_path: str,
    ):
        """
        Trains the given model using the given scaler, optimizer, scheduler, and early stopping.

        Args:
            train_loader (DataLoader): The training data loader.
            valid_loader (DataLoader): The validation data loader.
            model (torch.nn.Module): The model to be trained.
            crtierion (torch.nn.Module): The loss function.
            optimizer (torch.optim.Optimizer): The optimizer for training.
            scheduler (torch.optim.lr_scheduler): The learning rate scheduler.
            early_stopping (EarlyStopping): The early stopping object.
            num_epochs (int): The number of epochs to train the model.
            folder_path (str): The folder path to save the best model.

        Logs:
            Trainining and validation:
                - Epoch
                - Loss
                - Accuracy
                - Precision
                - Recall
                - F1 score

        Returns:
            str: The path to the best model.
        """
        log_file = open(f"{settings.LOGGED_MODELS_PATH}/logs.txt", "w")
        model_save_path = f"{folder_path}/best.pt"

        def log(message: str) -> None:
            print(message)
            log_file.write(message + "\n")

        log(f"Training started and performing on {settings.device} ...")
        best_valid_f1 = float("-inf")
        for epoch in range(num_epochs):
            torch.cuda.empty_cache()
            gc.collect()
            start_time = timer()
            train_loss, train_accuracy, train_precision, train_recall, train_f1 = (
                self.train_one_epoch(
                    train_loader,
                    model,
                    crtierion,
                    optimizer,
                    epoch,
                )
            )
            log(
                f"Epoch {epoch + 1}/{num_epochs} | Phase: train | Train_loss: {train_loss:.4f} | Train_accuracy: {train_accuracy:.4f} | Train_precision: {train_precision:.4f} | Train_recall: {train_recall:.4f} | Train_f1: {train_f1:.4f}"
            )
            valid_loss, valid_accuracy, valid_precision, valid_recall, valid_f1 = (
                self.evaluate_model(
                    valid_loader,
                    model,
                    crtierion,
                )
            )
            log(
                f"Epoch {epoch + 1}/{num_epochs} | Phase: valid | Valid_loss: {valid_loss:.4f} | Valid_accuracy: {valid_accuracy:.4f} | Valid_precision: {valid_precision:.4f} | Valid_recall: {valid_recall:.4f} | Valid_f1: {valid_f1:.4f}"
            )
            if early_stopping(valid_f1):
                log(
                    f"Epoch {epoch+1}: early stopping due to no improvement for {early_stopping.patience} consecutive epochs"
                )
                log(f"Best validation f1 score: {early_stopping.best_monitor_value}")
                return
            prev_lr = optimizer.param_groups[0]["lr"]
            scheduler.step(valid_loss)
            current_lr = optimizer.param_groups[0]["lr"]
            end_time = timer()
            log(f"Epoch time: {end_time - start_time}[s]")
            if current_lr != prev_lr:
                log(f"Learning rate updated: {prev_lr} -> {current_lr}")

            if valid_f1 > best_valid_f1:
                best_valid_f1 = valid_f1
                model_to_save = model
                model_to_save.eval()
                torch.save(model_to_save.state_dict(), model_save_path)
                log(
                    f"Best validation f1: {best_valid_f1:.4f} | Model saved to: {model_save_path}"
                )

        return model_save_path

    def train_one_epoch(
        self,
        train_loader: DataLoader,
        model: torch.nn.Module,
        criterion: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        epoch: int,
    ) -> Tuple[float, float, float, float, float]:
        """
        Trains the given model for one epoch.

        Args:
            train_loader (DataLoader): The training data loader.
            model (torch.nn.Module): The model to be trained.
            criterion (torch.nn.Module): The loss function.
            optimizer (torch.optim.Optimizer): The optimizer for training.
            epoch (int): The current epoch.

        Returns:
            Tuple[float, float, float, float, float]: The training loss, accuracy, precision, recall, and F1 score.
        """
        header = f"Training Epoch {epoch+1}"
        running_loss = 0.0
        all_labels, preds = torch.tensor([], dtype=torch.long).to(
            settings.device
        ), torch.tensor([], dtype=torch.long).to(settings.device)
        model.train()
        with tqdm(train_loader, desc=header) as pbar:
            for idx, (inputs, targets) in enumerate(pbar):
                inputs = torch.stack(inputs).to(settings.device)
                targets = torch.stack(targets).to(settings.device)
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
                loss_value = loss.item()
                running_loss += loss_value * inputs.size(0)
                all_labels = torch.cat((all_labels, targets), 0)
                preds = torch.cat((preds, torch.argmax(outputs, dim=1)), 0)
                pbar.set_postfix(
                    loss=f"{loss_value:.4f}", lr=optimizer.param_groups[0]["lr"]
                )
        train_loss = running_loss / len(train_loader.dataset)
        all_labels = all_labels.detach().cpu().numpy().tolist()
        preds = preds.detach().cpu().numpy().tolist()
        accuracy = accuracy_score(all_labels, preds)
        precision = precision_score(
            all_labels, preds, average="macro", zero_division=1.0
        )
        recall = recall_score(all_labels, preds, average="macro", zero_division=1.0)
        f1 = f1_score(all_labels, preds, average="macro", zero_division=1.0)
        return train_loss, accuracy, precision, recall, f1

    def evaluate_model(
        self,
        valid_loader: DataLoader,
        model: torch.nn.Module,
        criterion: torch.nn.Module,
    ) -> Tuple[float, float, float, float, float]:
        """
        Evaluates the given PyTorch model on the validation dataset.

        Args:
            valid_loader (DataLoader): The validation data loader.
            model (torch.nn.Module): The model to be evaluated.
            criterion (torch.nn.Module): The loss function.

        Returns:
            Tuple[float, float, float, float, float]: The validation loss, accuracy, precision, recall, and F1 score
        """
        header = "Validation"
        running_loss = 0.0
        all_labels, preds = torch.tensor([], dtype=torch.long).to(
            settings.device
        ), torch.tensor([], dtype=torch.long).to(settings.device)
        model.eval()
        with tqdm(valid_loader, desc=header) as pbar:
            for idx, (inputs, targets) in enumerate(pbar):
                inputs = torch.stack(inputs).to(settings.device)
                targets = torch.stack(targets).to(settings.device)
                with torch.no_grad():
                    outputs = model(inputs)
                    loss = criterion(outputs, targets)
                loss_value = loss.item()
                running_loss += loss_value * inputs.size(0)
                all_labels = torch.cat((all_labels, targets), 0)
                preds = torch.cat((preds, torch.argmax(outputs, dim=1)), 0)
                pbar.set_postfix(loss=f"{loss_value:.4f}")
        valid_loss = running_loss / len(valid_loader.dataset)
        all_labels = all_labels.detach().cpu().numpy().tolist()
        preds = preds.detach().cpu().numpy().tolist()
        accuracy = accuracy_score(all_labels, preds)
        precision = precision_score(
            all_labels, preds, average="macro", zero_division=1.0
        )
        recall = recall_score(all_labels, preds, average="macro", zero_division=1.0)
        f1 = f1_score(all_labels, preds, average="macro", zero_division=1.0)
        return valid_loss, accuracy, precision, recall, f1
