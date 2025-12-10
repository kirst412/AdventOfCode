with open('data/day9_in.txt') as fp:
    lst = fp.read().split('\n')
    
print(lst)

# get combos of all areas
combos = {}
for pair in lst:
	i,j = pair.split(',')
	i = int(i)
	j = int(j)
	for pair2 in lst:
		i2,j2 = pair2.split(',')
		i2 = int(i2)
		j2 = int(j2)
		if i!=i2 and j!=j2 and (pair2 + '-' + pair not in combos.keys()):
			# calculate area
			area = (abs(i+1-i2) * abs(j+1-j2))
			combos[pair + '-' + pair2] = area
			
print(combos)
print('largest rectangle: {}'.format(max(combos.values())))
