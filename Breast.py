from sklearn.datasets import load_breast_cancer
from scipy import stats
import pandas as pd

# Load dataset
data = load_breast_cancer(as_frame=True)
df = data.frame

# Split groups based on target
malignant = df[df["target"] == 0]["mean radius"]
benign = df[df["target"] == 1]["mean radius"]

# Independent t-test
t_stat, p_val = stats.ttest_ind(malignant, benign)

print("t-statistic:", t_stat)
print("p-value:", p_val)
