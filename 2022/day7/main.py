# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


# ignore anything with $ in front
# the if a line starts with a number, that's the file size
# loop through, if first char is an int, split on " " and add to total file size
total = 0
previous = False
dir_total = 0
# get a list of all the directories
dir_list = defaultdict(int)
for cmd in lst:
    potential_int = cmd.split(" ")[0]
    if potential_int == "dir":
        dir_list[(cmd.split(" ")[1])] = 0
        # Now get the size of that directory

print(dir_list)
