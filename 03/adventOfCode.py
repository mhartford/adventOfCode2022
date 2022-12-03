import os
def get_duplicate_item(contents):
    duplicate_item = ""
    contents = contents.strip()
    first_pocket = contents[0:(int(len(contents)/2))]
    second_pocket = contents.replace(first_pocket, "")
    for item in list(first_pocket):
        if item in list(second_pocket):
            duplicate_item = item
            break
    return duplicate_item
def get_duplicate_item_score(item):
    score = 0
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    pos_in_alphabet = 0
    for letter in alphabet:
        pos_in_alphabet = pos_in_alphabet + 1
        if item.lower() == letter:
            break
    if item.lower() == item:
        score = pos_in_alphabet
    else:
        score = pos_in_alphabet + 26
    return score
def get_badge(rucksackArray):
    rucksacks_contents = ""
    badge = ""
    for item in list(rucksackArray[0]):
        if item in list(rucksackArray[1]):
            if item in list(rucksackArray[2]):
                badge = item
                break
    return badge
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "03.txt")
lines = open(inputFile, 'r').readlines()
running_score = 0
running_badge_score = 0
rucksack_group = []
for line in lines:
    duplicate_item = get_duplicate_item(line)
    duplicate_item_score = get_duplicate_item_score(duplicate_item)
    running_score = running_score + duplicate_item_score
    rucksack_group.append(line.strip())
    if len(rucksack_group) == 3:
        badge = get_badge(rucksack_group)
        badge_score = get_duplicate_item_score(badge)
        running_badge_score = running_badge_score + badge_score
        rucksack_group = []
print(str(running_score))
print(str(running_badge_score))