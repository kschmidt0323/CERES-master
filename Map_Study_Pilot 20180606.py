from __future__ import division #so that 1/3=0.333 instead of 1/3=0
__author__ = "reber lab"

# import libraries

import os, sys, random, datetime, time, psychopy
from psychopy import visual, core, data, event, logging, gui, sound
import numpy as np


# Read a configuration file with task parameters, trial order, etc.

'''
Configuration files

‘#’ lines are comments

keyword: parameters…

cfg={}

cfg[[keyword]=parameters
'''

'''
cfg_file=”””

mapfile1.jpg ….

“””
'''




# Administer trials
'''Map Trials:

  Show map
  Overlay circle
  Show video
  Show map
  Overlay circle
  Collect arrow location response
  Collect arrow orientation response
  Give feedback
<name-of-map-file> <location-of-circle> <map-display-time> <name-of-video-file> <x,y,facing>

class MapTrial:

def __init__(self):

self.MapFileName=”

self.LocationOfCircle=(0.0,0.0,0.0)

self.MapDisplayTime=0.0

self.VideoFileName=”

self.Answer=(0.0,0.0,0.0)

def show_map(self):

# call to PsychoPy VisStim
'''









# Write a really dense datalog of everything that happened
'''

datalog=[]

datalog.append(“Something happened”)

f=open(‘output.log’,’w’)

for i in datalog:

f.write(“%s\n” % i)

f.close()
'''






