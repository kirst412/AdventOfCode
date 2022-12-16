# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


# each digit is a tree height, 0 is shortest 9 is tallest
# list of string digits

# print(lst)
# print("rows ", len(lst))
# print("columns ", len(lst[0]))

# the grid is 99 by 99 grid
# all trees along the edge are visible
# a tree is visible if all other trees between it and an edge of the grid are shorter than it.  only look along rows or columns
# sum up all visible trees

# first, add all edges
total = 0
total += len(lst) * 2 + (len(lst[0]) - 2) * 2

def check_rows(row, column_id):
    truth_list = []
    for i in range(column_id):
        if row[column_id] > row[i]:
            truth_list.append(True)
        else:
            truth_list.append(False)
    if all(truth_list):
        return True
    rev_row = "".join(list(reversed(row)))
    # now check right side
    truth_list = []
    prior = rev_row[0]
    for i in range(len(row)-column_id-1):
        if row[column_id] > rev_row[i]:
            truth_list.append(True)
            prior = rev_row[i]
        else:
            truth_list.append(False)
            prior = rev_row[i]
    if all(truth_list):
        return True
    return False

def count_score(row, column_id):
    # splice to left and right
    left = row[:column_id]  # does not include the tree
    right = row[-(len(row) - column_id - 1):]  # does not include the tree
    # print(left)
    # print(right)
    # for the left one, start at the right and count until it is greater than or equal to tree value
    # for the right one, start at the left and count until it is greater than or equal to tree value
    score_1 = 0
    tree_value = row[column_id]
    # right is easier
    for i,val in enumerate(right):
        if val < tree_value:
            score_1 += 1
        elif val >= tree_value:
            score_1 += 1
            break

    # print(score)
    score_2 = 0
    for i,val in enumerate("".join(list(reversed(left)))):
        # print(val)
        if val < tree_value:
            score_2 += 1
        elif val >= tree_value:
            score_2 += 1
            break

    return score_2 * score_1



def convert_columns_to_list(list, column_id):
    column = []
    for i, row in enumerate(list):
        column.append(row[column_id])
    return "".join(column)


# iterate through each cell except first and last rows, first and last columns.  add to total if lower than one of the four sides
total_not_work = []
total_work = []
for i,row in enumerate(lst):
    if i != 0 and i != (len(lst) - 1):
        for j,value in enumerate(row):
            if j != 0 and j != len(row) - 1:
                # edges are eliminated, check tree heights
                if check_rows(row, j):
                    total += 1
                    total_work.append([i,j])
                else:
                    column_to_check = convert_columns_to_list(lst, j)
                    if check_rows(column_to_check, i):
                        total += 1
                        total_work.append([i,j])
                    else:
                        total_not_work.append([i,j])

print(total)

# print(total_work)
# print(total_not_work)


# temp = convert_columns_to_list(lst, 5)
# # 1, 5 should not work
# print(temp)
# print(check_rows(temp, 1))

# between 744 and 2002, not 1410

# part 2
score_map = defaultdict(int)
for i, row in enumerate(lst):
    for j, value in enumerate(row):
        score_map["{},{}".format(i,j)] = count_score(row, j) * count_score(convert_columns_to_list(lst, j), i)

print(score_map)
print(max(score_map.values()))

# 0,2 is wrong

# print(count_score(lst[0], 2))