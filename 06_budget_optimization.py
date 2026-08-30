import pandas as pd
from scipy.optimize import minimize

# Current marketing budget
total_budget = 1000000

# Channel minimum and maximum budgets
minimum_budget = {
    "TV": 100000,
    "Digital": 100000,
    "Social": 50000
}

maximum_budget = {
    "TV": 600000,
    "Digital": 600000,
    "Social": 400000
}

# Estimated ROI assumptions
roi = {
    "TV": 1.0,
    "Digital": 2.0,
    "Social": 1.5
}

channels = ["TV", "Digital", "Social"]


# Objective function
def objective(budget):

    expected_return = 0

    for i, channel in enumerate(channels):
        expected_return += budget[i] * roi[channel]

    return -expected_return


# Budget constraint
def budget_constraint(budget):

    return sum(budget) - total_budget


# Starting allocation
initial_budget = [
    400000,
    350000,
    250000
]


# Bounds
bounds = [
    (minimum_budget[channel], maximum_budget[channel])
    for channel in channels
]


# Optimization
result = minimize(
    objective,
    initial_budget,
    method="SLSQP",
    bounds=bounds,
    constraints={
        "type": "eq",
        "fun": budget_constraint
    }
)


# Results
optimized_budget = result.x

optimization_result = pd.DataFrame({
    "Channel": channels,
    "Recommended_Budget": optimized_budget
})

print("\nRecommended Marketing Budget:")
print(optimization_result)

optimization_result.to_csv(
    "optimized_budget.csv",
    index=False
)

print("\nBudget optimization completed!")
