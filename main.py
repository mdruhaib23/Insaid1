#Data cleaning:
import pandas as pd
# load data
data = pd.read_csv("C:\Users\MOHAMMED RUHAIB\Downloads\Fraud.csv")
# check for missing values
print(data.isnull().sum())

# handle missing values
data = data.fillna(data.mean())

# check for outliers
print(data.describe())

# handle outliers
data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]

# check for multi-collinearity
corr = data.corr()
print(corr)

# handle multi-collinearity
data = data.drop(columns=["col1", "col2"])
