# -*- coding: utf-8 -*-
from __future__ import division #so that 1/3=0.333 instead of 1/3=0
__author__ = "Kevin Schmidt - kevin.daniel.schmidt@gmail.com"

# import libraries

import os, sys, random, datetime, time, psychopy, re
from psychopy import visual, core, data, event, logging, gui, sound
import numpy as np

# ID and print the spawn position and orientation from LoadTuple.txt based on commas
#comma 4-5 is X, 5-6 is y, 6-7 is orientation

file = open('LoadTuple.txt', 'r') # opens the tuple generation file containing spawn information

answerKey = {} # holds the spawn values for each trial # THIS IS WHAT THIS CODE IS ALL ABOUT IN THE END # stores the x coordinate, y coordinate, and orientation values

scenes = []
scenes = file.readlines() # makes a list breaking up each line of the text file
t = 0
    
for i in scenes: # indexes each line of the txt file, which equates to indexing each scene information used to generate tuple
    start = 9 # this is the starting index where the data begins
    # print i #prints the whole line from the tuple text file
    end = i.find(',', start + 1)
    x = i[start:end]
    # print x #prints the x axis spawn value for that scene
    start = end + 1
    end = i.find(',', start + 1)
    y = i[start:end - 1]
    # print y Prints the y axis spawn for the scene
    start = end + 1
    end = i.find(',', start + 1)
    ori = i[start:end]
    # print ori #prints the orientation for that scene
        
    answerKey[t] = x,y,ori # stores the x coordinate, y coordinate, and orientation values
    t = t+1
