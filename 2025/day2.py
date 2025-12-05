with open('data/day2_in.txt') as fp:
    lst = fp.read().split('\n')

# with open('day2_test.txt') as fp:
#     lst = fp.read().split('\n')
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

total = 0

# find all numbers divisible by the number.  make each split and check if they all are equal

for one_range in list_of_ranges:
    low, high = one_range.split('-')
    low = int(low)
    high = int(high)
    inclusive_list = list(range(low, high + 1))
    for item in inclusive_list:
        added = False
        item = str(item)
        if len(item)%2 == 0:
            first = item[0:int(len(item)/2)]
            last = item[int(len(item)/2):len(item)]
            if first == last:
                total += int(item)
                added = True
        if len(item)%3 == 0 and not added:
            first = item[0:int(len(item)/3)]
            middle = item[int(len(item)/3):-int(len(item)/3)]
            last = item[-int(len(item)/3):len(item)]
            if first == middle and middle == last:
                total += int(item)
                added = True
        if len(item)%4 == 0 and not added:
            first = item[0:int(len(item)/4)]
            second = item[int(len(item)/4):int(len(item)/2)]
            third = item[int(len(item)/2):-int(len(item)/4)]
            last = item[-int(len(item)/4):len(item)]
            if first == second == third == last:
                total += int(item)
                added = True
        if len(item)%5 == 0 and not added:
            first = item[0:int(len(item)/5)]
            second = item[int(len(item)/5):int(len(item)/5) * 2]
            third = item[int(len(item)/5) * 2:int(len(item)/5) * 3]
            fourth = item[int(len(item)/5) * 3:-int(len(item)/5)]
            fifth = item[-int(len(item)/5):len(item)]
            if first == second == third == fourth == fifth:
                total += int(item)
                added = True
        if len(item)%6 == 0 and not added:
            mod = 6
            first = item[0:int(len(item)/mod)]
            second = item[int(len(item)/mod):int(len(item)/mod) * 2]
            third = item[int(len(item)/mod) * 2:int(len(item)/mod) * 3]
            fourth = item[int(len(item)/mod) * 3:int(len(item)/mod) * 4]
            fifth = item[int(len(item)/mod) * 4:-int(len(item)/mod)]
            sixth = item[-int(len(item)/mod):len(item)]
            if first == second == third == fourth == fifth == sixth:
                total += int(item)
                added = True
        if len(item)%7 == 0 and not added:
            mod = 7
            first = item[0:int(len(item)/mod)]
            second = item[int(len(item)/mod):int(len(item)/mod) * 2]
            third = item[int(len(item)/mod) * 2:int(len(item)/mod) * 3]
            fourth = item[int(len(item)/mod) * 3:int(len(item)/mod) * 4]
            fifth = item[int(len(item)/mod) * 4:int(len(item)/mod) * 5]
            sixth = item[int(len(item)/mod) * 5:-int(len(item)/mod)]
            seventh = item[-int(len(item)/mod):len(item)]
            if first == second == third == fourth == fifth == sixth == seventh:
                total += int(item)
                added = True
        if len(item)%8 == 0 and not added:
            mod = 8
            first = item[0:int(len(item)/mod)]
            second = item[int(len(item)/mod):int(len(item)/mod) * 2]
            third = item[int(len(item)/mod) * 2:int(len(item)/mod) * 3]
            fourth = item[int(len(item)/mod) * 3:int(len(item)/mod) * 4]
            fifth = item[int(len(item)/mod) * 4:int(len(item)/mod) * 5]
            sixth = item[int(len(item)/mod) * 5:int(len(item)/mod) * 6]
            seventh = item[int(len(item)/mod) * 6:-int(len(item)/mod)]
            eighth = item[-int(len(item)/mod):len(item)]
            if first == second == third == fourth == fifth == sixth == seventh == eighth:
                total += int(item)
                added = True

print(total)
