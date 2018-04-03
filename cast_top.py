import pandas as pd
import numpy as np
from datetime import datetime
import ast
import operator

full_data=pd.read_csv('added_rows.csv',encoding='utf-8',delimiter=',')

# cast_value_dict={}

# for index, row in full_data.iterrows():
#     row_cast=ast.literal_eval(row['cast'])
#     for actor in row_cast:
#         if actor['name'] not in cast_value_dict:
#             cast_value_dict[actor['name']]=[0,0]
#         cast_value_dict[actor['name']][0]=cast_value_dict[actor['name']][0]+1
#         cast_value_dict[actor['name']][1]=cast_value_dict[actor['name']][1]+row['rating'] 
#     if index%10000 == 0:
#         print(index)
cast_dict={}
for index in range(0,len(full_data)):
    row_cast=ast.literal_eval(full_data['cast'][index])
    for actor in row_cast:
        if actor['name'] not in cast_dict:
            cast_dict[actor['name']]=[]
        cast_dict[actor['name']].append(full_data['rating'][index])
    if index%10000 == 0:
        print(index)
print("second vypocet")
# vypocet priemeru
cast_dict_average={}
# for key, value in cast_value_dict.items():
#     if value[0] < 50:
#          continue
#     cast_dict_average[key] = value[1]/value[0]
for key, value in cast_dict.items():
    if len(value) < 50:
        continue
    cast_dict_average[key] = sum(value)/float(len(value))
    
sorted_x = sorted(cast_dict_average.items(), key=operator.itemgetter(1)) 
print(len(sorted_x))
#worse = list(list(zip(*(sorted_x[0:100])))[0])
best = list(list(zip(*(sorted_x[-101:-1])))[0])
actors = best

cast={}
for actor in actors:
    cast[actor]= [0] * full_data.shape[0]

for index in range(0,len(full_data)):
    row_cast=ast.literal_eval(full_data['cast'][index])
    for actor in row_cast:
        if actor['name'] not in cast:
            continue
        cast[actor['name']][index]=1
    if index%10000 == 0:
        print(index)
print('kek wat')
for actor in actors:
    full_data[actor]= cast[actor]
print("we here boys")

full_data.to_csv('added_rows.csv',sep=',',encoding='utf-8', index=False)