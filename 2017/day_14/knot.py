class KnotHash:
	def __init__(self):
		self.string = range(256)
		self.pos = 0
		self.skip = 0
		self.hash = ''
		
	def _single(self, length):
		right = len(self.string) - self.pos

		if right < length:
			width = right
			extra = length - right
		else:
			width = length
			extra = 0

		sub = self.string[self.pos:self.pos + width]
		sub += self.string[0:extra]

		sub.reverse()

		self.string[self.pos:self.pos + width] = sub[0:width]
		self.string[0:extra] = sub[width:]

		# move
		self.pos = (self.pos + length + self.skip) % len(self.string)
		
		# increase
		self.skip += 1

	def update(self, input):
		lengths = [ord(x) for x in input]
		lengths += [17, 31, 73, 47, 23]

		for a in range(64):
			for l in lengths:
				self._single(l)

	def digest(self):
		dh = range(16)
		for i in range(16):
			dh[i] = self.string[16*i] 	
			for j in range(1, 16):
				dh[i] = dh[i] ^ self.string[16*i+j]

		hash = ''
		for x in dh:
			hash += format(x, '#04x')[2:]

		return hash

	def __str__(self):
		s = ''
		for i in range(len(self.string)):
			if self.pos == i:
				s += '[' + str(self.string[i]) + '] '
			else:
				s += str(self.string[i]) + ' '
		return s[:-1]
