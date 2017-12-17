from knot import KnotHash

class Disk:
	def __init__(self, input):
		self.rows = []
		self.used = 0

		for i in range(128):
			knot = KnotHash()
			knot.update('{}-{}'.format(str(input),i))
			r = map(int,'{:0128b}'.format(int(knot.digest(), 16)))
			self.rows += [r]
			self.used += sum(r)

	def __str__(self):
		s=''

		for row in self.rows:
			for x in range(128):
				if row[x] == 1:
					s += '#'
				else:
					s += '.'
				s += ' '
			s = s[:-1] + '\n'

		return s[:-1]
		
disk = Disk('vbqugkhl')
print('Number of used squares: {}'.format(disk.used))
