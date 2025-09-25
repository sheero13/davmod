UCI heart disease dataset

H₀ (Null): The mean cholesterol level (chol) is the same for patients with and without heart disease.

H₁ (Alt): The mean cholesterol level is different between the two groups.

 import pandas as pd
from scipy import stats

# Load dataset (assuming heart.csv is the UCI Heart Disease dataset)
df = pd.read_csv("heart.csv")

# Split groups
with_disease = df[df["target"] == 1]["chol"]
without_disease = df[df["target"] == 0]["chol"]

# Independent t-test
t_stat, p_val = stats.ttest_ind(with_disease, without_disease)

print("t-statistic:", t_stat)
print("p-value:", p_val)
