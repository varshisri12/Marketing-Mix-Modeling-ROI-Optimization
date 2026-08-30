import pandas as pd

# Load MMM results
df = pd.read_csv("mmm_results.csv")

channels = {
    "TV": "TV_Spend",
    "Digital": "Digital_Spend",
    "Social": "Social_Spend"
}

results = []

total_marketing_spend = sum(
    df[column].sum()
    for column in channels.values()
)

for channel, spend_column in channels.items():

    spend = df[spend_column].sum()

    # Simple model-based contribution estimate
    contribution = (
        df[spend_column] * 
        df[spend_column].corr(df["Sales"])
    ).sum()

    roi = (contribution - spend) / spend

    results.append({
        "Channel": channel,
        "Spend": spend,
        "Estimated_Contribution": contribution,
        "ROI": roi
    })

roi_df = pd.DataFrame(results)

print("\nROI Analysis:")
print(roi_df)

roi_df.to_csv("roi_analysis.csv", index=False)

print("\nROI analysis completed!")
