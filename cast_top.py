import pandas as pd
import numpy as np
from datetime import datetime
import ast
import operator

full_data=pd.read_csv('full_data.csv',delimiter=';')
cast_dict={}
for index in range(0,len(full_data)):
    row_cast=ast.literal_eval(full_data['cast'][index])
    for actor in row_cast:
        if actor['name'] not in cast_dict:
            cast_dict[actor['name']]=[]
        cast_dict[actor['name']].append(full_data['rating'][index])
    if index%100 == 0:
        print(index)

# vypocet priemeru
cast_dict_average={}
for key, value in cast_dict.items():
    if len(value) < 50:
        continue
    cast_dict_average[key] = sum(value)/float(len(value))
    
sorted_x = sorted(cast_dict_average.items(), key=operator.itemgetter(1)) 
worse = list(list(zip(*(sorted_x[0:100])))[0])
best = list(list(zip(*(sorted_x[-201:-1])))[0])
actors = worse + best

cast={}
for actor in actors:
    cast[actor]= [0] * full_data.shape[0]

for index in range(0,len(full_data)):
    row_cast=ast.literal_eval(full_data['cast'][index])
    for actor in row_cast:
        if actor['name'] not in cast:
            continue
        cast[actor['name']][index]=1
    if index%100 == 0:
        print(index)

for actor in actors:
    full_data[actor]= cast[actor]

full_data.to_csv('full_data.csv',sep=';', index=False)