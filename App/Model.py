'''
📝 Pro Tips:

1. To load this model later:
Make sure you initialize the same model architecture first, then load the weights:

model = models.resnet50(weights=None)  # or pretrained=False
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, NUM_CLASSES)
model.load_state_dict(torch.load("resnet50_fruit_classifier.pth"))
model.to(device)
model.eval()


2. Optional — Save the entire model (less recommended):

torch.save(model, "resnet50_fruit_classifier_full.pth")


But this makes the file larger and is more fragile to code changes.

✅ Best practice (what you’re doing): save only state_dict — more flexible and portable.

'''