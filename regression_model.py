import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset using a raw string for the file path
df = pd.read_csv('housing.csv')

# Specify the target variable
target_variable = 'population'

# List of features (independent variables)
selected_features = [
    'longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']#'median_house_value']


# Iterate over each feature
for feature in selected_features:
    # Select the feature and target
    X = df[feature].values.reshape(-1, 1)
    y = df[target_variable]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Make predictions on the test data
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f'Feature: {feature}')
    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R-squared: {r2:.2f}')

    # Plot the regression line
    plt.scatter(X_test, y_test, color='black', label='Actual data points')
    plt.plot(X_test, predictions, color='blue', linewidth=3, label='Linear Regression')
    plt.xlabel(feature)
    plt.ylabel(target_variable)
    plt.title(f'Linear Regression Model - {feature} vs {target_variable}')
    plt.legend()
    plt.show()
