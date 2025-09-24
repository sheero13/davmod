import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import time


df=pd.read_csv('housing.csv')

selected_columns = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']
selected_data = df[selected_columns]

correlation_matrix = selected_data.corr()

correlation_with_power_consumption = correlation_matrix['population']

print(correlation_with_power_consumption)