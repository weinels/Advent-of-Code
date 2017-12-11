import re

class Prgm:
	def __init__(self, string):
		m = re.match('(\S+) \((\d+)\)(.*)', string)
		if m:
			self.name = m.group(1)
			self.weight = int(m.group(2))
			above = m.group(3)[4:]
			if above == '':
				self.above = None
			else:
				self.above = above.split(', ')
			
		else:
			raise Exception

programs = []
with open('part1.input') as f:
	for line in f:
		programs += [Prgm(line[:-1])]

# find the base
for p in programs:
	above = [x for x in programs if (x.above is not None) and (p.name in x.above)]
	if len(above) == 0:
		# we found the base
		print("Base: {0}".format(p.name))
		break
