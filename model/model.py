import torchvision.models as models
import torch.nn as nn


def build_model(pretrained = True, fine_tune = True, num_classes = 10):
    if pretrained:
        print('Loading pre-trained model')
    else:
        print('Not loading pre-trained model')
    
    model = models.efficientnet_b0(pretrained = pretrained)
    
    if fine_tune:
        print('Model is fine-tuned')
        for params in model.parameters():
            params.requires_grad = True
    elif not fine_tune:
        print('Model is not fine-tuned')
        for params in model.parameters():
            params.requires_grad = False     
    model.classifier[1] = nn.Linear(in_features = 1280, out_features = num_classes)
    
    return model


def pretrained_model(pretrained = True, fine_tune = True, num_classes = 10):
    if pretrained:
        print('Loading pre-trained model')
    else:
        print('Not loading pre-trained model')
    
    model = models.efficientnet_b0(pretrained = pretrained)
    
    if fine_tune:
        print('Model is fine-tuned')
        for params in model.parameters():
            params.requires_grad = True    
    elif not fine_tune:
        print('Model is not fine-tuned')
        for params in model.parameters():
            params.requires_grad = False    
    model.classifier[1] = nn.Linear(in_features = 1280, out_features = num_classes)
    
    return model