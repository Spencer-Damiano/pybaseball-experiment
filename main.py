import pybaseball
import pandas as pd

astros_batting_log = pybaseball.team_game_logs(2017, 'HOU')

grouped = astros_batting_log.groupby('Home').agg({
    'AB': 'sum',                 # Total at-bats
    'H': 'sum',                  # Total hits
    'R': 'sum',                  # Total runs
    'HR': 'sum',                 # Total home runs
    'RBI': 'sum',                # Total RBIs
    'BB': 'sum',                 # Total walks
    'SO': 'sum',                 # Total strikeouts
    'BA': 'mean',                # Average batting average
    'OBP': 'mean',               # Average on-base percentage
    'SLG': 'mean',               # Average slugging percentage
    'OPS': 'mean'                # Average on-base plus slugging
}).reset_index()

print(grouped)