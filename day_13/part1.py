class Scanner:
	def __init__(self, depth, range):
		self.depth = depth
		self.range = range 
		self.pos = 1
		self.vel = 1
		
	def move(self):
		next = self.pos + self.vel
		if next > self.range:
			self.vel = -1
		if next < 1:
			self.vel = 1
			
		self.pos += self.vel
		
class Firewall:
	def __init__(self):
		self.scanners = []
		self.packet_depth = -1
		self.severity = 0

	def add(self, d, r):
		self.scanners.append(Scanner(int(d), int(r)))

	def move_scanners(self):
		for s in self.scanners:
			s.move()

	def move_packet(self):
		self.packet_depth += 1

	def move(self):
		self.move_packet()

		scan = self.find(self.packet_depth)
		if scan is not None and scan.pos == 1:
#			print('caught {}*{}={}'.format(scan.depth, scan.range, scan.depth*scan.range))
#			print(self)
			self.severity += scan.depth * scan.range

		self.move_scanners()
		
	def max_depth(self):
		return max([s.depth for s in self.scanners])

	def max_range(self):
		return max([s.range for s in self.scanners])

	def find(self, depth):
		for s in self.scanners:
			if s.depth == depth:
				return s
		return None

	def __str__(self):
		s = ''
		for i in range(self.max_depth()+1):
			s += ' {}  '.format(i)
			
		s = s[:-1] + '\n'

		
		for y in range(1,self.max_range()+1):
			for x in range(self.max_depth()+1):
				scan = self.find(x)
				if scan is None or y > scan.range:
					s += '    '
				else:
					if scan.pos == y:
						if y == 1 and x == self.packet_depth:
							s += '(S) '
						else:
							s += '[S] '
					else:
						if y == 1 and x == self.packet_depth:
							s += '( ) '
						else:
							s += '[ ] '
						
			s = s[:-1] + '\n'
			
		return s

firewall = Firewall()
			
with open('part1.input') as f:
	for line in f:
		d, r = line[:-1].split(': ')
		firewall.add(d, r)

for i in range(firewall.max_depth()+1):
	firewall.move()

print('Trip severity: {}'.format(firewall.severity))
