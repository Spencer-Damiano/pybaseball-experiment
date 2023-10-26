import pandas as pd
import numpy as np
import scipy
import pybaseball
import json


# data = team_batting(2023)
# data.to_json('./json_files/Team_Batting_23.json')

# data_object = json.load(open('./json_files/Team_Batting_23.json'))

# data_formated = json.dumps(data_object, indent=1)

# print(data_formated[0:100])

LAD_batting_23 = pybaseball.team_batting_bref('LAD',2023) # this is a pandas DF

# filter out the pitchers

LAD_batters = LAD_batting_23[LAD_batting_23['Pos'] != 'P']

print(LAD_batters[['Name', 'AB', 'H', 'BA']])

batting_log = pybaseball.team_game_logs(2023, 'LAD')

print(batting_log) # this is what you want to use. See if you can replicate manually the post season data. This might give you enough of a data set
