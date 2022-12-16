# imports
from collections import defaultdict


# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')


# each digit is a tree height, 0 is shortest 9 is tallest
# list of string digits

print(lst)
print("rows ", len(lst))
print("columns ", len(lst[0]))

# the grid is 99 by 99 grid
# all trees along the edge are visible
# a tree is visible if all other trees between it and an edge of the grid are shorter than it.  only look along rows or columns
# sum up all visible trees

# first, add all edges
total = 0
total += len(lst) * 2 + (len(lst[0]) - 2) * 2

def check_rows(row, column_id):
    truth_list = []
    prior = row[0]
    for i in range(column_id):
        if row[column_id] > row[i]:
            truth_list.append(True)
            prior = row[i]
        else:
            truth_list.append(False)
            prior = row[i]
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

