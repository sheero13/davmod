Housing dataset

H₀ (Null): The mean house value is the same in high-income areas and low-income areas.

H₁ (Alt): The mean house value is different between high-income and low-income areas.

from sklearn.datasets import fetch_california_housing
from scipy import stats

# Load dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Split into high vs low income groups
median_income = df["MedInc"].median()
high_income = df[df["MedInc"] > median_income]["MedHouseVal"]
low_income = df[df["MedInc"] <= median_income]["MedHouseVal"]

# Perform independent t-test
t_stat, p_val = stats.ttest_ind(high_income, low_income)

print("t-statistic:", t_stat)
print("p-value:", p_val)
