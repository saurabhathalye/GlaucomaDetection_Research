
# Documentation

## Project Overview
This project demonstrates glaucoma detection using a hybrid deep learning framework combining U-Net and DeepLabV3+ for segmentation and Conditional Lyrebird Algorithm for classification.

## Running the Code
1. Preprocess Images:
   ```
   python code/preprocessing.py
   ```
2. Segment Optic Disc and Cup:
   ```
   python code/segmentation.py
   ```
3. Classify Glaucoma:
   ```
   python code/classification.py
   ```

## Adding New Data
Place your dataset in the `data/` folder and update the scripts to point to the new dataset.

## Outputs
Generated results are saved in the `results/` folder.
