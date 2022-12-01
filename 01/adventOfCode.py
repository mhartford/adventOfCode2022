import os
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "elf-calories.txt")
lines = open(inputFile, 'r').readlines()
runningCalories = 0
calArray = []
for line in lines:
    calories = line.strip()
    if len(calories) > 0:
        runningCalories = runningCalories + int(calories)
    else:
        calArray.append(runningCalories)
        runningCalories = 0
calArray.sort(reverse=True)
print("max calories=" + str(calArray[0]))
if len(calArray) >= 3:
    topCals = 0
    for i in range(3):
        topCals = topCals + calArray[i]
    print("top 3 calories = " + str(topCals))