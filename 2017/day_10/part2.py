class KnotHash:
	def __init__(self):
		self.string = range(256)
		self.pos = 0
		self.skip = 0
		self.hash = ''
		
	def _single(self, length):
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
#				print("i:{}	j:{}".format(i,j))
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

def test(input, valid):
	hash = KnotHash()
	hash.update(input)
	h = hash.digest()

	print("Input: {}".format(input))
	print("Hash:  {}".format(h))
	if h == valid:
		print("Pass")
	else:
		print("Fail, expected {}".format(valid))

'''
test('', 'a2582a3a0e66e6e86e3812dcb672a272')
test('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd')
test('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d')
test('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
'''

input = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"

hash = KnotHash()
hash.update(input)

print("Hash: {}".format(hash.digest()))
