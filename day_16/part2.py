
dancers = [chr(x) for x in range(97,97+16)]
start = reduce(lambda x, y: x + y, dancers)

with open('part1.input') as f:
	for line in f:
		moves = line[:-1]

repeat = -1
i = 0
end = 1000000000
while i < end:
	for move in moves.split(','):
		if move[0] == 's': # spin
			length = int(move[1:])
			dancers = dancers[-length:] + dancers[:-length]
		elif move[0] == 'x': # exchange
			locs = move[1:].split('/')
			locA = int(locs[0])
			locB = int(locs[1])
			dancers[locA], dancers[locB] = dancers[locB], dancers[locA]
		elif move[0] == 'p': # partner
			locs = move[1:].split('/')
			locA = dancers.index(locs[0])
			locB = dancers.index(locs[1])
			dancers[locA], dancers[locB] = dancers[locB], dancers[locA]
		else:
			raise Exception
			
	i += 1
	
	if reduce(lambda x, y: x + y, dancers) == start:
		end = end % i
		i = 0
		
print("The dancer order is: {}".format(reduce(lambda x, y: x + y, dancers)))
