# -Test: Comparing Means of Two Independent Samples
# Null Hypothesis (H_0): The mean radius of malignant tumors is equal to the mean radius of benign tumors.

# Alternative Hypothesis (H_a): The mean radius of malignant tumors is not equal to the mean radius of benign tumors.
import pandas as pd
from sklearn.datasets import load_breast_cancer
from scipy import stats

# Load data
cancer = load_breast_cancer()
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target # 0 for malignant, 1 for benign

# Create two independent samples
malignant_radius = df[df['target'] == 0]['mean radius']
benign_radius = df[df['target'] == 1]['mean radius']

# Perform independent t-test
t_stat, p_val = stats.ttest_ind(malignant_radius, benign_radius)
print(f"T-Test: P-value = {p_val:.4f}")
# If p < 0.05, the difference in means is statistically significant.
# Z-Test: Comparing a Sample Mean to a Population Mean
# Null Hypothesis (H_0): The mean radius of malignant tumors is equal to the overall mean radius of all tumors.

# Alternative Hypothesis (H_a): The mean radius of malignant tumors is not equal to the overall mean radius.
from statsmodels.stats.weightstats import ztest

# Sample: malignant tumors, Population mean: overall mean
malignant_radius = df[df['target'] == 0]['mean radius']
population_mean_radius = df['mean radius'].mean()

# Perform z-test
z_stat, p_val = ztest(x1=malignant_radius, value=population_mean_radius)
print(f"Z-Test: P-value = {p_val:.4f}")
# If p < 0.05, the malignant group's mean is significantly different from the overall mean.
