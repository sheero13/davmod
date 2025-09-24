import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import time

df=pd.read_csv('housing.csv')

l=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']#'median_house_value']
for i in l:

    plt.scatter(df[i], df['population'])
    plt.title(f'{i} population')
    plt.xlabel(f'{i}')
    plt.ylabel('population')
    plt.show()