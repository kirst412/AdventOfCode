with open('day3_in.txt') as fp:
    lst = fp.read().split('mul(')

total_sum = 0
counter = 0
mults = []
enabled = True

print(len(lst))
# print(lst)

if "don't" in lst[0]:
    enabled = False

for i,item in enumerate(lst):
    if i != 0:
        # split on ','
        item_split = item.split(',')
        try:
            val_1 = item_split[0]
            val_2 = item_split[1]
            # check if val_1 starts with parens
            try:
                int_1 = int(val_1)
                # Now we can split val_2 on )
                if len(val_2.split(')')) > 1:
                    int_2 = int(val_2.split(')')[0])
                    # if we made it this far, do the mult
                    # print('int_1:',int_1)
                    # print('int_2:', int_2)
                    # print(int_1 * int_2)
                    if enabled:
                        total_sum += (int_1 * int_2)
                    # print(total_sum)
                        counter += 1
                    # print("worked on", item)
                        mults.append(int_1 * int_2)
                    if "don't" in item:
                        enabled = False
                    elif 'do' in item:
                        enabled = True
            except ValueError:
                # print("couldn't work on", item)
                if "don't" in item:
                    enabled = False
                elif 'do' in item:
                    enabled = True
        except IndexError:
            # print("couldn't work on", item)
            if "don't" in item:
                enabled = False
            elif 'do' in item:
                enabled = True

print(total_sum)
print(counter)

# print(mults)