import pandas as pd

data = pd.read_csv('netflix_titles.csv') #giving pandas access to the csv

#understanding the dataset
print(data.head())
print(data.info())
missing_values = data.isnull().sum()

total_cells = data.size
total_missing = missing_values.sum()

percent_missing = (total_missing / total_cells) * 100

print(percent_missing)