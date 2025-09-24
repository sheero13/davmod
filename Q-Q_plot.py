import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import time
import statsmodels.api as sm

df=pd.read_csv('housing.csv')

l=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']#'median_house_value']

for i in l:

    data = df[i]
    sm.qqplot(data, line='s')
    plt.title(f'Q-Q Plot for {i}')
    plt.show()