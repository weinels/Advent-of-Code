from collections import deque

with open('part2.input') as f:
	array = []
	first = None
	for line in f:
		for c in line:
			if c != '\n':
				if first is None:
					first = int(c)
				array += [int(c)]

sum = 0
size = len(array)
offset = (size+1)/2

for i in range(size):
	next = (i + offset) % size
	if array[i] == array[next]:
		sum += array[i]
				
print("Sum is {0}".format(sum))
