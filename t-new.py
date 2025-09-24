from statsmodels.stats import weightstats as stests
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Padhmapriya\\Desktop\\dav-proj\\WildBlueberryPollinationSimulationData.csv')
Ho = "There is no dependency between total_rooms and median_income" # Stating the Null Hypothesis
Ha = "There is a dependency between total_rooms and median_income" # Stating the Alternate Hypothesis

x = np.array(df[df.total_rooms >= 4000]['median_income'])
y = np.array(df[df.total_rooms < 4000]['median_income'])

p_value  = stests.ttest_ind(x,y)[1]  #Performing an Independent t-test


if p_value < 0.05:  # Setting our significance level at 5%
    print(f'{Ha} as the p_value ({p_value}) < 0.05')
else:
    print(f'{Ho} as the p_value ({p_value}) > 0.05')