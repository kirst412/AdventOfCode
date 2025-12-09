import math

with open('data/day8_in.txt') as fp:
    lst = fp.read().split('\n')

min_num_circuits = 10

def eucdist(x1, x2, y1, y2, z1, z2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
	
def combine_circuits(list_of_pairs):
	# given a list of pairs, return a list of combined circuits
	combined_pairs = []
	for pair in list_of_pairs:
		if len(combined_pairs) == 0:
			combined_pairs.append([pair[0],pair[1]])
		else:
			added = False
			added_idx = None
			equal = False
			dupe = False
			for i,circuit in enumerate(combined_pairs):
				if pair[0] in circuit and pair[1] in circuit:
					equal = True
				# need to add handling if they are in 2 different circuits
				elif pair[0] in circuit and not equal:
					if added:
						# combine the 2 lists of the other idx
						new_circuit = list(set(combined_pairs[added_idx]+circuit))
						combined_pairs[added_idx] = new_circuit
						combined_pairs[i] = new_circuit
						dupe = True
					else:
						combined_pairs[i].append(pair[1])
						added = True
						added_idx = i
				elif pair[1] in circuit and not equal:
					if added:
						new_circuit = list(set(combined_pairs[added_idx]+circuit))
						print('new_circuit', new_circuit)
						combined_pairs[added_idx] = new_circuit
						combined_pairs[i] = new_circuit
						dupe = True
					else:
						combined_pairs[i].append(pair[0])
						added = True
						added_idx = i
			if not added and not equal:
				combined_pairs.append([pair[0],pair[1]])
		
			# remove added_idx if not none
			if dupe:
				del combined_pairs[added_idx]
			
	return combined_pairs

# could make a matrix of len(lst) x len(lst) to keep track of distances
# 1. lookup dictionary for each xyz pair
# 2. array with all distances

lookup = {}
for i, coord in enumerate(lst):
	x, y, z = coord.split(',')
	lookup[i] = (int(x), int(y), int(z))

rows = len(lst)
cols = len(lst)
distances = [[0 for _ in range(cols)] for _ in range(rows)]

for i, row in enumerate(lst):
	for j, col in enumerate(lst):
		distances[i][j] = eucdist(lookup[i][0],lookup[j][0],lookup[i][1],lookup[j][1],lookup[i][2],lookup[j][2])
		
# find smallest non-zero distance
counter = 0
min_vals = []
min_val = None
min_idx = None
mult = 1
all_vals = []
all_pairs = []
prev_circuits = []
while counter < min_num_circuits:
	for i,row in enumerate(distances):
		for j,val in enumerate(row):
			if min_val == None:
				if val != 0:
					min_val = val
					min_idx = (i,j)
			elif val < min_val and (val != 0) and (val not in all_vals) and ((i,j) not in all_pairs or (j,i) not in all_pairs):
				min_val = val
				min_idx = (i,j)
	min_vals.append({'pair': min_idx,'val':min_val})
	all_vals = [dictin['val'] for dictin in min_vals]
	all_pairs = [(dictin['pair'][0],dictin['pair'][1])for dictin in min_vals]
	# check if the new pair min_idx is already covered in an existing circuit
	print(min_idx)
	counter += 1
	min_val = None
	min_idx = None
	# I need to check if the new pair is already connected through an existing circuit.  if so, reduce counter
	new_circuits = combine_circuits(all_pairs)
	if prev_circuits != new_circuits:
		prev_circuits = new_circuits

	print(new_circuits)
	
lengths = sorted([len(circuit) for circuit in new_circuits], reverse=True)
print(lengths)

mult = 1
for i in range(3):
	mult = mult * lengths[i]
	
print(mult)

