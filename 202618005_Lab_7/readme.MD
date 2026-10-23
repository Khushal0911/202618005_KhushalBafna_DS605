# DS605: Fundamentals of Machine Learning

## Lab Assignment - 7: Image Representation, PCA, Eigenfaces and Face Recognition

### Student Details

**Name:** Khushal Bafna
**Student ID:** 202618005

### Dataset

**Dataset:** AT&T Database of Faces (ORL)  
**Source:** Local Archive (40 subject directories with 10 images each)

The dataset contains 400 grayscale images representing 40 distinct subjects. The images were processed by reading the 2D pixel matrices, flattening them into 1D feature vectors, and organizing them into a unified dataset matrix alongside their corresponding subject labels.

## Objective

The objective of this assignment was to represent facial images numerically and implement Principal Component Analysis (PCA) strictly using foundational linear algebra operations (NumPy) to extract Eigenfaces and reduce dimensionality. The assignment evaluates face matching within this reduced PCA space against a raw pixel baseline and compares these similarity-based results with traditional machine-learning classifiers using Scikit-learn.

## Preprocessing & Representation Choices

### Image Representation

- Images were loaded and explicitly converted to grayscale matrices.
- Each 2D pixel matrix was flattened into a 1D feature vector (dimensionality heavily dependent on image resolution, resulting in a large feature space).
- The complete dataset was aggregated into an $N \times D$ matrix, with an accompanying target array mapping each image to its subject (labels 0-39).

### Train-Test Split

The data was split using:

- `test_size=0.2`
- `stratify=y`
- `random_state=42`

A stratified split was critical to ensure exactly 8 training images and 2 testing images per subject, guaranteeing all 40 subjects were represented in both sets.

### Mean Centering (Part B)

Before computing covariance and applying dimensionality reduction, the training data was mean-centered. A "Mean Face" was computed by averaging the training set along the feature axis, and this vector was subtracted from both the training and testing sets.

## Implementation Details

### PCA and Eigenfaces (From Scratch)

- **Mathematical Approach:** Dimensionality reduction was performed strictly using NumPy. Both the Covariance matrix/Eigendecomposition (`np.linalg.eigh`) and Singular Value Decomposition (`np.linalg.svd`) methods were tested.
- **Component Selection:** Cumulative explained variance was plotted, identifying that **$k=98$** principal components were required to retain at least 90% of the dataset's variance.
- **Eigenfaces:** The retained eigenvectors were reshaped back into 2D matrices and visualized, revealing the dominant structural variations (lighting, contours) across the dataset.

### Recognition Baselines (Part C)

A custom 1-Nearest Neighbor (1-NN) function was implemented using vectorized Euclidean distance computations in NumPy. This function was used to benchmark:

1. **Raw Pixel Space:** Matching test images directly using their full, uncompressed feature vectors.
2. **PCA Space:** Projecting test images into the $k=98$ subspace and matching based on the reduced representations.

## Models Compared (Part D)

Using the $k=98$ PCA features, four traditional Scikit-learn classifiers were trained and compared against the NumPy similarity-matching baselines:

1. Support Vector Machine (RBF Kernel, `gamma='scale'`)
2. Support Vector Machine (Linear Kernel)
3. K-Nearest Neighbors (`k=1`, Euclidean)
4. Logistic Regression (`solver='lbfgs'`, `max_iter=1000`)

## Observations and Execution Differences

The empirical comparisons revealed significant computational and structural differences between raw pixel matching and operating within the PCA eigenspace:

- **Storage & Dimensionality:** Projecting the data reduced the feature space from thousands of pixels down to just 98 components, offering a massive reduction in the memory footprint (RAM) required to store the representations. The overall storage saving ratio demonstrates how effectively PCA isolates primary variance from redundant background pixels.
- **Matching Latency:** Inference matching time in the PCA space was substantially faster. Computing pairwise Euclidean distances over 98 dimensions is computationally cheaper than over the full high-dimensional raw pixel space.
- **Reconstruction Quality:** While reconstructing faces from the 98 components resulted in slight blurring (loss of high-frequency noise), the core structural identifiers necessary to distinguish subjects remained fully intact.

## Final Observations

- The pure **PCA Similarity Matching (1-NN)** yielded highly competitive accuracy (e.g., **95.00%**) while executing faster and utilizing a fraction of the memory footprint of raw pixel matching.
- Removing the high-frequency components effectively acted as a noise filter, preventing extreme lighting or minor pixel shifts from corrupting the distance metric.
- When deploying traditional ML classifiers on the reduced space, the **SVM (Linear Kernel)** achieved the highest performance at **97.50%** accuracy, outperforming the basic Euclidean similarity matching.
- **Logistic Regression** also performed very well (**96.25%**), though it required a slightly longer training time compared to the optimized SVM routines.

## Conclusion

This assignment confirms that raw image pixels contain a massive amount of redundant and correlated information. By implementing PCA from scratch using core linear algebra properties (SVD/Covariance), we successfully extracted the fundamental "Eigenfaces" of the dataset. This allowed for extreme data compression that accelerated nearest-neighbor search times and proved highly effective as an input feature space for traditional classification algorithms like Support Vector Machines, which successfully modeled non-linear relationships to exceed baseline accuracies.
