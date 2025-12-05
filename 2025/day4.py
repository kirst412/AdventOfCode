with open('day4_in.txt') as fp:
    lst = fp.read().split('\n')

print(lst)
# list of strings, each string is a row
roll_char = '@'

# for each check function, return true if there is another roll in the space
def check_up(row_idx, col_idx, grid):
    if row_idx == 0:
        return False
    elif grid[row_idx-1][col_idx] == roll_char:
        return True
    else:
        return False

def check_down(row_idx, col_idx, grid):
    if row_idx == len(grid)-1:
        return False
    elif grid[row_idx+1][col_idx] == roll_char:
        return True
    else:
        return False

def check_left(row_idx, col_idx, grid):
    if col_idx == 0:
        return False
    elif grid[row_idx][col_idx-1] == roll_char:
        return True
    else:
        return False

def check_right(row_idx, col_idx, grid):
    if col_idx == len(grid[row_idx])-1:
        return False
    elif grid[row_idx][col_idx+1] == roll_char:
        return True
    else:
        return False

def check_up_right(row_idx, col_idx, grid):
    if row_idx == 0 or col_idx == len(grid[row_idx])-1:
        return False
    elif grid[row_idx-1][col_idx+1] == roll_char:
        return True
    else:
        return False

def check_down_left(row_idx, col_idx, grid):
    if row_idx == len(grid)-1 or col_idx == 0:
        return False
    elif grid[row_idx+1][col_idx-1] == roll_char:
        return True
    else:
        return False

def check_down_right(row_idx, col_idx, grid):
    if row_idx == len(grid)-1 or col_idx == len(grid[row_idx])-1:
        return False
    elif grid[row_idx+1][col_idx+1] == roll_char:
        return True
    else:
        return False

def check_up_left(row_idx, col_idx, grid):
    if row_idx == 0 or col_idx == 0:
        return False
    elif grid[row_idx-1][col_idx-1] == roll_char:
        return True
    else:
        return False

total = 0

for i,row in enumerate(lst):
    for j,col in enumerate(row):
        around = 0
        if check_up(i, j, lst): around += 1
        if check_down(i, j, lst): around += 1
        if check_left(i, j, lst): around += 1
        if check_right(i, j, lst): around += 1
        if check_up_right(i, j, lst): around += 1
        if check_down_left(i, j, lst): around += 1
        if check_down_right(i, j, lst): around += 1
        if check_up_left(i, j, lst): around += 1
        if around < 4 and col == roll_char:
            total += 1

# part 1
print(total)

new_grid = lst.copy()
full_total = 0
new_total = 1

while new_total > 0:
    new_total = 0
    rolls_to_remove = []
    for i,row in enumerate(new_grid):
        for j,col in enumerate(row):
            around = 0
            if check_up(i, j, new_grid): around += 1
            if check_down(i, j, new_grid): around += 1
            if check_left(i, j, new_grid): around += 1
            if check_right(i, j, new_grid): around += 1
            if check_up_right(i, j, new_grid): around += 1
            if check_down_left(i, j, new_grid): around += 1
            if check_down_right(i, j, new_grid): around += 1
            if check_up_left(i, j, new_grid): around += 1
            if around < 4 and col == roll_char:
                new_total += 1
                rolls_to_remove.append((i,j))

    for roll in rolls_to_remove:
        row = list(new_grid[roll[0]])
        row[roll[1]] = 'x'
        new_grid[roll[0]] = ''.join(row)
    print(new_grid)
    full_total += new_total

print(full_total)


