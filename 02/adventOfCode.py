import os
def get_shape(elfPlay, desiredScore):
    shapeScore = 0
    if elfPlay == "A":
        if desiredScore == "X":
            shapeScore = 3
        elif desiredScore == "Y":
            shapeScore = 1
        elif desiredScore == "Z":
            shapeScore = 2
    if elfPlay == "B":
        if desiredScore == "X":
            shapeScore = 1
        elif desiredScore == "Y":
            shapeScore = 2
        elif desiredScore == "Z":
            shapeScore = 3
    if elfPlay == "C":
        if desiredScore == "X":
            shapeScore = 2
        elif desiredScore == "Y":
            shapeScore =  3
        elif desiredScore == "Z":
            shapeScore = 1
    return shapeScore
def get_score(elfPlay, myPlay):
    shapeScore = 0
    playScore = 0
    if myPlay == "X":
        shapeScore = 1
        if elfPlay == "A":
            playScore = 3
        if elfPlay == "C":
            playScore = 6
    elif myPlay == "Y":
        shapeScore = 2
        if elfPlay == "B":
            playScore = 3
        elif elfPlay == "A":
            playScore = 6
    elif myPlay == "Z":
        shapeScore = 3
        if elfPlay == "B":
            playScore = 6
        elif elfPlay == "C":
            playScore = 3
    return shapeScore + playScore
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rps.txt")
lines = open(inputFile, 'r').readlines()
shapes = ["X","Y","Z"]
runningScore = 0
runningShapes = 0
for line in lines:
    plays = line.strip().split(" ")
    score = get_score(plays[0], plays[1])
    shapeScore = get_shape(plays[0], plays[1])
    second_score = get_score(plays[0], shapes[shapeScore - 1])        
    runningScore = runningScore + score
    runningShapes = runningShapes + second_score
print(str(runningScore))
print(str(runningShapes))