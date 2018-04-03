import pandas as pd
import numpy as np
from datetime import datetime
import ast

full_data=pd.read_csv('added_rows.csv',delimiter=',')

full_data['crew_first_film'] = 0
full_data['crew_vote_average'] = 0
crew_vote_dict={}
crew_vote_average = []
crew_first_film = []
for index in range(0,len(full_data)):
    row_crew=ast.literal_eval(full_data['crew'][index])
    crew_vote = []
    first_film = 0
    for actor in row_crew:
        if actor['name'] not in crew_vote_dict:
            first_film = first_film + 1
        else:
            crew_vote.extend(crew_vote_dict[actor['name']])
    if len(crew_vote) != 0:
        crew_vote_average.append(sum(crew_vote)/float(len(crew_vote)))
    else:
        crew_vote_average.append(0)
    crew_first_film.append(first_film)
    for actor in row_crew:
        if actor['name'] not in crew_vote_dict:
            crew_vote_dict[actor['name']] = []
        crew_vote_dict[actor['name']].append(full_data['rating'][index])

    if index%100 == 0:
        print(index)

full_data['crew_first_film'] = crew_first_film
full_data['crew_vote_average'] = crew_vote_average
full_data.to_csv('added_rows.csv',sep=',', index=False)
