# Sales Data Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project is developed as part of the **CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis (EDA)**.

The project focuses on exploring a sales dataset to understand its structure, identify data-quality issues, clean and preprocess the data, discover trends and patterns, analyze relationships between variables, and detect potential outliers.

Python-based data analysis and visualization techniques are used to extract meaningful insights from the dataset.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the structure and characteristics of the sales dataset.
* Identify missing values and duplicate records.
* Detect completely empty or incomplete records.
* Clean and preprocess the dataset.
* Convert date columns into appropriate datetime format.
* Create useful date-based features.
* Analyze sales, profit, and quantity across different categories.
* Analyze regional and customer-segment performance.
* Study the relationship between discount and profit.
* Analyze yearly sales and profit trends.
* Analyze sub-category performance.
* Detect potential outliers using the IQR method.
* Analyze correlations between numerical variables.
* Create meaningful visualizations to support the analysis.

---

## 📂 Dataset

The project uses a sales dataset containing information about orders, customers, products, categories, regions, sales, profit, quantity, discount, and dates.

The dataset is stored in:

```text
Dataset/
└── Sales.csv
```

### Major Dataset Attributes

Some of the important attributes used in the analysis include:

* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer information
* Segment
* Region
* Category
* Sub-Category
* Sales
* Quantity
* Discount
* Profit

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **VS Code** – Development environment

---

## 🔍 Exploratory Data Analysis Process

### 1. Dataset Exploration

The initial structure of the dataset is examined using:

* First five records
* Dataset shape
* Column names
* Data types
* Statistical summary

This helps understand the overall structure and characteristics of the dataset.

---

### 2. Data Quality Analysis

The dataset is checked for:

* Missing values
* Duplicate rows
* Completely empty rows
* Rows containing missing values except for the Row ID
* Missing Order Date values

These checks help identify potential data-quality problems before performing further analysis.

---

### 3. Data Cleaning

Rows with missing `Order Date` values are removed from the dataset.

A cleaned copy of the dataset is created so that the original data remains unchanged.

The dataset is then checked again for missing values and duplicate records after cleaning.

---

### 4. Date Conversion

The following columns are converted into datetime format:

```text
Order Date
Ship Date
```

This allows date-based calculations and time-series analysis.

---

### 5. Feature Engineering

New features are created from the order and shipping dates:

```text
Order Year
Order Month
Shipping Days
```

These features help analyze yearly trends, monthly patterns, and shipping duration.

---

## 📊 Category-wise Analysis

Sales, profit, and quantity are aggregated according to product category.

The analysis helps understand the contribution of different product categories to overall business performance.

---

## 🌎 Region-wise Analysis

Sales, profit, and quantity are analyzed across different regions.

This helps identify differences in business performance across geographical areas.

---

## 👥 Customer Segment Analysis

The dataset is analyzed based on customer segments.

Sales, profit, and quantity are calculated for each segment to understand their contribution to the overall business.

---

## 💰 Discount vs Profit Analysis

The relationship between discount and profit is analyzed using:

* Discount-wise aggregation
* Sales and profit comparison
* Correlation analysis
* Scatter plot

The correlation coefficient is calculated to understand the strength and direction of the linear relationship between discount and profit.

> Correlation indicates statistical association and does not by itself establish causation.

---

## 📈 Year-wise Sales and Profit Analysis

Sales and profit are aggregated by year.

Two separate visualizations are created:

* Year-wise Sales Trend
* Year-wise Profit Trend

These visualizations help examine how sales and profit change over time.

---

## 📦 Sub-Category Analysis

Sales, profit, and quantity are analyzed for individual product sub-categories.

A bar chart is created to visualize profit across sub-categories.

This helps identify sub-categories with relatively higher or lower total profit.

---

## 🚨 Outlier Analysis

Potential outliers are identified using the **Interquartile Range (IQR)** method.

The analysis is performed for:

* Sales
* Profit

The following are calculated:

* First Quartile (Q1)
* Third Quartile (Q3)
* Interquartile Range (IQR)
* Lower Bound
* Upper Bound

Separate counts are calculated for sales and profit outliers.

---

## 🔗 Correlation Analysis

Correlation is calculated between the following numerical variables:

```text
Sales
Quantity
Discount
Profit
```

A correlation matrix is generated to examine the relationships between these variables.

A heatmap is then created for easier visual interpretation.

---

## 📊 Visualizations

The project generates the following visualizations:

### 1. Discount vs Profit

A scatter plot showing the relationship between discount and profit.

### 2. Year-wise Sales Trend

A line chart showing sales across different years.

### 3. Year-wise Profit Trend

A line chart showing profit across different years.

### 4. Profit by Sub-Category

A bar chart showing total profit for different product sub-categories.

### 5. Correlation Heatmap

A heatmap showing correlations between:

* Sales
* Quantity
* Discount
* Profit

---

## 📁 Project Structure

```text
TASK_2/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── Dataset/
│   └── Sales.csv
│
├── notebooks/
│   └── EDA.py
│
└── visualizations/
    ├── correlation_heatmap.png
    ├── discount_vs_profit.png
    ├── subcategory_profit.png
    ├── yearly_profit_trend.png
    └── yearly_sales_trend.png
```

---

## ▶️ How to Run the Project

### Step 1: Open the TASK_2 folder

Open the `TASK_2` folder in VS Code.

### Step 2: Install the required libraries

Run:

```bash
pip install -r requirements.txt
```

### Step 3: Run the EDA script

Because the Python file is inside the `notebooks` folder, run:

```bash
python notebooks/EDA.py
```

The analysis results will be displayed in the terminal.

The generated visualizations will be saved automatically inside:

```text
visualizations/
```

---

## 📌 Data Processing Workflow

```text
Raw Sales Dataset
       ↓
Dataset Exploration
       ↓
Data Quality Checking
       ↓
Missing Value Analysis
       ↓
Data Cleaning
       ↓
Date Conversion
       ↓
Feature Engineering
       ↓
Category / Region / Segment Analysis
       ↓
Trend Analysis
       ↓
Outlier Detection
       ↓
Correlation Analysis
       ↓
Data Visualization
       ↓
Meaningful Insights
```

---

## 📈 Key Questions Explored

The analysis investigates questions such as:

1. What is the overall structure of the dataset?
2. Are there missing values or duplicate records?
3. Which categories contribute to sales and profit?
4. How does performance vary across regions?
5. How do different customer segments perform?
6. What is the relationship between discount and profit?
7. How do sales change over the years?
8. How does profit change over the years?
9. Which sub-categories generate higher or lower profit?
10. Are there potential outliers in sales and profit?
11. How are sales, quantity, discount, and profit correlated?

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Exploratory Data Analysis using Python
* Data cleaning and preprocessing
* Missing-value analysis
* Duplicate detection
* Date conversion
* Feature engineering
* Group-by analysis using Pandas
* Statistical analysis
* Outlier detection using IQR
* Correlation analysis
* Data visualization using Matplotlib
* Statistical visualization using Seaborn
* Extracting patterns and insights from real-world data

---

## 💼 Internship Information

**Program:** CodeAlpha Data Analytics Internship

**Task:** Task 2 – Exploratory Data Analysis (EDA)

**Project:** Sales Data Exploratory Data Analysis

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn

---

## 👩‍💻 Author

**Mehak Rathore**

This project was completed as part of the **CodeAlpha Data Analytics Internship**.
