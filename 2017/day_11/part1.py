class Axial:
	def __init__(self, col, row):
		self.q = col
		self.r = row

	def __add__(self, other):
		col = self.q + other.q
		row = self.r + other.r
		return Axial(col, row)

	def __radd__(self, other):
		returnself.__add__(other)

	def __str__(self):
		return'({}, {})'.format(self.q, self.r)

def move(coordinate, direction, distance=1):
	if direction == 'n':
		t = Axial(0,-1*distance)
	elif direction == 'ne':
		t = Axial(distance,-1*distance)
	elif direction == 'se':
		t = Axial(distance,0)
	elif direction == 's':
		t = Axial(0,distance)
	elif direction == 'sw':
		t = Axial(-1*distance,distance)
	elif direction == 'nw':
		t = Axial(-1*distance,0)
	else:
		raise Exception

	return coordinate + t

def distance(a, b):
	return (abs(a.q - b.q) + abs(a.q + a.r - b.q - b.r) + abs(a.r - b.r)) / 2

def walk(path, start=Axial(0,0)):
	pos = start

	for step in path:
		pos = move(pos, step, 1)
		
	return pos

def test(string, valid):
	start = Axial(0,0)
	print('Path: {}'.format(string))
	end = walk(string.split(','), start)
	print('End: {}'.format(end))
	dist = distance(start, end)
	print('Distance: {}'.format(dist))
	if dist == valid:
		print('Pass')
	else:
		print('Fail, expected {}'.format(valid))
	print

'''
test('ne,ne,ne', 3)
test('ne,ne,sw,sw', 0)
test('ne,ne,s,s', 2)
test('se,sw,se,sw,sw', 3)
'''

with open('part1.input') as f:
	for line in f:
		print('Distance: {}'.format(distance(Axial(0,0), walk(line[:-1].split(',')))))
