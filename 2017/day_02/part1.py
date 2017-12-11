def input(file):
	with open(file) as f:
		for line in f:
			yield [int(x) for x in line[:-1].split('\t')]
					
checksum = 0

for l in input('part1.input'):
	checksum += int(max(l)) - int(min(l))
	print("{0} = {1}".format(l,int(max(l)) - int(min(l))))

print("Checksum is {0}".format(checksum))
