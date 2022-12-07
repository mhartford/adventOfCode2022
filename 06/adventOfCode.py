import os
def find_start_of_packet(input):
    return find_start_of_unit(input, 4)
def find_start_of_message(input):
    return find_start_of_unit(input, 14)
def find_start_of_unit(input, len_of_set):
    chars = []
    chars.extend(input)
    count = 0
    set_of_chars = []
    for char in chars:
        if len(set_of_chars) > (len_of_set - 1):
            set_of_chars.pop(0)
        set_of_chars.append(char)
        if len(set_of_chars) == len_of_set:
            rc = check_for_unique(set_of_chars)
            if rc:
                break
        count = count + 1
    return count + 1
def check_for_unique(myArray):
    unique = False
    running_count = len(myArray)
    for char in myArray:
        for x in myArray:
            if char == x:
                running_count = running_count - 1
    if running_count == 0:
        unique = True
    return unique
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
lines = open(inputFile, 'r').readlines()
for line in lines:
    rc = find_start_of_packet(line.strip())
    print(str(rc))
    rc = find_start_of_message(line.strip())
    print(str(rc))
