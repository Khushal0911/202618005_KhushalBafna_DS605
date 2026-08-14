# DS605 Lab Assignment 1
## Data Scraping and Preprocessing using Python and Scrapy

### Student Details

- **Name:** Khushal Bafna
- **Student ID:** 202618005

---

## Objective

The objective of this assignment is to build a complete data pipeline by scraping book information from **https://books.toscrape.com/** using Scrapy within a Jupyter Notebook environment, preprocessing the collected data with Pandas, performing exploratory data analysis, generating visualizations with Matplotlib/Seaborn, and extracting meaningful data-driven insights.

---

## Project Structure

Based on the current working directory, the project is structured as a flat, notebook-driven analysis:

```text
202618005_Lab_1/
├── __pycache__/
├── book_spider.ipynb
├── books_raw.csv
├── books_cleaned.csv
├── combined_6_plots_grid.png
├── plot_1_price_distribution.png
├── plot_2_rating_distribution.png
├── plot_3_avg_price_by_category.png
├── plot_4_price_vs_rating.png
├── plot_5_wordcloud.png
├── plot_6_stock_by_category.png
└── plot_7_correlation_heatmap.png
```
---

## Task 1 – Data Scraping
- Scraped **120 books** sequentially from the first six catalogue pages.
- Extracted the following fields:
  - Title
  - Category
  - Price
  - Rating
  - Availability
  - Product Description
  - UPC
  - Number of Reviews
  - Product URL
- Exported the raw scraped data to `books_raw.csv`.

---

## Task 2 – Data Preprocessing
The following preprocessing steps were performed:
- Cleaned whitespace and inconsistent text across all string columns.
- Removed duplicate books by validating unique UPCs.
- Handled missing product descriptions with default filler text.
- Extracted and converted price strings to numeric float values.
- Mapped string-based ratings (One–Five) to integers (1-5).
- Extracted available stock count as integers.

### Engineered Features
- `description_word_count`: Total word count of the product description.
- `price_band`: Categorized books into 3 equal-sized buckets ('Budget', 'Mid-Range', 'Premium').
- `value_score`: A calculated metric (Rating / Price) to find highly-rated, affordable books.

*The cleaned dataset was saved as `books_cleaned.csv`.*

---

## Task 3 – Visualization and Analysis
Generated visualizations saved as individual PNGs and a combined 2x3 grid:
- Price Distribution (Histogram with KDE)
- Rating Distribution (Count Plot)
- Average Price by Category (Bar Plot)
- Price vs. Rating (Box Plot)
- Average Stock by Category (Bar Plot)
- Correlation Heatmap of Numeric Features
- Word Cloud generated from Book Descriptions

*Exploratory Data Analysis (EDA) and summary statistics were also generated for the cleaned dataset directly within the notebook.*

---

## Task 4 – Insights and Interpretation

### Key Observations
1. Price Concentration: Book prices are broadly distributed between £10 and £60, with a slight concentration in the £15–£20 range (where the count peaks at 10 books), as highlighted by the KDE trend line in the Price Distribution plot.
2. Balanced Star Ratings: Unlike real-world e-commerce platforms that usually skew positive, the star ratings in this dataset are remarkably balanced. The counts for 1 through 5 stars are nearly equal, with 2 and 3 stars marginally leading the pack at roughly 26 books each.
3. Category Pricing Variance: Among the top 15 most represented categories, average prices fluctuate significantly. The "Childrens" category is currently the most expensive on average at roughly £49, while categories like "Young Adult" and "Romance" average under £30.
4. Uniform Stock Levels: Despite the variance in price, the average stock levels across the top 15 categories are highly uniform. Almost all top categories maintain an average stock count of between 15 and 18 units.
5. No Price-to-Rating Relationship: The Price vs. Rating box plot reveals no clear relationship between cost and quality. In fact, the data shows a counterintuitive trend: the median price for a 1-star book (approximately £37) is slightly higher than the median price for a 5-star book (approximately £29).
6. Value Score Correlations: The Correlation Heatmap definitively proves that price and rating are entirely unrelated (r = -0.10). Furthermore, it shows that the engineered `value_score` has a strong positive correlation with ratings (r = 0.70) and a strong negative correlation with price (r = -0.66), confirming that the best theoretical value comes from highly rated, budget-friendly books.

### Limitations of the Dataset and Analysis
* Fictional Frequencies: The target website (`books.toscrape.com`) is a dedicated sandbox for developers learning to scrape. The prices, stock counts, and star ratings are randomly generated. The lack of correlation between price and rating is a byproduct of this randomized dummy data, meaning no real-world economic or consumer behavior trends can be drawn from it.
* Sample Size Constraints: Scraping 120 books represents only a small fraction of the entire catalog on the site. This small sample size limits the accuracy of category-based analysis, as many niche genres in the cleaned dataset are represented by only a single book.
* Textual Source Limitations: Because the website does not host actual customer reviews, publisher product descriptions were substituted to generate the Word Cloud. This prevents genuine sentiment analysis, as publisher descriptions are naturally generic and promotional rather than reflective of reader opinions.

---

## Technologies Used
- Python (Jupyter Notebook)
- Scrapy (Web scraping)
- Pandas & NumPy (Data manipulation and cleaning)
- Matplotlib & Seaborn (Data visualization)
- WordCloud (Text visualization)

---

## How to Run

### Execute the Pipeline
All tasks have been consolidated into a single notebook workflow.
1. Open `book_spider.ipynb` in your preferred environment (Jupyter Notebook or VS Code).
2. Ensure the required libraries are installed:
   ```bash
   pip install scrapy pandas numpy matplotlib seaborn wordcloud

## Conclusion
Here, the data only consists of 10% of the actual data, which makes the scope very narrow, so to have a better understanding, we can use the entire dataset and derive more insights which may change the correlation between the attributes.
