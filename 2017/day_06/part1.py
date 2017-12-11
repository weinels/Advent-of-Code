banks = []
history = []
count = 0

with open('part1.input') as f:
	for line in f:
		banks += [int(x) for x in line[:-1].split("\t")]
		
while True:
	count += 1
	blocks = max(banks)
	p = banks.index(blocks)
	banks[p] = 0
	
	for i in range(1,blocks+1):
		banks[(p+i)%len(banks)] += 1

	if banks in history:
		break
	else:
		history += [list(banks)]

print("Redistibution cycles: {0}".format(count))
