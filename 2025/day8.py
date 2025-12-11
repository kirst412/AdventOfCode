import math

with open('data/day8_in.txt') as fp:
    lst = fp.read().split('\n')

min_num_circuits = 6006  # at least greater than 6004

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


def connect_circuits(lst, min_num_circuits):
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
	last_pair = None
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
		counter += 1
		last_pair = min_idx
		min_val = None
		min_idx = None
		# I need to check if the new pair is already connected through an existing circuit.  if so, reduce counter
		new_circuits = combine_circuits(all_pairs)
		if prev_circuits != new_circuits:
			prev_circuits = new_circuits
		lengths = sorted([len(circuit) for circuit in new_circuits], reverse=True)
		if counter == min_num_circuits and lengths[0] != len(lst):
			print(min_num_circuits)
			min_num_circuits += 1
	
	print(new_circuits)
	lengths = sorted([len(circuit) for circuit in new_circuits], reverse=True)
	print('length of circuit = {}'.format(lengths))
	print('lengths needs to match length of input list which is {}.'.format(len(lst)))
	print('min_num_circuits ran was {}. '.format(min_num_circuits))
	return lengths, last_pair, lookup

#mult = 1
#for i in range(3):
	#mult = mult * lengths[i]
	
#print(mult)

lengths, last_pair, lookup = connect_circuits(lst, min_num_circuits)

while lengths[0] != len(lst):
	min_num_circuits += 1
	lengths, last_pair, lookup = connect_circuits(lst, min_num_circuits)

# for part 2, I just need to retain the last 2 circuits that were connected
# using last pair, look up what the z value of the pair is
print('min_num_circuits: {}'.format(min_num_circuits))
print('last pair to be added is {}.'.format(last_pair))
pair1 = last_pair[0]
pair2 = last_pair[1]
print('coordinates are {} and {}, x mult is {}'.format(lookup[pair1],lookup[pair2],lookup[pair1][0] * lookup[pair2][0]))

# okay instead of manually checking the min number of connections, let's set up a loop

