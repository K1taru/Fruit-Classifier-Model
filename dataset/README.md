# Dataset Directory

This directory contains the fruit classification dataset used to train the models.

## Dataset Structure

The dataset is organized into 5 main fruit categories, each containing multiple subdirectories with various fruit types and conditions:

### Classes:
- **Apple/** - 5,061 images (229.93 MB)
- **Banana/** - 5,061 images (153.37 MB)
- **Grapes/** - 5,061 images (641.90 MB)
- **Mango/** - 4,172 images (200.80 MB)
- **Orange/** - 2,788 images (360.60 MB)

**Total:** 22,143 images (1,586.59 MB)

## Dataset Details

The dataset includes various varieties and conditions:
- Different fruit varieties (e.g., Red Apple, Pink Lady Apple, Braeburn)
- Different ripeness stages (ripe, unripe)
- Fresh and damaged fruits
- Multiple angles and lighting conditions

See `dataset_info.txt` for detailed class distribution statistics.

## Data Not Included in Repository

Due to size constraints (1.5+ GB), the actual image files are not stored in this repository. To use this project:

1. Download the dataset from your source (e.g., Kaggle)
2. Organize images into the subdirectories as shown in the workspace structure
3. Run the training notebook at `/src/fruit_classifier_model.ipynb`

## Dataset Sources

The dataset was compiled from multiple sources including:
- Various Kaggle fruit datasets
- Custom collected images
- Public fruit image repositories

Use the utility script at `/utils/kaggle_dataset_installer.py` to help download and organize datasets.
