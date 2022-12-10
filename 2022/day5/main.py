# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


# print(lst)
# Need to grab indeces 1-9, then put 11 to the end in a move list
move_list = lst[10:]
initial_stacks = lst[:9]
# print(initial_stacks)

# convert to stacks 1-9
# initialize stack dictionary
stack_dict = {
    1: ['V','C','D','R','Z','G','B','W'],
    2: ['G','W','F','C','B','S','T','V'],
    3: ['C','B','S','N','W'],
    4: ['Q','G','M','N','J','V','C','P'],
    5: ['T','S','L','F','D','H','B'],
    6: ['J','V','T','W','M','N'],
    7: ['P','F','L','C','S','T','G'],
    8: ['B','D','Z'],
    9: ['M','N','Z','W']
}

def unpack_move(move_str):
    move_lst = move_str.split(' ')
    num_to_move = int(move_lst[1])
    from_stack = int(move_lst[3])
    to_stack = int(move_lst[5])
    return num_to_move,from_stack,to_stack

def execute_move(stk_dct,from_stack,to_stack):
    box_to_move = ''.join(stk_dct[from_stack])[-1]
    stk_dct[to_stack].append(box_to_move)
    stk_dct[from_stack].pop()
    return stk_dct

for move in move_list:
    num_to_move,from_stack,to_stack = unpack_move(move)
    for i in range(num_to_move):
        stack_dict = execute_move(stack_dict,from_stack,to_stack)

print(stack_dict)

for v in stack_dict.values():
    print(v[-1])






