# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:47:26 2016

@author: RichardG
"""

import random, pylab
def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    balls = ['r']*4 + ['g']*4
    chosen_balls = random.sample(balls,3)
    if chosen_balls[0] == chosen_balls[1] == chosen_balls[2]:
        return True
    return False

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    num_true = 0
    for trial in range(numTrials):
        if oneTrial() == True:
            num_true += 1
    return float(num_true)/(numTrials)