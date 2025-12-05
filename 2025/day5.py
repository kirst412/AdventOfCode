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

# can't do full range, run out of memory

total = 0
fresh_ranges = []
for item in to_check:
    in_range = False
    for ran in ranges:
        low, high = ran.split('-')
        low = int(low)
        high = int(high)
        fresh_ranges.append((low, high))
        if int(item) >= low and int(item) <= high:
            in_range = True

    if in_range:
        total += 1

print(total)

#now I have a list of all the fresh ranges.  I need to somehow get all values and count uniques
# sort by low value
fresh_ranges.sort()

merged_ranges = []
for low, high in fresh_ranges:
    if len(merged_ranges) == 0:
        merged_ranges.append([low, high])
    else:
        last_low = merged_ranges[-1][0]
        last_high = merged_ranges[-1][1]
        if low <= last_high:
            if high > last_high:
                merged_ranges[-1][1] = high
        else:
            merged_ranges.append([low, high])

# now that we have all the ranges merged, count the number of values within the ranges
total_2 = 0
for low, high in merged_ranges:
    total_2 += (high + 1) - low

print(total_2)
