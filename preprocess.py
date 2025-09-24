import pandas as pd


# Load the dataset using a raw string for the file path
df=pd.read_csv('housing.csv')
l=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']#'median_house_value']

# Check and print missing values
print(df.isnull().sum())


# Fill missing values for numrical values with the median
df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True)
#Replace missing string values with mode
#df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# Encoding Categorical Variables
df['ocean_proximity'] = df['ocean_proximity'].map({'NEAR BAY': 0, '<1H OCEAN': 1})
#for dropping a column
#df.drop('Cabin', axis=1, inplace=True)


