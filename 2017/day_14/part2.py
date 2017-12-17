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

	def count_regions(self):
		count = 0
		
		for py in range(128):
			for px in range(128):
				if self.rows[py][px] == 1:
					count += 1
					queue = [(px,py)]
					while queue:
						x,y = queue.pop()
						self.rows[y][x] = 0
						if x < 127 and self.rows[y][x+1] == 1:
							if (x+1,y) not in queue:
								queue.append((x+1,y))
						if x > 0 and self.rows[y][x-1] == 1:
							if (x-1,y) not in queue:
								queue.append((x-1,y))
						if y < 127 and self.rows[y+1][x] == 1:
							if (x,y+1) not in queue:
								queue.append((x,y+1))
						if y > 0 and self.rows[y-1][x] == 1:
							if (x,y-1) not in queue:
								queue.append((x,y-1))
					
		return count

			
	def __str__(self):
		s=''

		for row in self.rows:
			for x in range(128):
				if row[x] == 1:
					s += '#'
				if row[x] > 1:
					s += '*'
				else:
					s += '.'
				s += ' '
			s = s[:-1] + '\n'

		return s[:-1]
		
disk = Disk('vbqugkhl')
print('Number of regions: {}'.format(disk.count_regions()))
#print(disk)
