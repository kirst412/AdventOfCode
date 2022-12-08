# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')

from collections import defaultdict

count = 0

for group in lst:
    group1 = group.split(",")[0]
    group2 = group.split(",")[1]
    group1num1 = int(group1.split("-")[0])
    group1num2 = int(group1.split("-")[1]) + 1
    group2num1 = int(group2.split("-")[0])
    group2num2 = int(group2.split("-")[1]) + 1
    range1 = [i for i in range(group1num1,group1num2)]
    range2 = [i for i in range(group2num1,group2num2)]
    sec1_len = len(range1)
    sec2_len = len(range2)
    truth_list = []
    # find the smaller length section, then check if each of those digits are in the other
    if sec1_len < sec2_len:
        # check if 1st list is in second list
        for i in range1:
            if i in range2:
                truth_list.append(True)
            else:
                truth_list.append(False)
    else:
        # check if second list is in first list
        for i in range2:
            if i in range1:
                truth_list.append(True)
            else:
                truth_list.append(False)
    if all(truth_list):
        count += 1
        # print(range1, range2)

print(count)

count = 0

for group in lst:
    group1 = group.split(",")[0]
    group2 = group.split(",")[1]
    group1num1 = int(group1.split("-")[0])
    group1num2 = int(group1.split("-")[1]) + 1
    group2num1 = int(group2.split("-")[0])
    group2num2 = int(group2.split("-")[1]) + 1
    range1 = [i for i in range(group1num1,group1num2)]
    range2 = [i for i in range(group2num1,group2num2)]
    sec1_len = len(range1)
    sec2_len = len(range2)
    truth_list = []
    # find the smaller length section, then check if each of those digits are in the other
    if sec1_len < sec2_len:
        # check if 1st list is in second list
        for i in range1:
            if i in range2:
                truth_list.append(True)
            else:
                truth_list.append(False)
    else:
        # check if second list is in first list
        for i in range2:
            if i in range1:
                truth_list.append(True)
            else:
                truth_list.append(False)
    if any(truth_list):
        count += 1
        # print(range1, range2)

print(count)


