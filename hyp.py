# student_data_analysis.py 
import numpy as np 
import pandas as pd 
from scipy import stats 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error 
# Load data 
data = pd.read_csv('students.csv', delimiter=',') 
print(data.head()) 
# Prepare data for analysis 
study_hours = np.array(data['hours']) 
scores = np.array(data['scores']) 
# HYPOTHESIS 
# H0: no correlation between the study hours and the results corr = 0 
# H1: correlation exists corr !=0 
# correlation analysis 
corr_coef, p_value_corr = stats.pearsonr(study_hours, scores) 
print(f"Correlation coefficient: {corr_coef:.3f}, p-val: {p_value_corr:.3e}") 
# simple linear regression 
X = study_hours.reshape(-1, 1) 
model = LinearRegression().fit(X, scores) 
print(f"Intercept: {model.intercept_:.3f}") 
print(f"Slope: {model.coef_[0]:.3f}") 
# predict for demonstration 
pred = model.predict(X) 
print("predicted scores:", pred) 
# Evaluate the model 
print(f"Mean squared error: {mean_squared_error(scores, pred)}")
