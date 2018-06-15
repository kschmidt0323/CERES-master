# Someday will be a cfg file generator


#this creates the lists for the maps and videos
direc = os.getcwd() # current directory

# makes lists of movies and maps and creates a dictionary that matches them up

movieNames = os.listdir(direc + '\\clips') # create a list of movie names

mapNames = os.listdir(direc + '\\maps') # create a list of map names

answerKey = {} # creates an empty dictionary
answerKey = dict(zip(movieNames, mapNames)) # create dictioary of corresponding movies and maps
print answerKey

randomStimuliNumber = random.randint(0,len(answerKey)) #this is what decides which map/ video / spawn is selected

print "this was the random number" + str(randomStimuliNumber)


#below is how you get spawn coordinates
file = open(direc + '\\LoadTuple', 'r') # opens the tuple generation file containing spawn information

coordinates = {} # holds the spawn values for each trial # THIS IS WHAT THIS CODE IS ALL ABOUT IN THE END # stores the x coordinate, y coordinate, and orientation values

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
        
    coordinates[t] = x,y,ori # stores the x coordinate, y coordinate, and orientation values
    t = t+1

print coordinates


#this defines the parameters for the trial
mapFileName = direc + '\\maps\\' + mapNames[randomStimuliNumber] #this has to adjust based on trial
videoFileName = direc + '\\clips\\' + movieNames[randomStimuliNumber] #this has to adjust based on trial
difficulty = 100 #this adjusts based on performance
xCoor = coordinates[randomStimuliNumber][0] #this adjusts based on trial, gives x cooredinate of spawn
yCoor = coordinates[randomStimuliNumber][1] #this adjusts based on trial, gives y coordinate of spawn
ori = coordinates[randomStimuliNumber][2] #this adjusts based on trial, gives orintation of spawn first person
