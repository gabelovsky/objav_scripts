#Script for removing unused columns from the data
import pandas as pd
import numpy as np
from datetime import datetime
import ast

full_data=pd.read_csv('full_data.csv',delimiter=';', index_col=0)

full_data = full_data.dropna(subset=['release_date']) 
full_data = full_data[full_data.rating_count!=0]
full_data = full_data[pd.notnull(full_data['rating_count'])]
full_data['cast'] = full_data['cast'].replace('[]',np.nan)
full_data['crew'] = full_data['crew'].replace('[]',np.nan)
full_data = full_data[pd.notnull(full_data['cast'])]
full_data = full_data[pd.notnull(full_data['crew'])]

full_data['release_date'] = pd.to_datetime(full_data['release_date'])

# Split date to year, month, day
full_data['release_date_year'] = full_data['release_date'].dt.year.astype('int64')
full_data['release_date_month'] = full_data['release_date'].dt.month.astype('int64')
full_data['release_date_day'] = full_data['release_date'].dt.day.astype('int64')

full_data = full_data.sort_values(['release_date_year', 'release_date_month', 'release_date_day'], ascending=[True, True, True])
full_data = full_data.reset_index(drop=True)


full_data.to_csv('full_data.csv',sep=';', index=False)