# DS605 Lab 6 — Feature Extraction and Machine Learning with Image and Text Data

## Overview

This project focuses on feature extraction and traditional machine learning classification using both image and text data.

The project consists of two main tasks:

- **Part A:** Asphalt Crack Image Classification
- **Part B:** Email Spam Classification

**Part C** investigates an improvement to the feature extraction process and compares the original and improved approaches in terms of classification performance and computational cost.

The project uses traditional machine learning methods and does not use CNNs, deep learning models, or pretrained image embeddings.

---

## Datasets

### Asphalt Crack Dataset

The image dataset contains:

- 200 Crack images
- 200 Non-Crack images
- **400 images in total**

The images are stored in:

- `448/Cracks/`
- `448/NonCracks/`

### Email Dataset

The email dataset contains:

- **5,172 emails**
- **3,000 numerical word-frequency features**
- `Email No.` as the email identifier
- `Prediction` as the target variable

The target distribution is:

- Non-Spam: 3,672
- Spam: 1,500

---

# Part A — Asphalt Crack Image Classification

## Image Preprocessing

Each image is processed using OpenCV and NumPy.

The following preprocessing steps are performed:

1. Read the image using OpenCV.
2. Convert the image from BGR to grayscale.
3. Resize the image to `10 × 10`.
4. Normalize pixel values to the range `[0, 1]`.

The normalized image is then flattened to obtain numerical pixel features.

### Feature Representation

Each image produces **106 features**:

- 100 pixel features from the `10 × 10` normalized image
- Mean brightness
- Contrast
- Dark-pixel ratio
- Bright-pixel ratio
- Edge count
- Edge density

Therefore:

**100 + 4 + 2 = 106 features**

---

## Canny Edge Detection

Canny edge detection is used to extract edge-related features from the grayscale images.

The original configuration uses:

- Lower threshold: `100`
- Upper threshold: `200`

The extracted edge features are:

- Edge count
- Edge density

Sample images are also visualized using:

- Original image
- Grayscale image
- Resized image
- Canny edge image

---

## Machine Learning Models

Two traditional machine learning classifiers are used:

- Logistic Regression
- Random Forest

The image dataset is divided using an 80:20 stratified train-test split.

- Training samples: 320
- Testing samples: 80
- Features: 106

---

## Image Classification Results

| Model               | Features |   Accuracy |  Precision |     Recall |   F1 Score | Training Time (s) | Prediction Time (s) |
| ------------------- | -------: | ---------: | ---------: | ---------: | ---------: | ----------------: | ------------------: |
| Logistic Regression |      106 |     67.50% |     68.42% |     65.00% |     66.67% |            0.4014 |              0.0005 |
| Random Forest       |      106 | **91.25%** | **92.31%** | **90.00%** | **91.14%** |            0.3885 |              0.0059 |

Random Forest achieved the highest image classification accuracy of **91.25%**.

### Logistic Regression Confusion Matrix

```text
[[28 12]
 [14 26]]
```

### Random Forest Confusion Matrix

```text
[[37  3]
 [ 4 36]]
```

---

# Part B — Email Spam Classification

## Dataset Representation

The supplied `emails.csv` dataset is already represented numerically using word-frequency features.

The dataset contains:

- `Email No.` — email identifier
- 3,000 numerical word-frequency features
- `Prediction` — spam/non-spam target

The original raw email text is not available in the supplied CSV. Therefore, the existing numerical representation is used directly as the feature matrix.

### TF-IDF

TF-IDF is **not used** in this project.

The supplied dataset is already converted into numerical word-frequency features, and the project follows the instruction not to use TF-IDF.

---

## Train-Test Split

The email dataset is divided using an 80:20 stratified train-test split.

- Training samples: 4,137
- Testing samples: 1,035
- Features: 3,000

---

## Machine Learning Models

The following classifiers are used:

- Logistic Regression
- Random Forest

---

## Email Classification Results

| Model               | Features |   Accuracy |  Precision |     Recall |   F1 Score | Training Time (s) | Prediction Time (s) |
| ------------------- | -------: | ---------: | ---------: | ---------: | ---------: | ----------------: | ------------------: |
| Logistic Regression |     3000 | **98.26%** | **95.78%** | **98.33%** | **97.04%** |           14.5323 |              0.1217 |
| Random Forest       |     3000 |     96.43% |     93.40% |     94.33% |     93.86% |        **2.3037** |              0.1430 |

Logistic Regression achieved the highest email classification accuracy of **98.26%**.

Random Forest required substantially less training time, but its classification performance was lower than Logistic Regression.

### Logistic Regression Confusion Matrix

```text
[[722  13]
 [  5 295]]
```

### Random Forest Confusion Matrix

```text
[[715  20]
 [ 17 283]]
```

---

# Part C — Improvement Experiment

Part C investigates whether modifying the feature extraction process can improve classification performance or reduce computational cost.

