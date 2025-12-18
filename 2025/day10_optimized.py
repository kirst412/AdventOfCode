import collections
import itertools

def clean_machine(machine):
    partial = machine.split('[')[1]
    return partial.split(']')[0]

def init_machine(button_list):
    # Initializes a new list of '.' with the correct length
    return ['.' for _ in range(len(clean_machine(button_list)))]

def clean_button_group(button_group):
    partial = button_group.split('(')[1]
    no_parens = partial.split(')')[0]
    no_comma = no_parens.split(',')
    ints = [int(val) for val in no_comma]
    return tuple(ints)

def press_button_group(button_group, machine_tuple):
    # Operate on a tuple for hashability needed in the 'visited' set
    machine_list = list(machine_tuple)
    for button in button_group:
        if machine_list[button] == '.':
            machine_list[button] = '#'
        else:
            machine_list[button] = '.'
    return tuple(machine_list) # Return as a tuple

# --- Main Logic for Processing Data ---

total_presses = 0

with open('data/day10_in.txt') as fp:
    lst = fp.read().split('\n')

for i, row in enumerate(lst):
    # Skip empty lines if any
    if not row:
        continue
        
    split_row = row.split(' ')
    machine_str = split_row[0]
    machine_final_state_list = list(clean_machine(machine_str))
    machine_final_state = tuple(machine_final_state_list) # Use tuple for hashability

    # Initialize the starting state as a tuple
    machine_init_list = init_machine(machine_str)
    machine_init = tuple(machine_init_list)

    buttons = split_row[1:-1]
    cleaned_buttons = [clean_button_group(group) for group in buttons]
    # Keep only unique button groups if they perform identical actions
    unique_buttons = list(set(cleaned_buttons))

    # --- Use Breadth-First Search (BFS) to find the shortest path ---
    
    # Queue stores (current_machine_state, steps_taken)
    queue = collections.deque([(machine_init, 0)])
    # Set to keep track of visited states to avoid cycles and redundant work
    # Must store states as immutable tuples
    visited = {machine_init}
    
    min_presses_found = False

    while queue:
        current_state, steps = queue.popleft()

        if current_state == machine_final_state:
            min_presses = steps
            min_presses_found = True
            break
        
        # Optimization: Don't explore paths longer than the current best known (though BFS naturally handles this)
        # and limit exploration depth if needed (e.g., if the problem implies a small max number of presses)

        for button_group in unique_buttons:
            next_state = press_button_group(button_group, current_state)
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    
    if min_presses_found:
        total_presses += min_presses
        # print(f"Row {i}: Min presses = {min_presses}")
    else:
        # print(f"Row {i}: No solution found")
        pass # Handle cases where a solution might not exist

print(f"Total presses across all rows: {total_presses}")
