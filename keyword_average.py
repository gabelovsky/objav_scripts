import pandas as pd
import numpy as np
from datetime import datetime
import ast

full_data=pd.read_csv('full_data.csv',delimiter=';')

keywords_vote_dict={}
keywords_vote_average = []
keywords_first_film = []
for index in range(0,len(full_data)):
    row_keywords=ast.literal_eval(full_data['keywords'][index])
    keywords_vote = []
    first_film = 0
    for keyword in row_keywords:
        if keyword['name'] not in keywords_vote_dict:
            first_film = first_film + 1
            keywords_vote_dict[keyword['name']] = []
        else:
            keywords_vote.extend(keywords_vote_dict[keyword['name']])
        keywords_vote_dict[keyword['name']].append(full_data['rating'][index])
    if len(keywords_vote) != 0:
        keywords_vote_average.append(sum(keywords_vote)/float(len(keywords_vote)))
    else:
        keywords_vote_average.append(0)
    keywords_first_film.append(first_film)

    if index%100 == 0:
        print(index)

full_data['keywords_first_film'] = keywords_first_film
full_data['keywords_vote_average'] = keywords_vote_average
full_data.to_csv('full_data.csv',sep=';', index=False)