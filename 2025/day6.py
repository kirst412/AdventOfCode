with open('data/day6_in.txt') as fp:
    lst = fp.read().split('\n')
    
print(lst)

# I want to loop through and separate out each of the problems
probs = {}

for nums in lst:
	split_nums = nums.split(' ')
	#split_nums = [s for s in split_nums if s.strip('')]
	#split_nums = nums
	print(split_nums)
	print(nums[::-1])
	nums = nums[::-1]
	# I need to reverse the string of characters
	for i,num in enumerate(nums):
		if i not in probs.keys():
			probs[i] = [num]
		else:
			probs[i].append(num)
			
print(probs)
total = 0
prob_total = []
for key,value in probs.items():
	# value is a list of digits.  if the last item in the list is an operator, 
	# complete the calc and add to total
	num = ''.join(value[:-1])
	print(num)
	try:
		prob_total.append(int(num))
	except ValueError:
		print('empty string, moving onto next problem, prob_total {} should be empty'.format(prob_total))
	if value[-1] == '+':
		total += sum(prob_total)
		prob_total = []
	elif value[-1] == '*':
		mult = 1
		for val in prob_total:
			mult *= val
		total += mult
		prob_total = []
		
print(total)
	
