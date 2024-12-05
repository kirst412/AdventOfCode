with open('day4_in.txt') as fp:
    lst = fp.read().split('\n')

print(lst)

xmas_total = 0
xmas_string = ['X','M','A','S']
string_index = 0

for i,row in enumerate(lst):
    for j,value in enumerate(row):
        if value == 'X':
            if j <= len(row) - 4:
                # check horizontal first
                if row[j+1] == 'M':
                    if row[j+2] == 'A':
                        if row[j+3] == 'S':
                            xmas_total += 1
                if i <= len(lst) - 4:
                    # check diag down right
                    if lst[i+1][j+1] == 'M':
                        if lst[i+2][j+2] == 'A':
                            if lst[i+3][j+3] == 'S':
                                xmas_total += 1
                if i >= 3:
                    # check diag up right
                    if lst[i-1][j+1] == 'M':
                        if lst[i-2][j+2] == 'A':
                            if lst[i-3][j+3] == 'S':
                                xmas_total += 1
            if j >= 3:
                # check horizontal backwards
                if row[j-1] == 'M':
                    if row[j-2] == 'A':
                        if row[j-3] == 'S':
                            xmas_total += 1
                if i <= len(lst) - 4:
                    # check diag down left
                    if lst[i+1][j-1] == 'M':
                        if lst[i+2][j-2] == 'A':
                            if lst[i+3][j-3] == 'S':
                                xmas_total += 1
                if i >= 3:
                    # check diag up left
                    if lst[i-1][j-1] == 'M':
                        if lst[i-2][j-2] == 'A':
                            if lst[i-3][j-3] == 'S':
                                xmas_total += 1
            if i >= 3:
                # check up
                if lst[i-1][j] == 'M':
                    if lst[i-2][j] == 'A':
                        if lst[i-3][j] == 'S':
                            xmas_total += 1
            if i <= len(lst) - 4:
                # check down
                if lst[i+1][j] == 'M':
                    if lst[i+2][j] == 'A':
                        if lst[i+3][j] == 'S':
                            xmas_total += 1

print(xmas_total)

partb_total = 0

## Part B
for i,row in enumerate(lst):
    for j,value in enumerate(row):
        if value == 'A':
            true_up_left = False
            true_up_right = False
            true_down_left = False
            true_down_right = False
            if j >= 1 and i >= 1 and i <= len(lst) - 2 and j <= len(lst) - 2:
                if lst[i-1][j-1] == 'M':
                    if lst[i+1][j+1] == 'S':
                        true_up_left = True
                if lst[i-1][j+1] == 'M':
                    if lst[i+1][j-1] == 'S':
                        true_up_right = True
                if lst[i+1][j-1] == 'M':
                    if lst[i-1][j+1] == 'S':
                        true_down_left = True
                if lst[i+1][j+1] == 'M':
                    if lst[i-1][j-1] == 'S':
                        true_down_right = True
            if (true_up_left and (true_up_right or true_down_left)) or (true_up_right and (true_up_left or true_down_right)) or (true_down_right and (true_up_right or true_down_left)) or (true_down_left and (true_up_left or true_down_right)):
                partb_total += 1

print(partb_total)

                    