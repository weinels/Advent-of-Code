class KnotHash:
	def __init__(self, size=255):
		self.string = range(size)
		self.pos = 0
		self.skip = 0

	def update(self, length):
#		print(self)
		right = len(self.string) - self.pos

		if right < length:
			width = right
			extra = length - right
		else:
			width = length
			extra = 0

#		print("length: {}\nright: {}\nwidth: {}\nextra: {}".format(length, right, width, extra))
		
		sub = self.string[self.pos:self.pos + width]
		sub += self.string[0:extra]

		sub.reverse()

		self.string[self.pos:self.pos + width] = sub[0:width]
		self.string[0:extra] = sub[width:]

		# move
		self.pos = (self.pos + length + self.skip) % len(self.string)
		
		# increase
		self.skip += 1

#		print(self)
#		raw_input()
		
	def digest(self):
		return self.string[0] * self.string[1]

	def __str__(self):
		s = ''
		for i in range(len(self.string)):
			if self.pos == i:
				s += '[' + str(self.string[i]) + '] '
			else:
				s += str(self.string[i]) + ' '
		return s[:-1]

input = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
#input = "3,4,1,5"


hash = KnotHash(256)

for l in [int(x) for x in input.split(',')]:
	hash.update(l)

print("Product of first two numbers: {}".format(hash.digest()))
