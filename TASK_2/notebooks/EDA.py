import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")

df = pd.read_csv("../Dataset/Sales.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())


# Dataset Shape
print("\nDataset Shape:")
print(df.shape)


# Column Names
print("\nColumn Names:")
print(df.columns)


# Dataset Information
print("\nDataset Information:")
print(df.info())


# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())


# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

print("\nCompletely Empty Rows:")
print(df.isnull().all(axis=1).sum())

print("\nRows with all data missing except Row ID:")

blank_data_rows = df.drop(columns=["Row ID"]).isnull().all(axis=1)

print(blank_data_rows.sum())

print("\nRows with missing Order Date:")
print(df[df["Order Date"].isnull()].head(10))
print("\nNumber of rows with missing Order Date:")
print(df["Order Date"].isnull().sum())

# Remove rows where Order Date is missing
clean_df = df.dropna(subset=["Order Date"]).copy()

print("\nOriginal Shape:")
print(df.shape)

print("\nCleaned Shape:")
print(clean_df.shape)

print("\nMissing Values After Cleaning:")
print(clean_df.isnull().sum())

print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())


print("\nSample Duplicate Rows:")
print(clean_df[clean_df.duplicated(keep=False)].head(10))

print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())

print("\nSample Duplicate Rows:")
print(clean_df[clean_df.duplicated(keep=False)].head(10))

# Convert date columns to datetime
clean_df["Order Date"] = pd.to_datetime(clean_df["Order Date"])
clean_df["Ship Date"] = pd.to_datetime(clean_df["Ship Date"])

print("\nData Types After Date Conversion:")
print(clean_df[["Order Date", "Ship Date"]].dtypes)

# Create new date-based features
clean_df["Order Year"] = clean_df["Order Date"].dt.year
clean_df["Order Month"] = clean_df["Order Date"].dt.month
clean_df["Shipping Days"] = (
    clean_df["Ship Date"] - clean_df["Order Date"]
).dt.days

print("\nNew Features:")
print(clean_df[[
    "Order Date",
    "Ship Date",
    "Order Year",
    "Order Month",
    "Shipping Days"
]].head())

# Explore categorical columns

print("\nUnique Values in Segment:")
print(clean_df["Segment"].unique())

print("\nUnique Values in Region:")
print(clean_df["Region"].unique())

print("\nUnique Values in Category:")
print(clean_df["Category"].unique())

print("\nUnique Values in Ship Mode:")
print(clean_df["Ship Mode"].unique())

# Category-wise analysis

category_analysis = clean_df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\nCategory-wise Sales, Profit and Quantity:")
print(category_analysis)


# Region-wise analysis

region_analysis = clean_df.groupby("Region").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\nRegion-wise Sales, Profit and Quantity:")
print(region_analysis)

# Customer segment analysis

segment_analysis = clean_df.groupby("Segment").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\n Customer Segment-wise Sales, Profit and Quantity:")
print(segment_analysis)

# Discount vs Profit analysis

discount_analysis = clean_df.groupby("Discount").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\nDiscount-wise Sales, Profit and Quantity:")
print(discount_analysis)

# Correlation between Discount and Profit

discount_profit_corr = clean_df["Discount"].corr(clean_df["Profit"])

print("\nCorrelation between Discount and Profit:")
print(round(discount_profit_corr, 3))


# Scatter Plot: Discount vs Profit
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean_df,
    x="Discount",
    y="Profit",
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.axhline(0, linestyle="--")

plt.tight_layout()

plt.savefig("../visualizations/discount_vs_profit.png")
plt.show()

# Year-wise Sales and Profit Analysis
year_analysis = clean_df.groupby("Order Year").agg({
    "Sales": "sum",
    "Profit": "sum"
}).round(2)

print("\nYear-wise Sales and Profit:")
print(year_analysis)

# Year-wise Sales Trend
plt.figure(figsize=(8, 5))

sns.lineplot(
    data=year_analysis,
    x=year_analysis.index,
    y="Sales",
    marker="o"
)

plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("../visualizations/yearly_sales_trend.png")
plt.show()

# Year-wise Profit Trend
plt.figure(figsize=(8, 5))

sns.lineplot(
    data=year_analysis,
    x=year_analysis.index,
    y="Profit",
    marker="o"
)

plt.title("Year-wise Profit Trend")
plt.xlabel("Year")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("../visualizations/yearly_profit_trend.png")
plt.show()

# Sub-Category-wise Sales and Profit Analysis
subcategory_analysis = clean_df.groupby("Sub-Category").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\nSub-Category-wise Sales, Profit and Quantity:")
print(subcategory_analysis.sort_values("Profit", ascending=False))

# Sub-Category-wise Profit Visualization

plt.figure(figsize=(10, 7))

subcategory_profit = subcategory_analysis.sort_values("Profit")

sns.barplot(
    x=subcategory_profit["Profit"],
    y=subcategory_profit.index
)

plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

plt.axvline(0, linestyle="--")

plt.tight_layout()

plt.savefig("../visualizations/subcategory_profit.png")
plt.show()

# Outlier Analysis using IQR

Q1 = clean_df[["Sales", "Profit"]].quantile(0.25)
Q3 = clean_df[["Sales", "Profit"]].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = clean_df[
    (clean_df["Sales"] < lower_bound["Sales"]) |
    (clean_df["Sales"] > upper_bound["Sales"]) |
    (clean_df["Profit"] < lower_bound["Profit"]) |
    (clean_df["Profit"] > upper_bound["Profit"])
]

print("\nOutlier Analysis:")
print("Number of Outlier Rows:", len(outliers))

print("\nLower Bounds:")
print(lower_bound)

print("\nUpper Bounds:")
print(upper_bound)

# Separate Outlier Counts

sales_outliers = (
    (clean_df["Sales"] < lower_bound["Sales"]) |
    (clean_df["Sales"] > upper_bound["Sales"])
)

profit_outliers = (
    (clean_df["Profit"] < lower_bound["Profit"]) |
    (clean_df["Profit"] > upper_bound["Profit"])
)

print("\nSales Outliers:", sales_outliers.sum())
print("Profit Outliers:", profit_outliers.sum())


# Correlation Analysis

correlation_matrix = clean_df[
    ["Sales", "Quantity", "Discount", "Profit"]
].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(3))


# Correlation Heatmap

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("../visualizations/correlation_heatmap.png")
plt.show()