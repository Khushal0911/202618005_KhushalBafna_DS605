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
1. **Gender Disparity in Survival:** Survival rate was **74.20%** for females compared to **18.89%** for males, demonstrating the strong prioritization of women during lifeboat evacuations.
2. **Correlation Strengths:** The strongest positive relationship in the dataset is between `FamilySize` and `SibSp` ($+0.89$), while the strongest negative relationship is between `FamilySize` and `IsAlone` ($-0.69$).
3. **Class & Gender Intersection:** 1st-class females achieved the highest survival rate across all groups (**96.80%**), whereas 3rd-class males suffered the lowest survival rate (**13.54%**).
4. **Demographic Casualties:** Passengers traveling alone (`IsAlone = 1`), particularly young adult males under the age of 30 in lower classes, constituted the largest casualty demographic cohort.
5. **High Fare Survival Premium:** Passengers paying extreme fares ($> \$100$) had substantially higher survival rates, clearly separated in the upper region of the `Age vs. Fare` scatter plot.
---

## Repository Structure
* `titanic_analysis.ipynb` (or `.py`): Complete, runnable Python workflow.
* `titanic_cleaned.csv`: Cleaned dataset with imputed missing values and engineered features.
* `figures/`: Generated visualization charts (`correlation_heatmap.png`, `survival_by_sex.png`, `age_vs_fare.png`).
