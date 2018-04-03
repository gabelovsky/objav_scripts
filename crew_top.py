import pandas as pd
import numpy as np
from datetime import datetime
import ast
import operator

#full_data=pd.read_csv('added_rows.csv',delimiter=',',low_memory=False)

mylist = []
for chunk in  pd.read_csv('added_rows.csv',delimiter=',', chunksize=20000):
    mylist.append(chunk)
print("hereh")
full_data = pd.concat(mylist, axis= 0)
print("kek")
del mylist



crew_dict={}
for index in range(0,len(full_data)):
    row_crew=ast.literal_eval(full_data['crew'][index])
    for crew in row_crew:
        if crew['name'] not in crew_dict:
            crew_dict[crew['name']]=[]
        crew_dict[crew['name']].append(full_data['rating'][index])
    if index%100 == 0:
        print(index)

# vypocet priemeru
crew_dict_average={}
for key, value in crew_dict.items():
    if len(value) < 50:
        continue
    crew_dict_average[key] = sum(value)/float(len(value))
    
sorted_x = sorted(crew_dict_average.items(), key=operator.itemgetter(1)) 
worse = list(list(zip(*(sorted_x[0:100])))[0])
best = list(list(zip(*(sorted_x[-201:-1])))[0])
crew_top = worse + best

crew={}
for crew_i in crew_top:
    crew[crew_i]= [0] * full_data.shape[0]

for index in range(0,len(full_data)):
    row_crew=ast.literal_eval(full_data['crew'][index])
    for actor in row_crew:
        if actor['name'] not in crew:
            continue
        crew[actor['name']][index]=1
    if index%100 == 0:
        print(index)
for crew_i in crew_top:
    full_data[crew_i]= crew[crew_i]

full_data.to_csv('added_rows.csv',sep=',', index=False)
