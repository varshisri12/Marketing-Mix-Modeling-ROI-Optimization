import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("clean_marketing_data.csv")

df["Week"] = pd.to_datetime(df["Week"])

# -----------------------------
# Sales Trend
# -----------------------------

plt.figure(figsize=(12, 5))

plt.plot(df["Week"], df["Sales"])

plt.title("Weekly Sales Trend")
plt.xlabel("Week")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_trend.png")
plt.show()


# -----------------------------
# Marketing Spend
# -----------------------------

plt.figure(figsize=(12, 5))

plt.plot(df["Week"], df["TV_Spend"], label="TV")
plt.plot(df["Week"], df["Digital_Spend"], label="Digital")
plt.plot(df["Week"], df["Social_Spend"], label="Social")

plt.title("Marketing Spend Over Time")
plt.xlabel("Week")
plt.ylabel("Marketing Spend")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("marketing_spend.png")
plt.show()


# -----------------------------
# Correlation
# -----------------------------

correlation = df.corr(numeric_only=True)["Sales"].sort_values(
    ascending=False
)

print("\nCorrelation with Sales:")
print(correlation)
