# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')

from collections import defaultdict

# create letter and score mapping
# split each row in half.
# find the letter that is found in each (case sensitive)
# sum total score

lower_list = list(map(chr,range(ord('a'),ord('z')+1)))
upper_list = list(map(chr,range(ord('A'),ord('Z')+1)))

prio_map = defaultdict(int)
counter = 1
for i in lower_list:
    prio_map[i] = counter
    counter += 1
for i in upper_list:
    prio_map[i] = counter
    counter += 1

total = 0

for group in lst:
    first_comp = group[:int(len(group)/2)]
    second_comp = group[int(len(group)/2):len(group)]
    # determine common value
    common = list(set([c for c in first_comp if c in second_comp]))
    total += prio_map[common[0]]

print(total)

# part 2

# find matching character in each group of 3 lines
group_lst = []
counter = 0
group_count = 1
total = 0
for row in lst:
    if group_count == 1:
        group_lst.append([row])
    else:
        group_lst[counter].append(row)
    group_count += 1
    if group_count > 3:
        counter += 1
        group_count = 1

common_lst = []
for group in group_lst:
    common = list(set([c for c in group[0] if c in group[1] and c in group[2]]))
    common_lst.append(common[0])
    total += prio_map[common[0]]

print(total)

