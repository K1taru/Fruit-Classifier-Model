import kagglehub

# Download latest version
path = kagglehub.dataset_download("ismail703/fruits")

print("Path to dataset files:", path)