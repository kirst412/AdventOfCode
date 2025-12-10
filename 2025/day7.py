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

for i,row in enumerate(lst):
	lst[i] = list(row)

counter = 0
# now loop through splits
for i,row in enumerate(lst):
	for j,val in enumerate(row):
		if val == '^' and lst[i-1][j] == '|':
			lst[i+1][j-1] = 1
			lst[i+1][j+1] = 1
		elif val == '^' and lst[i-1][j] != '.':
			# check if something else is already in lst[i+1][j-1]
			if lst[i+1][j-1] != '|':
				# add 1 to the number there
				lst[i+1][j-1] += lst[i-1][j]
			else:
				lst[i+1][j-1] = lst[i-1][j]
			lst[i+1][j+1] = lst[i-1][j]
		elif val == '|' and lst[i-1][j] != 'S':
			lst[i][j] = lst[i-1][j]
			# it's a number, add it
		if lst[i-1][j-1] != '.' and val == '^':
			if lst[i-1][j-2] == '.' or (lst[i-1][j-2] != '.' and lst[i][j-2] != '^'):
				if lst[i-1][j] == '.':
					lst[i+1][j-1] = lst[i][j-1]
				else:
					lst[i+1][j-1] += lst[i-1][j-1]
		if val == '^' and lst[i-1][j+1] != '.' and lst[i-1][j] != '.':
			if lst[i+1][j+1] == '|':
				lst[i+1][j+1] = lst[i-1][j+1]
			lst[i+1][j+1] += lst[i-1][j+1]
			
total = 0
for items in lst[-1]:
	if items != '.':
		total += int(items)
		
print(total)
	
for i,row in enumerate(lst):
	for j,col in enumerate(row):
		lst[i][j] = str(col)
	lst[i] = ''.join(lst[i])