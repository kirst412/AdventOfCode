# group and sum values that are separated by a blank line

from collections import defaultdict

# import input file as list

with open('input.txt') as fp:
    lst = fp.read().split('\n')

# it reads in as a list of strings
sums = defaultdict(int)
# initialize list of values to sum
tmp = []
counter = 0
for i in lst:
    if i == '':
        # sum list, store in dict, reset tmp
        sums[counter] = sum(tmp)
        counter += 1
        tmp = []
    else:
        tmp.append(int(i))

print(max(sums.values()))

# part 2

sums_sorted = dict(sorted(sums.items(), key=lambda x: x[1],reverse=True))

print(sums_sorted)

top = 3
top_lst = []

sorted_lst = [v for k,v in sums_sorted.items()]

for i in range(top):
    top_lst.append(sorted_lst[i])

print(sum(top_lst))
