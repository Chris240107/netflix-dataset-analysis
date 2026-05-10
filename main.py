import pandas as pd

data = pd.read_csv('netflix_titles.csv') #giving pandas access to the csv

#understanding the dataset
print(data.head())
print(data.info())
print(data.isnull().sum())

