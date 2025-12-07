with open('data/day7_in.txt') as fp:
    lst = fp.read().split('\n')

for i,row in enumerate(lst):
	lst[i] = list(row)

splits = 0
i = 0
pipes = []
	
while i < len(lst):
	row = lst[i]
	for j,item in enumerate(row):
		if i == 0:
			if item == 'S':
				lst[i+1][j] = '|'
		else:
			if item == '^' and lst[i-1][j] == '|':
				splits += 1
				lst[i+1][j-1] = '|'
				lst[i+1][j+1] = '|'
			elif lst[i-1][j] == '|':
				lst[i][j] = '|'
				lst[i+1][j] = '|'
	i += 2

for i,row in enumerate(lst):
	lst[i] = ''.join(row)
	print(lst[i])
	
print(splits)
