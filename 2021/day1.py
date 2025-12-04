# import data
import pandas as pd

with open('day1_in.txt') as fp:
    lst = fp.read().split('\n')


# part 1
# print(lst)

counter = 0
prev = 0

for item in lst:
    if int(item) > prev:
        counter += 1
    prev = int(item)

print(counter-1)

# part 2
# 3 scan rolling window
df = pd.DataFrame(lst)
df['window'] = df.rolling(window=3).sum()

temp = df['window'].dropna().copy()
print(temp)
counter = 0
prev = 0
for item in temp:
    if int(item) > prev:
        counter += 1
    prev = int(item)
print(counter-1)
