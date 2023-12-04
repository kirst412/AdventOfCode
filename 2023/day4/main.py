
with open('input.txt') as fp:
    data = fp.read().split('\n')

print(data)

indeces = []
number_indeces = []

for i, row in enumerate(data):
    # get indeces of symbols
    num_ind = []
    for j, item in enumerate(row):
        if item != '.' and not item.isdigit():
            indeces.append((i, j))
        if item.isdigit():
            num_ind.append(j)
    number_indeces.append(num_ind)

good_indeces = []

for i, row in enumerate(number_indeces):
    good_numbers = []
    for j, idx in enumerate(row):
        if i == 0:
            # check below only
            if idx == 0 or idx == len(data[i]) - 1:
            # starting or ending idx of a row, check below only at idx
                if data[i+1][idx] != '.' and not data[i+1][idx].isdigit():
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)
            else:
                # check below only, all around digit
                if (data[i+1][idx] != '.' and not data[i+1][idx].isdigit()) or (data[i+1][idx-1] != '.' and not data[i+1][idx-1].isdigit()) or (data[i+1][idx+1] != '.' and not data[i+1][idx+1].isdigit()):
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)
        elif i == len(data) - 1:
            # check above only
            if idx == 0 or idx == len(data[i]) - 1:
            # starting or ending idx of a row, check above only at idx
                if data[i-1][idx] != '.' and not data[i-1][idx].isdigit():
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)
            else:
                # check above only, all around digit
                if (data[i-1][idx] != '.' and not data[i-1][idx].isdigit()) or (data[i-1][idx-1] != '.' and not data[i-1][idx-1].isdigit()) or (data[i-1][idx+1] != '.' and not data[i-1][idx+1].isdigit()):
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)
        else:
            # check above and below, left and right
            if idx == 0 or idx == len(data[i]) - 1:
            # starting or ending idx of a row, check above and below only at idx
                if (data[i-1][idx] != '.' and not data[i-1][idx].isdigit()) or (data[i+1][idx] != '.' and not data[i+1][idx].isdigit()):
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)
            else:
                # check above and below, left and right
                if (data[i-1][idx] != '.' and not data[i-1][idx].isdigit()) or (data[i-1][idx-1] != '.' and not data[i-1][idx-1].isdigit()) or (data[i-1][idx+1] != '.' and not data[i-1][idx+1].isdigit()) or (data[i+1][idx] != '.' and not data[i+1][idx].isdigit()) or (data[i+1][idx-1] != '.' and not data[i+1][idx-1].isdigit()) or (data[i+1][idx+1] != '.' and not data[i+1][idx+1].isdigit()) or (data[i][idx-1] != '.' and not data[i][idx-1].isdigit()) or (data[i][idx+1] != '.' and not data[i][idx+1].isdigit()):
                    good_numbers.append(True)
                else:
                    good_numbers.append(False)

    good_indeces.append(good_numbers)

all = []

sm = 0
# Now group the number indeces.  If there is no trues in each group, add that number to the sum
for i, row in enumerate(number_indeces):
    number_digits = [] # reset this after every summation or skip
    truth = []
    # get all digits of this number
    for j, idx in enumerate(row):
        if j == 0 and row[j+1] - row[j] > 1:  # start of a digit
            if any(truth):
                sm += int(''.join(number_digits))
                all.append(int(''.join(number_digits)))
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
            else:
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
        elif j == 0:  # start of a digit
            number_digits.append(data[i][idx])
            truth.append(good_indeces[i][j])
        elif j == len(row) - 1 and row[j] - row[j-1] > 1:
            if any(truth):
                sm += int(''.join(number_digits))
                all.append(int(''.join(number_digits)))
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
            number_digits = [data[i][idx]]
            truth = [good_indeces[i][j]]
            if any(truth):
                sm += int(''.join(number_digits))
                all.append(int(''.join(number_digits)))
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
            else:
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
        elif row[j] - row[j-1] > 1:
            # new digit, do the calculation on the past digit, reset and add
            if any(truth):
                sm += int(''.join(number_digits))
                all.append(int(''.join(number_digits)))
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
            else:
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
        elif j == len(row) - 1:
            number_digits.append(data[i][idx])
            truth.append(good_indeces[i][j])
            if any(truth):
                sm += int(''.join(number_digits))
                all.append(int(''.join(number_digits)))
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
            else:
                number_digits = [data[i][idx]]
                truth = [good_indeces[i][j]]
        else:
            number_digits.append(data[i][idx])
            truth.append(good_indeces[i][j])

print(sm)



import math as m, re

board = list(open('input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

end = []
for p in chars.values():
    end.extend(p)

print(sorted(end))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))


