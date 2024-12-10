######################################################### 
##### IMPORTS 
######################################################### 

import numpy as np 
import pandas as pd 



######################################################### 
##### DATA LOADING 
######################################################### 

competitors = pd.read_csv('./data/competitors.csv')
rounds = pd.read_csv('./data/rounds.csv')
submissions = pd.read_csv('./data/submissions.csv', encoding='utf8')
votes = pd.read_csv('./data/votes.csv', encoding='utf8')


# Build ID-Competitor dictionary
id2competitor = dict(zip(competitors['ID'], competitors['Name']))

# Build ID-Round dictionary
id2round = dict(zip(rounds['ID'], rounds['Name']))

# Build a function that transforms submissions into dictionary (easy access across sheets)
def create_submission_dict(dataframe):
    return dataframe.set_index('Spotify URI').to_dict(orient='index')

# Srujan messed up his name SMH
def fix_srujan(string):
    if string == 'Vivek Dadi':
        return 'Srujan Dadi'
    return string

submission_dict = create_submission_dict(submissions)


######################################################### 
##### BUILDING output_master.csv 
######################################################### 

# Matching up submitter, song name, song artist, and submitter description for every vote
votes['Submitter'] = votes['Spotify URI'].apply(lambda x: id2competitor[submission_dict[x]['Submitter ID']]).apply(fix_srujan)
votes['Song Title'] = votes['Spotify URI'].apply(lambda x: submission_dict[x]['Title'])
votes['Artist'] = votes['Spotify URI'].apply(lambda x: submission_dict[x]['Artist(s)'])
votes['Submitter Description'] = votes['Spotify URI'].apply(lambda x: submission_dict[x]['Comment'])

# Transforming abstract IDs to names
votes['Voter ID'] = votes['Voter ID'].apply(lambda x: id2competitor[x]).apply(fix_srujan)
votes['Round ID'] = votes['Round ID'].apply(lambda x: id2round[x])

votes.to_csv('./outputs/output_master.csv', index=False)



