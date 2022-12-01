import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
inputFile = os.path.join(ROOT_PATH, "elf-calories.txt")
file = open(inputFile, 'r')
lines = file.readlines()
runningCalories = 0
maxCalories = 0
calArray = []
for line in lines:
    calories = line.strip()
    if len(calories) > 0:
        runningCalories = runningCalories + int(calories)
        if runningCalories > maxCalories:
            maxCalories = runningCalories
    else:
        calArray.append(runningCalories)
        runningCalories = 0
print("maxCalories = " + str(maxCalories))
calArray.sort(reverse=True)
if len(calArray) >= 3:
    topCals = 0
    for i in range(3):
        topCals = topCals + calArray[i]
    print("top 3 calories = " + str(topCals))