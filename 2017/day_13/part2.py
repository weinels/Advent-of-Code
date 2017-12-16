class Packet:
	def __init__(self, delay):
		self.depth = -1
		self.delay = delay
		self.caught = False

	def move(self):
		self.depth += 1

	def __str__(self):
		return '<{}:{} {}>'.format(str(self.depth), str(self.delay), str(self.caught))

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

	def reset(self):
		self.pos = 1
		self.vel = 1
		
class Firewall:
	def __init__(self):
		self.scanners = []

	def add(self, d, r):
		self.scanners.append(Scanner(int(d), int(r)))
		self.max_depth = max([s.depth for s in self.scanners])
		self.max_range = max([s.range for s in self.scanners])

	def move_scanners(self):
		for s in self.scanners:
			s.move()
			
	def find(self, depth):
		for s in self.scanners:
			if s.depth == depth:
				return s
		return None

	def check_packet(self, pkt):
		scan = self.find(pkt.depth)
		if scan is not None and scan.pos == 1:
			pkt.caught = True

firewall = Firewall()
			
with open('part1.input') as f:
	for line in f:
		d, r = line[:-1].split(': ')
		firewall.add(d, r)
i = 0
packets = []
while True:
	packets += [Packet(i)]

	for p in packets:
		p.move()
		firewall.check_packet(p)

	firewall.move_scanners()

	packets = [p for p in packets if p.caught is False]

	through = [p for p in packets if p.depth > firewall.max_depth]
	if len(through) > 0:
		break
	
	'''
	if i % 10000 == 0:
		if len(packets) > 0:
			print('{}: {}'.format(i,reduce(lambda x, y: str(x) + str(y),packets)))
		else:
			print('{}:'.format(i))
	'''
	i += 1


print('Smallest delay: {}'.format(through[0].delay))
