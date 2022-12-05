import os
def get_stacks(stack_array):
    stacks = []
    for i in range(9):
        stack = []
        stacks.append(stack)
    for line in stack_array:
        if line.strip().startswith("["):
            cols = [0, 4, 8, 12, 16, 20, 24, 28, 32]
            for i in range(9):
                item = line.strip()[cols[i]:cols[i]+3].strip()
                if len(item.strip()) > 0:
                    stacks[i].append(item)
    count = 0
    for stack in stacks:
        count = count + 1
        for item in stack:
            print(item)
        print(str(count))
        count = count + 1
    return stacks
def process_move(instructions, stacks, asGroup):
    moves = instructions.strip().split(" ")
    count = int(moves[1])
    source = int(moves[3])
    target = int(moves[5])
    if asGroup == True:
        move_item_set(count, source, target, stacks)
    else:
        move_item(count, source, target, stacks)
def move_item(count, source, target, stacks):
    for i in range((count)):
        #print("move " + stacks[(source-1)][0] + " to stack " + str(target) + " (" + str(i) + ")")
        stacks[(target-1)].insert(0, stacks[(source-1)][0])
        stacks[(source-1)].pop(0)
def move_item_set(count, source, target, stacks):
    item_set = []
    for i in range(count):
        item_set.insert(0, stacks[source-1][0])
        stacks[(source-1)].pop(0)
    for item in item_set:
        stacks[(target-1)].insert(0, item)
moveAsGroup = True
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "05.txt")
lines = open(inputFile, 'r').readlines()
stacks_def = []
stacks = []
for line in lines:
    if line.strip().startswith("["):
        stacks_def.append(line.strip())
    elif line.strip().startswith("move"):
        process_move(line.strip(), stacks, moveAsGroup)
    else:
        stacks = get_stacks(stacks_def)
tops = ""
for stack in stacks:
    tops = tops + stack[0].replace("[","").replace("]","")
print(tops)