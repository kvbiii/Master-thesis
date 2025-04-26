import os
import torch
import random
import numpy as np


class Settings:
    SEED_VALUE = 17
    num_epochs = 100
    batch_size = 16
    num_threads = 4
    early_stopping_patience = 20
    lr = 1e-4

    class_names = ["kitchen", "living_room", "bedroom", "bathroom", "dining_room", "outside_building", "urban_environment"]
    class_labels = {class_name: i for i, class_name in enumerate(class_names)}
    num_classes = len(class_names)

    DESTINATION_PATH = "dataset"
    LOGGED_MODELS_PATH = "./Models/resnet18_07_03"
    train_dir = os.path.join(DESTINATION_PATH, "train")
    valid_dir = os.path.join(DESTINATION_PATH, "val")
    test_dir = os.path.join(DESTINATION_PATH, "test")

    SMALLEST_MAX_SIZE = 256
    CHANNELS, HEIGHT, WIDTH = 3, 224, 224
    MEAN = [0.6032591, 0.56755817, 0.5286094]
    STD = [0.20900008, 0.2107773, 0.21879801]

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    @staticmethod
    def set_seeds() -> None:
        """
        Sets the seed for reproducibility.
        """
        random.seed(Settings.SEED_VALUE)
        np.random.seed(Settings.SEED_VALUE)
        torch.manual_seed(Settings.SEED_VALUE)

        if torch.cuda.is_available():
            torch.cuda.manual_seed(Settings.SEED_VALUE)
            torch.cuda.manual_seed_all(Settings.SEED_VALUE)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = True
