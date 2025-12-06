with open('data/day6_in.txt') as fp:
    lst = fp.read().split('\n')
    
print(lst)

# I want to loop through and separate out each of the problems
probs = {}

for nums in lst:
	split_nums = nums.split(' ')
	split_nums = [s for s in split_nums if s.strip('')]
	for i,num in enumerate(split_nums):
		if num != '':
			if i not in probs.keys():
				probs[i] = [num]
			else:
				probs[i].append(num)
			
print(probs)
total = 0
for key,value in probs.items():
	# value is the list of items in the math problem
	if value[-1] == '+':
		total += sum([int(item) for item in value[:-1]])
	else:
		mult = 1
		for item in value[:-1]:
			mult *= int(item)
		total += mult
		
print(total)
	
