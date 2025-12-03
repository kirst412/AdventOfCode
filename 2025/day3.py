
with open('day3_in.txt') as fp:
    lst = fp.read().split('\n')

def find_max_w_index(list_of_nums):
    max_val = max(list_of_nums)
    max_indices = [index for index, value in enumerate(list_of_nums) if value == max_val]
    return max_val, max_indices

# find the max 2 numbers in each bank
total = 0

for bank in lst:
    max_val, max_indices = find_max_w_index(bank)
    # if max_indices is more than 1, sum the max value times 11
    if len(max_indices) > 1:
        total += int(max_val) * 11
    # since there is only one instance of the max value, see if it's not the last item in the list
    elif max_indices[0] != (len(bank) - 1):
        # slice the list, get max again of items after max value index
        later_bank = bank[max_indices[0] + 1:]
        next_max, next_indices = find_max_w_index(later_bank)
        total += int(max_val) * 10 + int(next_max)
    else:
        # this means the max value is the last item in the list, we need to get the next largest one as the tens digit then
        early_bank = bank[0:max_indices[0]]
        early_max, early_indices = find_max_w_index(early_bank)
        total += int(early_max) * 10 + int(max_val)

print(total)
