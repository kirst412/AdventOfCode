with open('day2_in.txt') as fp:
    lst = fp.read().split('\n')


# for each range, get list of numbers, split in half, see if they are the same

list_of_ranges = lst[0].split(',')

print(list_of_ranges)

total = 0

for one_range in list_of_ranges:
    low, high = one_range.split('-')
    low = int(low)
    high = int(high)
    inclusive_list = list(range(low, high + 1))
    for item in inclusive_list:
        item = str(item)
        if len(item)%2 == 0:
            first = item[0:int(len(item)/2)]
            last = item[int(len(item)/2):len(item)]
            if first == last:
                total += int(item)

print(total)

# part 2

total2 = 0

for one_range in list_of_ranges:
    low, high = one_range.split('-')
    low = int(low)
    high = int(high)
    inclusive_list = list(range(low, high + 1))
    for item in inclusive_list:
        item = str(item)
        # see if it matches any previous numbers
        # 123123123, now I know to look for the next few items
        # get all unique characters in the string item
        chars = set([char for char in item])
        print(chars)
        print(item)
        break


