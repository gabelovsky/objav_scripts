#Script for calculating the cast value of the movies
import pandas as pd
import numpy as np
from datetime import datetime
import ast

full_data=pd.read_csv('added_rows.csv',delimiter=',')

cast_vote_dict={}
cast_vote_average = []
cast_first_film = []
for index in range(0,len(full_data)):
    row_cast=ast.literal_eval(full_data['cast'][index])
    cast_vote = []
    first_film = 0
    for actor in row_cast:
        if actor['name'] not in cast_vote_dict:
            first_film = first_film + 1
            cast_vote_dict[actor['name']] = []
        else:
            cast_vote.extend(cast_vote_dict[actor['name']])
        cast_vote_dict[actor['name']].append(full_data['rating'][index])
    if len(cast_vote) != 0:
        cast_vote_average.append(sum(cast_vote)/float(len(cast_vote)))
    else:
        cast_vote_average.append(0)
    cast_first_film.append(first_film)
    for actor in row_cast:
        if actor['name'] not in cast_vote_dict:
            cast_vote_dict[actor['name']] = []
        cast_vote_dict[actor['name']].append(full_data['rating'][index])
    if index%100 == 0:
        print(index)

full_data['cast_first_film'] = cast_first_film
full_data['cast_vote_average'] = cast_vote_average
full_data.to_csv('added_rows.csv',sep=',', index=False)