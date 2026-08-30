import pandas as pd
import numpy as np

# Reproducible results
np.random.seed(42)

# Number of weeks
n_weeks = 104

# Weekly dates
weeks = pd.date_range(
    start="2024-01-01",
    periods=n_weeks,
    freq="W-MON"
)

# Week number
week_number = np.arange(1, n_weeks + 1)

# Marketing spends
tv_spend = np.random.normal(50000, 12000, n_weeks)
tv_spend = np.clip(tv_spend, 15000, 85000)

digital_spend = np.random.normal(35000, 9000, n_weeks)
digital_spend = np.clip(digital_spend, 10000, 60000)

social_spend = np.random.normal(20000, 5000, n_weeks)
social_spend = np.clip(social_spend, 5000, 35000)

# Promotion indicator
promotion = np.random.binomial(1, 0.30, n_weeks)

# Product price
price = (
    100
    + 2 * np.sin(2 * np.pi * week_number / 26)
    + np.random.normal(0, 1.5, n_weeks)
)

# Distribution percentage
distribution = (
    75
    + 5 * np.sin(2 * np.pi * week_number / 52)
    + np.random.normal(0, 2, n_weeks)
)

distribution = np.clip(distribution, 65, 95)

# Seasonal effect
seasonality = 1 + 0.12 * np.sin(
    2 * np.pi * week_number / 52
)

# Generate realistic sales
sales = (
    250000
    + 1.8 * tv_spend
    + 2.5 * digital_spend
    + 2.0 * social_spend
    + 45000 * promotion
    - 3500 * price
    + 2500 * distribution
)

sales = sales * seasonality

# Add random business noise
sales = sales + np.random.normal(0, 25000, n_weeks)

# Create dataframe
df = pd.DataFrame({
    "Week": weeks,
    "Sales": np.round(sales, 0),
    "TV_Spend": np.round(tv_spend, 0),
    "Digital_Spend": np.round(digital_spend, 0),
    "Social_Spend": np.round(social_spend, 0),
    "Promotion": promotion,
    "Price": np.round(price, 2),
    "Distribution": np.round(distribution, 2)
})

# Save dataset
df.to_csv("marketing_data.csv", index=False)

print("Marketing dataset created successfully!")
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())
