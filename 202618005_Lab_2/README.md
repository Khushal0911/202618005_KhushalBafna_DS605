# Data Wrangling & Vectorized Programming: Titanic Analysis

## Student Details
* **Name:** Khushal Bafna
* **Student ID:** 202618005
* **Course:** DS605
* **Dataset:** [Kaggle Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)

---

## Project Overview
This project is divided into two core parts:
1. **Part A - Vectorized Programming with NumPy:** Implementing multi-dimensional array operations, matrix linear algebra (inversion, determinants, matrix products), and statistical distributions without explicit Python loops.
2. **Part B - Data Wrangling with Pandas:** Exploratory data analysis (EDA), multi-level grouping, data cleaning/imputation, outlier detection, feature engineering (`FamilySize`, `IsAlone`), and statistical visualization on the Titanic survival dataset.

---

## Key Observations
1. **Gender Disparity:** Female survival was **74.20%**, compared to just **18.89%** for males.
2. **Class Privilege:** Survival rate was highest in 1st Class (62.96%) and lowest in 3rd Class (24.24%).
3. **Highest vs Lowest Cohorts:** 1st Class females recorded the highest survival rate (**96.80%**), while 3rd Class males had the lowest (**13.54%**).
4. **Fare Outliers & Survival:** Fare was heavily right-skewed with an upper IQR threshold around $66.34; passengers paying $> $100 had significantly higher survival chances.
5. **Feature Correlations:** Strongest positive relationship is `FamilySize` and `SibSp` ($r = 0.89$), while `FamilySize` and `IsAlone` share the strongest negative relationship ($r = -0.69$).

---

## Repository Structure
* `titanic_analysis.ipynb` (or `.py`): Complete, runnable Python workflow.
* `titanic_cleaned.csv`: Cleaned dataset with imputed missing values and engineered features.
* `figures/`: Generated visualization charts (`correlation_heatmap.png`, `survival_by_sex.png`, `age_vs_fare.png`).
