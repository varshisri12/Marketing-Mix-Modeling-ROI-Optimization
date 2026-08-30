import pandas as pd

# Load dataset
df = pd.read_csv("marketing_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())

# Convert Week column to datetime
df["Week"] = pd.to_datetime(df["Week"])

# Remove duplicate rows
df = df.drop_duplicates()

# Sort data by week
df = df.sort_values("Week")

# Save cleaned dataset
df.to_csv("clean_marketing_data.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as clean_marketing_data.csv")
