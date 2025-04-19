import torchvision
import torch.nn as nn


def get_model(num_classes):
    # model = torchvision.models.convnext_tiny(weights="DEFAULT")
    # model = torchvision.models.mobilenet_v3_large(weights="DEFAULT")
    model = torchvision.models.resnet18(weights="DEFAULT")
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    # model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
    return model
