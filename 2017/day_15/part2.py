class Generator:
	def __init__(self, factor, start, criteria):
		self.factor = factor
		self.prev = start
		self.criteria = criteria

	def gen(self):
		while True:
			self.prev = (self.prev * self.factor) % 2147483647
			if self.prev % self.criteria == 0:
				return self.prev


def low_16b(n):
		s = format(n,'016b')
		return s[-16:]

A = Generator(16807, 591,4)
B = Generator(48271, 393,8)
total = 0

i = 0
while i < 5000000:
#	print('{}\t{}'.format(A.gen(), B.gen()))
	A_low = low_16b(A.gen())
	B_low = low_16b(B.gen())
	if A_low == B_low:
		total += 1
	i += 1

print('Judge\'s final count: {}'.format(total)) 
