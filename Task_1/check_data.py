import pandas as pd

# Load existing scraped dataset
df = pd.read_csv("products.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Records:")
print(df.head())