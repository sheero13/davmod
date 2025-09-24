import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import time
#import statsmodels.api as sm

df=pd.read_csv('housing.csv')

l=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']#'median_house_value']





for i in l:

    data=df[i]

    mean_value=np.mean(data)
    median_value=np.median(data)
    mode_result = stats.mode(data)
    mode_value = mode_result.mode

    std_dev=np.std(data)

    print(f'mean of {i} - ',mean_value)
    print(f'median of {i} - ',median_value)
    print(f'mode of {i} - ',mode_value)
    print(f'std  of {i} - ',std_dev)
    print('-------------------------------------')
    print()