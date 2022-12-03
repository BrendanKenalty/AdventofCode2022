#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:54:50 2022

@author: brendankenalty
"""

#%% Source files
#fPath = "../aoc-2022-Src/"
# f = open(fPath+"d2DemoInputs.txt", "r")
#f = open(fPath+"d2ActualInputs.txt", "r")
# inputs = f.read()

f = open("elfinputday2.txt", "r")
inputs = f.read()
 
# result = inputs.split("\n")
​
inputs = inputs.splitlines() # break each game into element on list
rounds = [line.split(' ') for line in inputs] # separate text sting in 2 elements
#%% Part 1
​
# Maps
# A = rock, B = paper, C= scissors
# X = rock, Y = paper, Z=scissors
​

# build dictionary of scoring element
scoreShapes = {'X':1, 'Y':2, 'Z':3}
scoreOutcome = {'win':6, 'lose':0, 'draw':3}

# ​build scoring matirx (for ecah scenerio)
outcomes = {'A':{'X':'draw','Y':'win','Z':'lose'},
            'B':{'X':'lose','Y':'draw','Z':'win'},
            'C':{'X':'win','Y':'lose','Z':'draw'}}
​
# Rounds
scores = []
for game in rounds:
    pick1 = game[0] #A, B or C - selecting 1st element in list
    pick2 = game[1] #X, Y or Z - slecting 2nd element in list
    outcome = outcomes[pick1][pick2] # using variable to get value in that spot of dictionary
    totalScore = scoreShapes[pick2] + scoreOutcome[outcome] # calc score
    scores.append(totalScore) # make list and add score of that round to list
​
print("Part 1:",sum(scores)) # add up list
​
#%% Part 2
scoreShapes = {'A':1, 'B':2, 'C':3}
scoreOutcome = {'win':6, 'lose':0, 'draw':3}
rules = {'X':'lose', 'Y':'draw', 'Z':'win'}
outcomes = {'A':{'win':'B','lose':'C','draw':'A'},
            'B':{'win':'C','lose':'A','draw':'B'},
            'C':{'win':'A','lose':'B','draw':'C'}}
​
scores = []
for game in rounds:
    # game = rounds[0]
    pick1 = game[0] #A, B or C
    rule = game[1] #X, Y or Z
    outcome = rules[rule]
    pick2 = outcomes[pick1][outcome]
    totalScore = scoreShapes[pick2] + scoreOutcome[outcome]
    scores.append(totalScore)
    
print("Part 2:",sum(scores))
