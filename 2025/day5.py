with open('data/day5_in.txt') as fp:
    lst = fp.read().split('\n')

def split_ranges(lst):
    ranges = []
    to_check = []
    for string in lst:
        if '-' in string:
            ranges.append(string)
        elif string != '':
            to_check.append(string)
    return ranges, to_check

ranges, to_check = split_ranges(lst)

full_range = []
for ran in ranges:
    low, high = ran.split('-')
    low = int(low)
    high = int(high)
    inclusive_list = list(range(low, high + 1))
    full_range.extend(inclusive_list)

total = 0
for item in to_check:
    if int(item) in full_range:
        total += 1

print(total)