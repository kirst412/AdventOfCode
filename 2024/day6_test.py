with open('day6_in_test.txt') as fp:
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
			constant_ex_positions.append((current_i,current_j-1))
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
		elif map_list[current_i-1][current_j] == 'X':
			constant_ex_positions.append((current_i-1,current_j))
			map_list[current_i-1][current_j] = '^'
			map_list[current_i][current_j] = 'X'
		else:
			map_list[current_i-1][current_j] = '^'
			map_list[current_i][current_j] = 'X'
	elif current_direction == 'right':
		if current_j == len(map_list[current_i]) - 1:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i][current_j+1] == '#':
			map_list[current_i][current_j] = 'v'
		elif map_list[current_i][current_j+1] == 'X':
			constant_ex_positions.append((current_i,current_j+1))
			map_list[current_i][current_j+1] = '>'
			map_list[current_i][current_j] = 'X'
		else:
			map_list[current_i][current_j+1] = '>'
			map_list[current_i][current_j] = 'X'
	else:
		if current_i == len(map_list) - 1:
			error_free = False
			map_list[current_i][current_j] = 'X'
		elif map_list[current_i +1][current_j] == '#':
			map_list[current_i][current_j] = '<'
		elif map_list[current_i+1][current_j] == 'X':
			constant_ex_positions.append((current_i+1,current_j))
			map_list[current_i+1][current_j] = 'v'
			map_list[current_i][current_j] = 'X'
		else:
			map_list[current_i+1][current_j] = 'v'
			map_list[current_i][current_j] = 'X'
	return map_list, constant_ex_positions
	
#error_free = True

#while error_free:
	#lst = move_guard(curr_i,curr_j,curr_direction,lst)
#	curr_i,curr_j,curr_direction = get_guard_position(lst)
#	if curr_i is None or curr_j is None:
#		error_free = False
	
#print(lst)
#counter  = 0
#for row in lst:
#	for column in row:
#		if column == 'X':
#			counter += 1
			
#print(counter)

#constant_exes = 0

obstacle_i = 0
obstacle_j = 0
final_obstacle_list = []
for obstacle_i in range(len(lst)-1):
	for obstacle_j in range(len(lst[i])-1):
		print("position:	{},{}".format(obstacle_i,obstacle_j))
		
		with open('day6_in_test.txt') as fp:
		    temp_lst = fp.read().split('\n')
		
		#print(lst)
		for i,row in enumerate(temp_lst):
			temp_lst[i] = list(row)
		
		if temp_lst[obstacle_i][obstacle_j] in ['#','v','<','>','^']:
			continue
		constant_ex_positions = []
		# change obstacle position
		temp_lst[obstacle_i][obstacle_j] = '#'
		error_free = True
		ex_loop = False
		prev_in_constant = False
		# get starting index and direction
		print('getting initial position...')
		curr_i, curr_j, curr_direction = get_guard_position(temp_lst)
		print(curr_i,curr_j,curr_direction)
		print('starting while loop...')
		while error_free:
			temp_lst, constant_ex_positions = move_guard(curr_i,curr_j,curr_direction,temp_lst,constant_ex_positions)
			curr_i,curr_j,curr_direction = get_guard_position(temp_lst)
			if curr_i is None or curr_j is None:
				error_free = False
			# check if the current position index is in constant_ex_positions
			if (curr_i,curr_j) in constant_ex_positions:
				if not prev_in_constant:
					prev_in_constant = True
				else:
					ex_loop = True
		if ex_loop:
			final_obstacle_list.append((obstacle_i,obstacle_j))
			
print(len(final_obstacle_list))
print(final_obstacle_list)