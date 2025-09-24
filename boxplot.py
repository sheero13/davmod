import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset using a raw string for the file path
df = pd.read_csv('housing.csv')

selected_columns = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']
selected_data = df[selected_columns]

# Calculate the correlation matrix
#correlation_matrix = selected_data.corr()

# Display the correlation matrix as a heatmap
#plt.figure(figsize=(12, 10))
for i in selected_data:
    sns.boxplot(df[i])
    plt.title('Correlation Matrix')
    plt.show()
