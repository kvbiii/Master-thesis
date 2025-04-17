# import os, shutil, glob
# from sklearn.model_selection import train_test_split

# from utils.config import Settings

# settings = Settings()


# class DataDownloader:
#     def download(self) -> None:
#         """
#         1. Clears the destination path.
#         2. Downloads file from the S3 bucket.
#         3. Unzip the file.
#         4. Splits the dataset into train, validation, and test sets.
#         5. Removes all files which are not .png files.
#         """
#         self.clear_destination_path()
#         self.copy_files_from_source_to_destination()
#         self.split_based_on_class_name()
#         self.remove_wrong_files()

#     @staticmethod
#     def clear_destination_path() -> None:
#         """
#         Clears the destination path.
#         """
#         shutil.rmtree(settings.DESTINATION_PATH, ignore_errors=True)
#         os.makedirs(settings.DESTINATION_PATH, exist_ok=True)

#     @staticmethod
#     def copy_files_from_source_to_destination() -> None:
#         """
#         Copies files from source to destination.
#         """
#         for folder_name, class_name in settings.folder2class.items():
#             os.makedirs(os.path.join(settings.DESTINATION_PATH, folder_name), exist_ok=True)
#             for idx, file in enumerate(glob.glob(os.path.join(settings.SOURCE_PATH, folder_name, "*"))):
#                 if class_name == "outside" and idx >= 3700:
#                     break
#                 shutil.copy(file, os.path.join(settings.DESTINATION_PATH, folder_name))

#     def split_based_on_class_name(self) -> None:
#         """
#         Splits the dataset into train, validation, and test sets.
#         """
#         self.create_subdirs()
#         self.train_val_test_split()
#         # Remove empty folders
#         for folder_name in settings.folder2class.keys():
#             shutil.rmtree(os.path.join(settings.DESTINATION_PATH, folder_name))

#     @staticmethod
#     def create_subdirs() -> None:
#         """
#         Creates subdirectories for each class in the destination path.
#         """
#         for dataset in ["train", "val", "test"]:
#             for class_name in settings.folder2class.values():
#                 os.makedirs(
#                     os.path.join(settings.DESTINATION_PATH, dataset, class_name),
#                     exist_ok=True,
#                 )

#     def train_val_test_split(self) -> None:
#         """
#         For each urzad inside given category (class_name) split files into: train (70%), val (15%), test (15%).

#         Args:
#             urzads (list): List of distinct urzads.
#         """
#         for folder_name, class_name in settings.folder2class.items():
#             files = []
#             for file in sorted(
#                 os.listdir(os.path.join(settings.DESTINATION_PATH, folder_name))
#             ):
#                 files.append(file)
#             try:
#                 train_files, val_test_files = train_test_split(
#                     files, test_size=0.3, random_state=settings.SEED_VALUE
#                 )
#                 val_files, test_files = train_test_split(
#                     val_test_files, test_size=0.5, random_state=settings.SEED_VALUE
#                 )
#             except:
#                 continue
#             self.move_files(train_files, folder_name, class_name, "train")
#             self.move_files(val_files, folder_name, class_name, "val")
#             self.move_files(test_files, folder_name, class_name, "test")

#     @staticmethod
#     def move_files(files, folder_name, class_name, dataset) -> None:
#         """
#         Moves files to corresponding folders.

#         Args:
#             files (list): List of files to move.
#             folder_name (str): Name of the folder.
#             class_name (str): Name of the class.
#             dataset (str): Name of the dataset.
#         """
#         for file in files:
#             shutil.move(
#                 os.path.join(settings.DESTINATION_PATH, folder_name, file),
#                 os.path.join(settings.DESTINATION_PATH, dataset, class_name),
#             )

#     @staticmethod
#     def remove_wrong_files() -> None:
#         """
#         Removes all files which are not .png files.
#         """
#         for dataset in ["train", "val", "test"]:
#             for class_name in settings.folder2class.values():
#                 for file in glob.glob(
#                     os.path.join(settings.DESTINATION_PATH, dataset, class_name, "*")
#                 ):
#                     if not file.endswith(".png"):
#                         os.remove(file)

import warnings, os, shutil, glob
import pandas as pd
import mysql.connector as mysql
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")
from utils.config import Settings

settings = Settings()


class DataDownloader:
    def download(self) -> None:
        """
        1. Clears the destination path.
        2. Downloads file from the S3 bucket.
        3. Unzip the file.
        4. Splits the dataset into train, validation, and test sets.
        5. Removes all files which are not .png files.
        """
        self.clear_destination_path()
        data = self.read_table_from_db("images")
        self.split_based_on_class_name(data)
        self.remove_wrong_files()

    @staticmethod
    def read_table_from_db(table_name):
        username = os.environ["MYSQL_user"]
        password = os.environ["MYSQL_password"]
        DB = mysql.connect(
            host="localhost", user=username, passwd=password, database="AIRBNB"
        )
        df = pd.read_sql(f"SELECT * FROM {table_name}", con=DB)
        return df

    @staticmethod
    def clear_destination_path() -> None:
        """
        Clears the destination path.
        """
        shutil.rmtree(settings.DESTINATION_PATH, ignore_errors=True)
        os.makedirs(settings.DESTINATION_PATH, exist_ok=True)

    def split_based_on_class_name(self, data) -> None:
        """
        Splits the dataset into train, validation, and test sets.
        """
        self.create_subdirs()
        self.train_val_test_split(data)

    @staticmethod
    def create_subdirs() -> None:
        """
        Creates subdirectories for each class in the destination path.
        """
        for dataset in ["train", "val", "test"]:
            for class_name in settings.class_names:
                os.makedirs(
                    os.path.join(settings.DESTINATION_PATH, dataset, class_name),
                    exist_ok=True,
                )

    def train_val_test_split(self, data) -> None:
        """
        Splits the dataset into train, validation, and test sets.
        """
        for class_name in settings.class_names:
            subset = data.loc[data["room_type"] == class_name, ["id", "image"]]
            train_subset, val_test_subset = train_test_split(
                subset, test_size=0.3, random_state=settings.SEED_VALUE
            )
            val_subset, test_subset = train_test_split(
                val_test_subset, test_size=0.5, random_state=settings.SEED_VALUE
            )
            self.move_files(train_subset, class_name, "train")
            self.move_files(val_subset, class_name, "val")
            self.move_files(test_subset, class_name, "test")

    @staticmethod
    def move_files(subset, class_name, dataset) -> None:
        """
        Moves images to corresponding folders and saves them with the id as the name.

        Args:
            subset (DataFrame): Subset of the data.
            class_name (str): Name of the class.
            dataset (str): Name of the dataset.
        """
        for id, row in subset.iterrows():
            id = row["id"]
            byte_image = row["image"]
            image_destination_path = os.path.join(
                settings.DESTINATION_PATH, dataset, class_name, f"{id}.png"
            )
            with open(image_destination_path, "wb") as file:
                file.write(byte_image)

    @staticmethod
    def remove_wrong_files() -> None:
        """
        Removes all files which are not .png files.
        """
        for dataset in ["train", "val", "test"]:
            for class_name in settings.class_names:
                for file in glob.glob(
                    os.path.join(settings.DESTINATION_PATH, dataset, class_name, "*")
                ):
                    if not file.endswith(".png"):
                        os.remove(file)
