# T-Test: Comparing Means of Two Independent Samples
# Null Hypothesis (H_0): The mean house value for homes NEAR OCEAN is equal to the mean for INLAND homes.

# Alternative Hypothesis (H_a): The mean house value for homes NEAR OCEAN is not equal to the mean for INLAND homes.
import pandas as pd
from sklearn.datasets import fetch_california_housing
from scipy import stats

# Load data
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Create two independent samples
near_ocean_val = df[df['OceanProximity'] == 'NEAR OCEAN']['MedHouseVal']
inland_val = df[df['OceanProximity'] == 'INLAND']['MedHouseVal']

# Perform independent t-test
t_stat, p_val = stats.ttest_ind(near_ocean_val, inland_val)
print(f"T-Test: P-value = {p_val:.4f}")
# If p < 0.05, the difference in means is statistically significant.
# Z-Test: Comparing a Sample Mean to a Population Mean
# Null Hypothesis (H_0): The mean value of homes NEAR OCEAN is equal to the overall mean value of all homes.

# Alternative Hypothesis (H_a): The mean value of homes NEAR OCEAN is not equal to the overall mean value of all homes.
from statsmodels.stats.weightstats import ztest

# Sample: NEAR OCEAN homes, Population mean: overall mean
near_ocean_val = df[df['OceanProximity'] == 'NEAR OCEAN']['MedHouseVal']
population_mean_val = df['MedHouseVal'].mean()

# Perform z-test
z_stat, p_val = ztest(x1=near_ocean_val, value=population_mean_val)
print(f"Z-Test: P-value = {p_val:.4f}")
# If p < 0.05, the 'NEAR OCEAN' group's mean is significantly different from the overall mean.
