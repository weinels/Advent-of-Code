def input(file):
	with open(file) as f:
		for line in f:
			yield [int(x) for x in line[:-1].split('\t')]
					
sum = 0

for l in input('part2.input'):
	# note, this list each par twice, but since we're doing integer division
	# only one pair will result in a nonzero number
	D = [(x,y) for x in l for y in l if ((x % y == 0) or (y % x == 0)) and (x <> y)]
	for num, den in D:
		#print("{0}/{1}={2}".format(num,den,num/den))
		sum += num/den
	
print("Sum is {0}".format(sum))
