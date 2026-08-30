import pandas as pd
import statsmodels.api as sm

# Load cleaned data
df = pd.read_csv("clean_marketing_data.csv")

# Independent variables
X = df[
    [
        "TV_Spend",
        "Digital_Spend",
        "Social_Spend",
        "Promotion",
        "Price",
        "Distribution"
    ]
]

# Dependent variable
y = df["Sales"]

# Add intercept
X = sm.add_constant(X)

# Build regression model
model = sm.OLS(y, X).fit()

# Display model results
print(model.summary())

# Predictions
df["Predicted_Sales"] = model.predict(X)

# Save results
df.to_csv("mmm_results.csv", index=False)

print("\nMMM model completed successfully!")
print("Results saved as mmm_results.csv")
