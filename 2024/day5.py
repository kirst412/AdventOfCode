# The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes 
# both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. 
# (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

# The second section specifies the page numbers of each update. Because most safety manuals are different, 
# the pages needed in the updates are different too. 
# The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.
import math

with open('day5_in.txt') as fp:
    lst = fp.read().split('\n')

# get a list of each correctly ordered update

# split into the rules and the updates
rules = []
left_side_of_rules = []
right_side_of_rules = []
updates = []
for item in lst:
    if '|' in item:
        rules.append(item)
        left_side_of_rules.append(int(item.split('|')[0]))
        right_side_of_rules.append(int(item.split('|')[1]))
    elif ',' in item:
        updates.append(item)

# print(rules)
# print(updates)
def find(lst, a):
    result = []
    for i,val in enumerate(lst):
        if val == int(a):
            result.append(i)
    return result

def find_values_from_index(lst_of_inds, value_list):
    return [value_list[index] for index in lst_of_inds]

# Okay now loop through each update item
correct_updates = []
incorr_updates = []
for item in updates:
    list_of_numbers = item.split(',')
    list_of_numbers = [int(val) for val in list_of_numbers]
    processed_numbers = []
    cor_update = []
    for number in list_of_numbers:
        # find all instances of this number on the right side
        indeces_of_value = find(right_side_of_rules, number)
        numbers_that_must_be_in_processed = find_values_from_index(indeces_of_value, left_side_of_rules)
        truth_list = []
        for num in numbers_that_must_be_in_processed:
            if num in list_of_numbers:
                if num in processed_numbers:
                    truth_list.append(True)
                else:
                    truth_list.append(False)
        if all(truth_list):
            cor_update.append(True)
        else:
            cor_update.append(False)
        processed_numbers.append(number)
    if all(cor_update):
        correct_updates.append(item)
    else:
        incorr_updates.append(item)
        print(cor_update)

sum = 0

print(len(correct_updates))
print(len(updates))
print(len(incorr_updates))

for updt in correct_updates:
    list_of_numbers = updt.split(',')
    # print(list_of_numbers)
    sum += int(list_of_numbers[int(math.trunc(len(list_of_numbers)/2))])
    # print(int(list_of_numbers[int(math.trunc(len(list_of_numbers)/2))]))

print(sum)

def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

correct_updates_b = []

for item in incorr_updates:
    cor_update = [False]
    list_of_numbers = item.split(',')
    list_of_numbers = [int(val) for val in list_of_numbers]
    while not all(cor_update):
        processed_numbers = []
        cor_update = []
        indeces_to_swap = []
        for i,number in enumerate(list_of_numbers):
            # find all instances of this number on the right side
            indeces_of_value = find(right_side_of_rules, number)
            numbers_that_must_be_in_processed = find_values_from_index(indeces_of_value, left_side_of_rules)
            truth_list = []
            for num in numbers_that_must_be_in_processed:
                if num in list_of_numbers:
                    if num in processed_numbers:
                        truth_list.append(True)
                    else:
                        # we need to swap the number
                        truth_list.append(False)
                        indeces_to_swap.append((i, list_of_numbers.index(num)))
            if all(truth_list):
                cor_update.append(True)
            else:
                cor_update.append(False)
                
            processed_numbers.append(number)
        if all(cor_update):
            correct_updates_b.append(list_of_numbers)
        else:
            list_of_numbers = swap_elements(list_of_numbers, indeces_to_swap[0][0], indeces_to_swap[0][1])

print(correct_updates_b)

    
sum = 0
print(len(incorr_updates))
print(len(correct_updates_b))

for updt in correct_updates_b:
    list_of_numbers = updt
    # print(list_of_numbers)
    sum += int(list_of_numbers[int(math.trunc(len(list_of_numbers)/2))])
    # print(int(list_of_numbers[int(math.trunc(len(list_of_numbers)/2))]))

print(sum)




