with open('day6_in.txt') as fp:
    lst = fp.read().split('\n')

#print(lst)
for i,row in enumerate(lst):
	lst[i] = list(row)

visited_indices = []

def get_guard_position(map_list):
	i = None
	j = None
	direction = None
	for row_index,row in enumerate(map_list):
		for column_index,column in enumerate(row):
			if column == '<' or column == '>' or column == '^' or column == 'v':
				i =  row_index
				j = column_index
				if column == '<':
					direction = 'left'
				elif column == 'v':
					direction = 'down'
				elif column == '>':
					direction = 'right'
				else:
					direction = 'up'
	return i, j, direction
	
# get starting index and direction
curr_i, curr_j, curr_direction = get_guard_position(lst)

def move_guard(current_i, current_j, current_direction, map_list,constant_ex_positions):
	if current_direction == 'left':
		if current_j == 0:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i][current_j-1] == '#':
			map_list[current_i][current_j] = '^'
		elif map_list[current_i][current_j-1] == 'X':
			constant_ex_positions.append((current_i,current_j-1]))
			map_list[current_i][current_j-1] = '<'
			map_list[current_i][current_j] = 'X'
		else:
			map_list[current_i][current_j-1] = '<'
			map_list[current_i][current_j] = 'X'
	elif current_direction == 'up':
		if current_i == 0:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i - 1][current_j] == '#':
			map_list[current_i][current_j] = '>'
		else:
			map_list[current_i-1][current_j] = '^'
			map_list[current_i][current_j] = 'X'
	elif current_direction == 'right':
		if current_j == len(map_list[current_i]) - 1:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i][current_j+1] == '#':
			map_list[current_i][current_j] = 'v'
		else:
			map_list[current_i][current_j+1] = '>'
			map_list[current_i][current_j] = 'X'
	else:
		if current_i == len(map_list) - 1:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i +1][current_j] == '#':
			map_list[current_i][current_j] = '<'
		else:
			map_list[current_i+1][current_j] = 'v'
			map_list[current_i][current_j] = 'X'
	return map_list
	
error_free = True

while error_free:
	lst = move_guard(curr_i,curr_j,curr_direction,lst)
	curr_i,curr_j,curr_direction = get_guard_position(lst)
	if curr_i is None or curr_j is None:
		error_free = False
	
print(lst)
counter  = 0
for row in lst:
	for column in row:
		if column == 'X':
			counter += 1
			
print(counter)

constant_exes = 0

temp_lst = lst.copy()

obstacle_i = 0
obstacle_j = 0
final_obstacle_list = []
for obstacle_i in range(len(lst)-1):
	for obstacle_j in range(len(lst[i]-1)):
		constant_ex_positions = []
		# change obstacle position
		temp_lst[obstacle_i][obstacle_j] = '#'
		error_free = True
		ex_loop = False
			