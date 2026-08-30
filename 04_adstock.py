import pandas as pd

def calculate_adstock(spend, decay_rate):
    adstock = []
    previous_value = 0

    for value in spend:
        current_value = value + (decay_rate * previous_value)
        adstock.append(current_value)
        previous_value = current_value

    return adstock


# Load data
df = pd.read_csv("clean_marketing_data.csv")

# Calculate adstock
df["TV_Adstock"] = calculate_adstock(
    df["TV_Spend"],
    0.5
)

df["Digital_Adstock"] = calculate_adstock(
    df["Digital_Spend"],
    0.3
)

df["Social_Adstock"] = calculate_adstock(
    df["Social_Spend"],
    0.4
)

# Save
df.to_csv("adstock_data.csv", index=False)

print("Adstock calculation completed!")
