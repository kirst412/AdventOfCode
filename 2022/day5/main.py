# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


# print(lst)
# Need to grab indeces 1-9, then put 11 to the end in a move list
move_list = lst[10:]
initial_stacks = lst[:9]
print(initial_stacks)


