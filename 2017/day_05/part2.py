inst = []

with open('part1.input') as f:
	for line in f:
		inst += [int(line)]

step = 0
i = 0
try:
	while True:
		#print("Before i:{0}; inst[i]:{1}; step:{2}; inst:{3}".format(i,inst[i], step, inst))
		next = inst[i]
		if inst[i] >= 3:
			inst[i] -= 1
		else:
			inst[i] += 1
		i += next
		step +=1
		#print("After  i:{0}; inst[i]:{1}; step:{2}; inst:{3}".format(i,inst[i], step, inst))

except LookupError:
	print("Steps = {0}".format(step))
