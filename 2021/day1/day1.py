# import data
with open('input.txt') as fp:
    lst = fp.read().split('\n')

print(lst)

counter = []

for i,item in enumerate(lst):
    if i != 0 and item != '':
        # print('item',item)
        # print('prev',lst[i-1])
        if item > lst[i-1]:
            counter.append('inc')
            # print('inc')
        else:
            counter.append('dec')

print(len(lst))
print(len([i for i in counter if i == 'inc']))

