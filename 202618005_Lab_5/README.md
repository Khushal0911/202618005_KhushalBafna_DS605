# DS605: Fundamentals of Machine Learning - Lab 5[cite: 1]

**Machine Learning with Scikit-learn and From Scratch**[cite: 1]

This repository contains the implementation for Lab 5 of the DS605 course. The objective is to build, compare, and optimize regression and classification pipelines using both Scikit-learn and from-scratch implementations utilizing only NumPy and Pandas[cite: 1].

## Dataset

**UCI Productivity Prediction of Garment Employees**[cite: 1]
The dataset includes production features such as department, team, overtime, incentives, work in progress, and number of workers to evaluate real production performance[cite: 1].

- **Regression Target:** `actual_productivity` (using Linear Regression)[cite: 1].
- **Classification Target:** `Meets_Target` (Binary: 1 if actual >= targeted productivity, 0 otherwise, using Logistic Regression)[cite: 1].

## Repository Structure

- `garments_worker_productivity.csv`: The raw UCI dataset used for model training and evaluation.
- `code.ipynb`: Jupyter Notebook containing the complete end-to-end workflow (Data Preprocessing, Part A, Part B, and Part C).
- `README.md`: Project documentation and key observations.

## Implementation Details

### Part A: Scikit-learn Implementation[cite: 1]

- **Preprocessing:** `SimpleImputer` for missing values, `StandardScaler` for numerical scaling, and `OneHotEncoder` for categorical features[cite: 1].
- **Models:** `LinearRegression()` and `LogisticRegression()`[cite: 1].
- **Evaluation:** Fixed 80-20 train-test split evaluated using MAE, RMSE, R2, Accuracy, Precision, Recall, and F1-Score[cite: 1].

### Part B: From-Scratch Implementation[cite: 1]

- **Preprocessing:** Manual median imputation, standardization, and pandas-based one-hot encoding[cite: 1].
- **Linear Regression:** Solved using the closed-form Normal Equation with pseudo-inverse for numerical stability and speed[cite: 1].
- **Logistic Regression:** Implemented via iterative Gradient Descent, including manual sigmoid activation and probability thresholding[cite: 1].

### Part C: Optimization and Comparison[cite: 1]

The manual logistic regression was optimized by introducing **L2 Regularization (Ridge)** and **Early Stopping** based on gradient tolerance to bridge the performance gap with Scikit-learn[cite: 1].

## Key Observations[cite: 1]

### 1. Execution Time Differences

The Scikit-learn implementation significantly outperforms the baseline manual implementation in terms of training time. Scikit-learn models are built on highly optimized C and Cython backends and utilize advanced second-order optimization algorithms (such as L-BFGS or LIBLINEAR) which take highly efficient optimization steps. The manual Logistic Regression relies on a first-order Gradient Descent loop written in pure Python, which is inherently slower. By introducing a gradient-tolerance early stopping mechanism, the manual runtime gap was drastically reduced.

### 2. Predictive Performance Differences

Initially, the manual Logistic Regression yielded slightly different decision boundaries compared to the Scikit-learn model. This discrepancy occurs because Scikit-learn applies an L2 regularization penalty by default. Without regularization, the manual model is more prone to minor overfitting on the scaled training data. Once an explicit L2 penalty (`lambda_reg`) was integrated into the manual gradient descent update step, the predictive metrics (Accuracy, F1-Score) aligned closely with the Scikit-learn baseline.

---

**Author:** Khushal Bafna
**Program:** M.Sc. Data Science, DAU
