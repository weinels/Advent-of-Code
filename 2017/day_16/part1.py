
dancers = [chr(x) for x in range(97,97+16)]


with open('part1.input') as f:
	for line in f:
		for move in line[:-1].split(','):
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

s = ''
for p in dancers:
	s += str(p)

print("The dancer order is: {}".format(s))
