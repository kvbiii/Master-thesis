import numpy as np


class EarlyStopping:
    def __init__(self, patience: int = 5, mode: str = "min"):
        """
        Early stops the training if validation loss doesn't improve after a given patience.

        Args:
            patience (int): How long to wait after last time validation loss improved (default: 5).
            mode (str): Chosen mode based on which the training will be stopped (default: min). Possible values: min, max, min_equal, max_equal.
        """
        self.patience = patience
        self.mode = mode
        self.compare = self.assign_mode(mode)
        self.wait = None
        self.stopped_epoch = None
        self.best_monitor_value = (
            np.inf if self.mode == "min" or self.mode == "min_equal" else -np.inf
        )

    @staticmethod
    def assign_mode(mode: str) -> np.ufunc:
        """
        Assigns the mode based on the given string.

        Args:
            mode (str): The mode to assign.

        Returns:
            np.ufunc: The function that compares the values.
        """
        if mode == "min":
            return np.less
        elif mode == "max":
            return np.greater
        elif mode == "min_equal":
            return np.less_equal
        else:
            return np.greater_equal

    def __call__(self, monitor_value: float) -> bool:
        """
        Checks if the training should be stopped.

        Args:
            monitor_value (float): The value of the monitored metric.

        Returns:
            bool: True if the training should be stopped, False otherwise.
        """
        monitor_value = monitor_value
        if monitor_value is None:
            return
        if self.compare(monitor_value, self.best_monitor_value):
            self.best_monitor_value = monitor_value
            self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                return True
        return False
