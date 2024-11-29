
# Glaucoma Detection Research

This repository contains the source code, datasets, and supplementary materials for the paper:
**"Enhancing Glaucoma Detection Accuracy through Conditional Lyrebird Algorithm-Trained Deep Spiking Neural Networks Using Retinal Fundus Images."**

## Repository Structure

- **code/**: Contains Python scripts for preprocessing, segmentation, feature extraction, and classification.
- **data/**: Placeholder for datasets (e.g., RIM-ONE, DRIONS-DB).
- **documentation/**: Instructions for running the code and reproducing results.
- **results/**: Sample outputs and performance metrics.

## Getting Started

### Dependencies

- Python 3.8+
- TensorFlow 2.x
- OpenCV
- NumPy
- Matplotlib

Install dependencies using:
```
pip install -r requirements.txt
```

### Running the Code

1. **Preprocessing**:
   - Navigate to `code/preprocessing.py` and run:
     ```
     python preprocessing.py
     ```
2. **Segmentation**:
   - Execute the U-Net and DeepLabV3+ models:
     ```
     python segmentation.py
     ```
3. **Classification**:
   - Train and test the semi-supervised CNN:
     ```
     python classification.py
     ```

### Datasets

Download the datasets and place them in the `data/` directory. Refer to the `data/README.md` for details.

### Results

Generated results will be stored in the `results/` directory.

## Citation

If you use this repository, please cite the corresponding paper.

## License

This project is licensed under the MIT License.
