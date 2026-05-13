import pandas as pd
import numpy as np

df = pd.read_csv('netflix_titles.csv') #giving pandas access to the csv

#understanding the dataset

#print(df.info())
#missing_values = df.isnull().sum()

#print(missing_values)

#total_cells = df.size
#total_missing = missing_values.sum()

#percent_missing = (total_missing / total_cells) * 100 # around 4% of the data is missing.

#print(percent_missing)

# fill missing values to have some sort of semblance

#df['country'] = df['country'].fillna(df['country'].mode()[0])
#df['cast'].replace(np.nan, 'No Data', inplace = True)

df.fillna({'director' : 'No Data'}, inplace = True)
df.fillna({'country' : 'No Data'}, inplace = True)
df.fillna({'cast' : 'No Data'}, inplace = True)

#print(df.isnull().sum())
df.dropna(inplace = True)
#print(df.isnull().sum())

#CORE ANALYSIS

#print(df['type'].value_counts()) # Movie      6126, TV Show    2664

#seperates the month from the date to get WHICH month the media was released in
type_and_date = df[['type', 'date_added']].copy()
type_and_date['date_added'] = pd.to_datetime(type_and_date['date_added'], format='mixed')
type_and_date['month_added'] = pd.DatetimeIndex(type_and_date['date_added']).month
type_and_date['year_added'] = pd.DatetimeIndex(type_and_date['date_added']).year
#maybe corelation or causation can be found
#print(type_and_date['month_added'].value_counts())
#print(type_and_date['year_added'].value_counts())


