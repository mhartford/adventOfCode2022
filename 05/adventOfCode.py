import os
def get_stacks(stack_array):
    stacks = []
    for i in range(9):
        stack = []
        stacks.append(stack)
    for line in stack_array:
        if line.strip().startswith("["):
            print(line.strip())
            cols = [0, 4, 8, 12, 16, 20, 24, 28, 32]
            for i in range(9):
                item = line.strip()[cols[i]:cols[i]+3].strip()
                if len(item.strip()) > 0:
                    print("putting " + item + " on stack " + str(i))
                    stacks[i].append(item)
    return stacks
def process_move(instructions, stacks):
    moves = instructions.strip().split(" ")
    count = int(moves[1])
    source = int(moves[3])
    target = int(moves[5])
    move_item(count, source, target, stacks)
def move_item(count, source, target, stacks):
    print("moving " + str(count) + " items from stack " + str(source) + " to stack " + str(target))
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "05.txt")
lines = open(inputFile, 'r').readlines()
stacks_def = []
stacks = []
for line in lines:
    if line.strip().startswith("["):
        stacks_def.append(line.strip())
    elif line.strip().startswith("move"):
        process_move(line.strip(), stacks)
    else:
        stacks = get_stacks(stacks_def)
