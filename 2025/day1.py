with open('day1_in.txt') as fp:
    lst = fp.read().split('\n')

# with open('day1_test.txt') as fp:
#     lst = fp.read().split('\n')

current_position = 50

# create a list of 100 booleans, 0 index is True and everything else is False
dial = [False] * 100
dial[0] = True

times_at_0 = 0

for rotation in lst:
    print(current_position, rotation)
    increment = int(rotation[1:])
    if rotation[0] == 'R':
        # dial is increasing value
        new_position = current_position + increment
        while new_position > 99:
            new_position = new_position - 100
            times_at_0 += 1
    if rotation[0] == 'L':
        if current_position  == 0:
            times_at_0 -= 1
        new_position = current_position - increment
        while new_position < 0:
            new_position = new_position + 100
            times_at_0 += 1
        if dial[new_position]:
            times_at_0 += 1
    current_position = new_position
    print(current_position)
    print(times_at_0)
print(times_at_0)