For the image classification task, the Canny edge detection thresholds were changed.

### Original Approach

Canny thresholds:

- Lower threshold: `100`
- Upper threshold: `200`

### Improved Approach

Canny thresholds:

- Lower threshold: `50`
- Upper threshold: `150`

All other image-processing steps were kept unchanged.

This allows the effect of changing the Canny thresholds to be evaluated independently.

---

## Original vs Improved — Logistic Regression

| Approach                  | Features | Accuracy | Precision | Recall | F1 Score | Training Time (s) | Prediction Time (s) |
| ------------------------- | -------: | -------: | --------: | -----: | -------: | ----------------: | ------------------: |
| Original Canny (100, 200) |      106 |   67.50% |    68.42% | 65.00% |   66.67% |            0.4014 |              0.0005 |
| Improved Canny (50, 150)  |      106 |   67.50% |    69.44% | 62.50% |   65.79% |        **0.2579** |              0.0019 |

---

## Original vs Improved — Random Forest

| Approach                  | Features |   Accuracy |  Precision |     Recall |   F1 Score | Training Time (s) | Prediction Time (s) |
| ------------------------- | -------: | ---------: | ---------: | ---------: | ---------: | ----------------: | ------------------: |
| Original Canny (100, 200) |      106 | **91.25%** | **92.31%** | **90.00%** | **91.14%** |            0.3885 |              0.0059 |
| Improved Canny (50, 150)  |      106 |     90.00% |     90.00% |     90.00% |     90.00% |        **0.3629** |              0.0414 |

---

## Canny Feature Comparison

The change in Canny thresholds produced the following edge statistics for the sample image:

| Canny Configuration | Edge Count | Edge Density |
| ------------------- | ---------: | -----------: |
| Original (100, 200) |     72,585 |     0.361652 |
| Improved (50, 150)  |     75,208 |     0.374721 |

The lower Canny thresholds detect more edges, increasing the edge density from approximately `0.3617` to `0.3747`.

---

## Trade-Off Analysis

The improved Canny configuration did not improve the classification accuracy of the image models.

For Random Forest:

- Original accuracy: **91.25%**
- Improved accuracy: **90.00%**

However, the Random Forest training time decreased slightly:

- Original: **0.3885 seconds**
- Improved: **0.3629 seconds**

For Logistic Regression, training time also decreased:

- Original: **0.4014 seconds**
- Improved: **0.2579 seconds**

The experiment shows that detecting more edges does not necessarily result in better classification performance. The additional edges detected using lower thresholds may contain less useful information or noise.

Therefore, the improved configuration provides a small computational benefit but does not provide better classification performance in this experiment.

This demonstrates the trade-off between:

- Feature information
- Classification performance
- Computational cost

---

# Overall Results

The highest classification accuracy obtained in the project was achieved on the email classification task.

### Email Classification

**Model:** Logistic Regression
**Accuracy:** 98.26%
**F1 Score:** 97.04%

### Image Classification

**Model:** Random Forest
**Accuracy:** 91.25%
**F1 Score:** 91.14%

The results demonstrate that model performance depends on both the characteristics of the dataset and the numerical representation used for classification.

---

# Evaluation Metrics

The models are evaluated using the following metrics:

### Accuracy

Measures the proportion of correctly classified samples.

### Precision

Measures how many of the samples predicted as positive actually belong to the positive class.

### Recall

Measures how many of the actual positive samples are correctly identified.

### F1 Score

Provides a balance between precision and recall.

### Confusion Matrix

Shows the number of:

- True Positives
- True Negatives
- False Positives
- False Negatives

### Training Time

Measures the time required to train the model.

### Prediction Time

Measures the time required to generate predictions on the test set.

---

# Technologies Used

- Python
- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

Install the required dependencies:

```bash
pip install numpy pandas opencv-python matplotlib scikit-learn jupyter
```

---

# Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
code.ipynb
```

Run the notebook cells sequentially.

Make sure the following dataset structure is available:

```text
448/
├── Cracks/
└── NonCracks/

emails.csv
```

---

# Repository Structure

```text
DS605-Lab6/
│
├── 448/
│   ├── Cracks/
│   └── NonCracks/
│
├── emails.csv
├── code.ipynb
└── README.md
```

---

# Key Learning Outcomes

This project demonstrates practical implementation of:

- Image preprocessing
- Grayscale conversion
- Image resizing
- Pixel normalization
- Image feature extraction
- Statistical intensity features
- Canny edge detection
- Edge count and edge density
- Numerical word-frequency representation
- Logistic Regression
- Random Forest
- Train-test splitting
- Stratified sampling
- Classification metrics
- Confusion matrices
- Training-time measurement
- Prediction-time measurement
- Feature dimensionality analysis
- Feature extraction parameter tuning
- Accuracy and computation trade-off analysis

---

# Author

**Khushal Bafna**
DAU, MSc Data Science
**DS605 — Machine Learning Lab**
