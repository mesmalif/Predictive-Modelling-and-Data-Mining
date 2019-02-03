import numpy as np
import pandas as pd
import scipy as sc
import matplotlib
import sklearn

import csv

#upload cvs file 

data = pd.read_csv("Titanic_original.csv")
df = pd.DataFrame(data)


# Drop the columns where all elements are missing values:
A = df.dropna(how='all')

# Drop the columns where any of the elements are missing values
B = df.dropna(how='any')
print B

# Keep only the rows which contain 2 missing values maximum
df.dropna(thresh=2)

# Fill all missing values with the mean of the particular column
df.fillna(df.mean())

# Fill any missing value in column 'A' with the column median
df['Age'].fillna(df['Age'].median())
categorical = data.dtypes[data.dtypes == "object"].index
print(categorical)

titanic_train[categorical].describe()

#delete variables 
del titanic_train["PassengerId"] 