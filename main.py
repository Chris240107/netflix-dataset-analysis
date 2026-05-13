import pandas as pd
import numpy as np

df = pd.read_csv('netflix_titles.csv') #giving pandas access to the csv

#understanding the dataset
print(df.head())
print(df.info())
missing_values = df.isnull().sum()

print(missing_values)

total_cells = df.size
total_missing = missing_values.sum()

percent_missing = (total_missing / total_cells) * 100 # around 4% of the data is missing.

print(percent_missing)

# fill missing values to have some sort of semblance

#df['country'] = df['country'].fillna(df['country'].mode()[0])
#df['cast'].replace(np.nan, 'No Data', inplace = True)

df.fillna({'director' : 'No Data'}, inplace = True)
df.fillna({'country' : 'No Data'}, inplace = True)
df.fillna({'cast' : 'No Data'}, inplace = True)

print(df.isnull().sum())
df.dropna(inplace = True)
print(df.isnull().sum())
