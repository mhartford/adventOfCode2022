import os
def is_contained(set_one_start, set_one_end, set_two_start, set_two_end):
    contained = False
    if set_one_start >= set_two_start and set_one_end <= set_two_end:
        contained = True
    elif set_two_start >= set_one_start and set_two_end <= set_one_end:
        contained = True
    return contained
def overlaps(set_one_start, set_one_end, set_two_start, set_two_end):
    overlaps = False
    range_one = explode_range(set_one_start, set_one_end)
    range_two = explode_range(set_two_start, set_two_end)
    for i in range_one:
        if i in range_two:
            overlaps = True
            break
    if overlaps == False:
        for i in range_two:
            if i in range_one:
                overlaps = True
                break
    return overlaps
def explode_range(start, end):
    my_range = []
    for i in range(start, end):
        my_range.append(i)
    my_range.append(end)
    return my_range
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "04.txt")
lines = open(inputFile, 'r').readlines()
running_count_contains = 0
running_count_overlaps = 0
for line in lines:
    set_one_start = int(line.strip().split(",")[0].split("-")[0])
    set_one_end = int(line.strip().split(",")[0].split("-")[1])
    set_two_start = int(line.strip().split(",")[1].split("-")[0])
    set_two_end = int(line.strip().split(",")[1].split("-")[1])
    if is_contained(set_one_start, set_one_end, set_two_start, set_two_end):
        running_count_contains = running_count_contains + 1
    if overlaps(set_one_start, set_one_end, set_two_start, set_two_end):
        running_count_overlaps = running_count_overlaps + 1
print(str(running_count_contains))
print(str(running_count_overlaps))