# T-Test: Comparing Means of Two Independent Samples
# Null Hypothesis (H_0): The mean max heart rate is the same for patients with heart disease and those without.

# Alternative Hypothesis (H_a): The mean max heart rate is different between the two groups.
import pandas as pd
from scipy import stats

# Load data from UCI repository
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
col_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
             'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
df = pd.read_csv(url, header=None, names=col_names)
# Target: 0 = no disease, >0 = disease. Let's make it binary.
df['target'] = (df['target'] > 0).astype(int)

# Create two independent samples
no_disease_hr = df[df['target'] == 0]['thalach']
has_disease_hr = df[df['target'] == 1]['thalach']

# Perform independent t-test
t_stat, p_val = stats.ttest_ind(no_disease_hr, has_disease_hr)
print(f"T-Test: P-value = {p_val:.4f}")
# If p < 0.05, the difference in means is statistically significant.
# Z-Test: Comparing a Sample Mean to a Population Mean
# Null Hypothesis (H_0): The mean max heart rate for patients with heart disease is equal to the overall mean max heart rate of all patients.

# Alternative Hypothesis (H_a): The mean max heart rate for patients with heart disease is not equal to the overall mean max heart rate.
from statsmodels.stats.weightstats import ztest

# Sample: patients with disease, Population mean: overall mean
has_disease_hr = df[df['target'] == 1]['thalach']
population_mean_hr = df['thalach'].mean()

# Perform z-test
z_stat, p_val = ztest(x1=has_disease_hr, value=population_mean_hr)
print(f"Z-Test: P-value = {p_val:.4f}")
# If p < 0.05, the group with heart disease has a mean heart rate significantly different from the overall mean.
