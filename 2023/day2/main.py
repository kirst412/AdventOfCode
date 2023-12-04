

valid_nums = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as fp:
    data = fp.read().split('\n')

sum = 0

for data_row in data:
    id = data_row.split(":")[0].split(' ')[1]
    truth_list = []
    for hand in data_row.split(":")[1].split(";"):
        hand_truth = []
        for block in hand.split(','):
            if block.split(' ')[0] == "":
                number = block.split(' ')[1]
                color = block.split(' ')[2]
            else:
                number = block.split(' ')[0]
                color = block.split(' ')[1]
            if int(number) <= valid_nums[color]:
                hand_truth.append(True)
            else:
                hand_truth.append(False)
        if all(hand_truth):
            truth_list.append(True)
        else:
            truth_list.append(False)
    if all(truth_list):
        sum += int(id)

print(sum)

sum = 0

for data_row in data:
    # Now find the min of each
    min_dict = {'red': 0, 'green': 0, 'blue': 0}
    for hand in data_row.split(":")[1].split(";"):
        for block in hand.split(','):
            if block.split(' ')[0] == "":
                number = block.split(' ')[1]
                color = block.split(' ')[2]
            else:
                number = block.split(' ')[0]
                color = block.split(' ')[1]
            if int(number) > int(min_dict[color]):
                min_dict[color] = number
    sum += int(min_dict['red']) * int(min_dict['blue']) * int(min_dict['green'])

print(sum)