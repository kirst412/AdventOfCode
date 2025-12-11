import itertools

with open('data/day10_test.txt') as fp:
    lst = fp.read().split('\n')

def clean_machine(machine):
	partial = machine.split('[')[1]
	return partial.split(']')[0]
	
# write a function to initialize each machine
def init_machine(button_list):
	only_buttons = clean_machine(button_list)
	length = len(only_buttons)
	return ['.' for i in range(length)]

def clean_button_group(button_group):
	partial = button_group.split('(')[1]
	no_parens = partial.split(')')[0]
	no_comma = no_parens.split(',')
	ints = [int(val) for val in no_comma]
	return tuple(ints)

def press_button_group(button_group,machine):
	for button in button_group:
		if machine[button] == '.':
			machine[button] = '#'
		else:
			machine[button] = '.'
	return machine
	
max_button_groups = 5
	
for i,row in enumerate(lst):
	machine = row.split(' ')[0]
	machine_final_state = list(clean_machine(machine))
	machine_init = init_machine(machine)
	split_row = row.split(' ')
	buttons = split_row[1:-1]
	cleaned_buttons = [clean_button_group(group) for group in buttons]
	# buttons is a list of strings where the string is a tuple
	# I think I need to get all the unique combinations of button presses
	# then loop through those until machine_init = machine_final_state
	button_combos = list(itertools.combinations(cleaned_buttons, max_button_groups))
	print(cleaned_buttons)
	print(button_combos)
	# loop through each combination and keep track of how many presses it took to get final machine_final_state
	
	