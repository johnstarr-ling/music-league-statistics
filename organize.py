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
submissions = pd.read_csv('./data/submissions.csv')
votes = pd.read_csv('./data/votes.csv')


# Build ID-Competitor dictionary
id2competitor = dict(zip(competitors['ID'], competitors['Name']))

# Build ID-Round dictionary:
id2round = {id:round for round,id in enumerate(rounds['ID'])}


