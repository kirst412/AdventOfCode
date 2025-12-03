
with open('day3_in.txt') as fp:
    lst = fp.read().split('\n')

# with open('day3_test.txt') as fp:
#     lst = fp.read().split('\n')

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

# part 2, it can now be 12 digits, what the heck
total = 0

for bank in lst:
    # okay knowing that we need 12 digits, make the starting string the last 12 digits.  one at a time move the starting digit to the earliest max.
    bank_num = list(bank[-12:len(bank) + 1])
    remaining_bank = list(bank[0:len(bank) - 12])
    print(bank_num)
    print(remaining_bank)
    for i,item in enumerate(bank_num):
        print(i)
        print(remaining_bank)
        if len(remaining_bank) > 0:
            max_val, max_indices = find_max_w_index(remaining_bank)
            print(max_val, max_indices[0])
            if int(max_val) >= int(bank_num[i]):
                remaining_bank.append(bank_num[i])
                bank_num[i] = int(max_val)
                remaining_bank = remaining_bank[max_indices[0] + 1:]
                print(bank_num)
                print(remaining_bank)
            else:
                remaining_bank = []
        else:
            bank_num[i] = int(bank_num[i])

    total += int(''.join(map(str, bank_num)))
    print(bank)
    print(total)

print(total)

def maxj(s,k):
    r=''
    for skip in range(k-1,-1,-1):
        j = s.index(max(s[:len(s)-skip]))
        r,s= r + s[j],s[j+1:]
    return int(r)

# total = 0
# for s in lst:
#     print(s)
#     total += maxj(s,12)
#     print(total)
#
# print(sum(maxj(s,12) for s in lst))


