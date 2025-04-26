import os
import torch
import torch.optim as optim
from torch.optim.lr_scheduler import ReduceLROnPlateau

from utils.config import Settings
from utils.plots import Plots
from dataset_utils.download_data import DataDownloader
from dataset_utils.dataloader import DataLoaderUtils
from model_utils.model_architecture import get_model
from model_utils.train import Train
from model_utils.early_stopping import EarlyStopping
from inference_utils.test import Test

settings = Settings()
settings.set_seeds()
# print("Downloading data ...")
# DataDownloader().download()

plots = Plots()
train_class = Train()
dataloader_utils = DataLoaderUtils()
model = get_model(num_classes=settings.num_classes).to(settings.device)
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=settings.lr)
scheduler = ReduceLROnPlateau(optimizer, mode="min", patience=6, factor=0.5)
early_stopper = EarlyStopping(patience=settings.early_stopping_patience, mode="max")

print("Training ...")
if not os.path.exists(settings.LOGGED_MODELS_PATH):
    os.makedirs(settings.LOGGED_MODELS_PATH)
model_save_path = train_class.train_model(
    dataloader_utils.dataloaders["train"],
    dataloader_utils.dataloaders["valid"],
    model,
    criterion,
    optimizer,
    scheduler,
    early_stopper,
    settings.num_epochs,
    settings.LOGGED_MODELS_PATH,
)
log_file = open(f"{settings.LOGGED_MODELS_PATH}/logs.txt", "r").read()
(
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
) = plots.parse_training_log(log_file)

fig_losses = plots.plot_losses(train_loss, valid_loss)
fig_accuracies = plots.plot_accuracy(train_accuracy, valid_accuracy)
fig_precisions_recalls = plots.plot_precision_and_recall(train_precision, valid_precision, train_recall, valid_recall)
fig_f1s = plots.plot_f1(train_f1, valid_f1)

print("Exporting to ONNX ...")
model = get_model(num_classes=settings.num_classes).to(settings.device)
model_save_path = f"{settings.LOGGED_MODELS_PATH}/best.pt"
state_dict = torch.load(model_save_path, weights_only=False)
model.load_state_dict(state_dict)
model.eval()

example_input = torch.randn(1, settings.CHANNELS, settings.HEIGHT, settings.WIDTH).to(
    settings.device
)
onnx_model_path = model_save_path[:-2] + "onnx"
torch.onnx.export(
    model.cpu(),
    example_input.cpu(),
    onnx_model_path,
    input_names=["input"],
    output_names=["output"],
    do_constant_folding=False,
    # dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
    #Add to dynamic axes also width and height
    dynamic_axes={"input": {0: "batch_size", 2: "width", 3: "height"}, "output": {0: "batch_size"}},
)

print("Testing ...")
test_class = Test(onnx_model_path)
inference_time_per_sample = test_class.measure_inference_time(500)
print(f"Measure inference time per sample: {inference_time_per_sample}\n")

(
    train_loss,
    train_accuracy,
    train_precision,
    train_recall,
    train_f1,
    train_confusion_matrix,
) = test_class.test_model(
    model, dataloader_utils.dataloaders["train"], "train", criterion
)
print(
    f"Train_loss: {round(train_loss, 4)} | Train_accuracy: {round(train_accuracy, 4)} | Train_precision {round(train_precision, 4)} | Train_recall: {round(train_recall, 4)} | Train_f1: {round(train_f1, 4)}\n"
)

(
    valid_loss,
    valid_accuracy,
    valid_precision,
    valid_recall,
    valid_f1,
    valid_confusion_matrix,
) = test_class.test_model(
    model, dataloader_utils.dataloaders["valid"], "valid", criterion
)
print(
    f"Valid_loss: {round(valid_loss, 4)} | Valid_accuracy: {round(valid_accuracy, 4)} | Valid_precision {round(valid_precision, 4)} | Valid_recall: {round(valid_recall, 4)} | Valid_f1: {round(valid_f1, 4)}\n"
)

(
    test_loss,
    test_accuracy,
    test_precision,
    test_recall,
    test_f1,
    test_confusion_matrix,
) = test_class.test_model(
    model, dataloader_utils.dataloaders["test"], "test", criterion
)
print(
    f"Test_loss: {round(test_loss, 4)} | Test_accuracy: {round(test_accuracy, 4)} | Test_precision {round(test_precision, 4)} | Test_recall: {round(test_recall, 4)} | Test_f1: {round(test_f1, 4)}\n"
)

# Test onnx model
(
    test_loss,
    test_accuracy,
    test_precision,
    test_recall,
    test_f1,
    test_confusion_matrix,
) = test_class.test_model_onnx(dataloader_utils.dataloaders["test"], "test", criterion)
print(
    f"Test_loss: {round(test_loss, 4)} | Test_accuracy: {round(test_accuracy, 4)} | Test_precision {round(test_precision, 4)} | Test_recall: {round(test_recall, 4)} | Test_f1: {round(test_f1, 4)}\n"
)