with open('day1_in.txt') as fp:
    lst = fp.read().split('\n')

lsta = []
lstb = []
for pair in lst:
    lsta.append(int(pair.split(' ')[0]))
    lstb.append(int(pair.split(' ')[3]))

print(len(lsta) == len(lstb))

lsta_copy = lsta.copy()
lstb_copy = lstb.copy()
pairings = []

def find_min(lst):
    return min(lst), min(range(len(lst)), key=lst.__getitem__)

sum_dist = 0

while len(lsta) != 0:
    min_a, index_a = find_min(lsta)
    min_b, index_b = find_min(lstb)
    sum_dist += abs(min_a - min_b)
    lsta.pop(index_a)
    lstb.pop(index_b)

print("Part A answer: ",sum_dist)

## part b
similarity_score = 0
for item in lsta_copy:
    # check the number of times that item appears in lstb
    similarity_score += item * len([i for i, x in enumerate(lstb_copy) if x == item])

print("Part B answer: ", similarity_score)