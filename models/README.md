# Models Directory

This directory contains trained model files for the Fruit Classifier project.

## Model Files (Not Included in Repository)

Due to file size constraints, trained model files are not stored in this repository. The following models were trained locally:

- `fruit_classifier_model_E9_VAL99.88.pth` - Model trained for 9 epochs with 99.88% validation accuracy
- `fruit_classifier_resnet50_E15.pth` - ResNet50-based model trained for 15 epochs
- `resnet50_fruit_classifier.pth` - Base ResNet50 fruit classifier
- `resnet50_fruit_classifier_E30.pth` - ResNet50 model trained for 30 epochs

## Production Model

The production-ready model is located in `/App/models/fruit_classifier_resnet50_E20.pth` and is included in the repository for deployment purposes.

## How to Use

1. Train your own model using the notebook at `/src/fruit_classifier_model.ipynb`
2. Save trained models to this directory
3. The production model will be loaded from `/App/models/` for inference

## Model Architecture

All models are based on ResNet50 architecture, fine-tuned for fruit classification across 5 classes:
- Apple
- Banana
- Grapes
- Mango
- Orange
