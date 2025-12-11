with open('data/day9_test.txt') as fp:
    lst = fp.read().split('\n')
    
print(lst)

pairs = [(int(pair.split(',')[0]),int(pair.split(',')[1])) for pair in lst]
x_dims = [pair[0] for pair in pairs]
y_dims = [pair[1] for pair in pairs]
max_x_dim = max(x_dims) + 2 
max_y_dim = max(y_dims) + 2

grid = [['.' for _ in range(max_x_dim)] for _ in range(max_y_dim)]
# get combos of all areas
combos = {}
for pair in lst:
	j,i = pair.split(',')
	i = int(i)
	j = int(j)
	grid[i][j] = '#'
	for pair2 in lst:
		j2,i2 = pair2.split(',')
		i2 = int(i2)
		j2 = int(j2)
		if i!=i2 and j!=j2 and (pair2 + '-' + pair not in combos.keys()):
			# calculate area
			area = (abs(i+1-i2) * abs(j+1-j2))
			combos[pair + '-' + pair2] = area
			
print(combos)
print('largest rectangle: {}'.format(max(combos.values())))

# now I need to calculate the perimeter
# connect all x coordinates and all y coordinates maybe?
# make a grid to make it easier to interpret the solution
def print_grid(grid):
	for row in grid:
		print(''.join(row))

for i,row in enumerate(grid):
	first_j = None
	second_j = None
	for j,val in enumerate(row):
		if val == '#':
			if first_j is None:
				first_j = j
			else:
				second_j = j
		elif second_j is None and first_j is not None:
			grid[i][j] = '#'
			
print_grid(grid)

def check_for_hash_until_bottom(row_idx, col_idx, grid):
	truth_list = []
	# I am at row_idx, col_idx.  see if [row_idx] + 1[col_idx] has any more hashes
	row_idx += 1
	while row_idx < len(grid):
		if grid[row_idx][j] == '#':
			truth_list.append(True)
		else:
			truth_list.append(False)
		row_idx += 1
	return any(truth_list)

indeces_to_fill = []
first_i = None
for i, row in enumerate(grid):
	for j,val in enumerate(grid):
		rower = i
		if row[j] == '#' and check_for_hash_until_bottom(i,j,grid) and i != len(grid):
			while grid[rower+1][j] != '#':
				grid[rower+1][j] = '#'
				rower += 1
			
print_grid(grid)