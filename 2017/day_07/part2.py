import re

class Node:
	def __init__(self, name, weight, parent=None):
		self.name = name
		self.weight = weight
		self.leafs = None
		self.parent = parent

	def __str__(self):
		s = self.name + " (" + str(self.weight) + ")"
		if self.leafs is not None:
			s += " -> "
			for l in self.leafs:
				s += l.name + " "
		return s

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

class Programs:
	def __init__(self):
		self.bag = []
		self.root = ''

	def add(self, string):
		self.bag += [Prgm(string)]

		for p in self.bag:
			above = [x for x in self.bag if (x.above is not None) and (p.name in x.above)]
			if len(above) == 0:
				self.root = p.name
				break
	def get(self, name):
		return [x for x in self.bag if (x.name == name)][0]

	def _build_tree(self, name, parent=None):
		p = self.get(name)

		node = Node(p.name, p.weight, parent)

		if p.above is not None:
			node.leafs = [self._build_tree(x, node) for x in p.above]

		return node
		
	def build_tree(self):
		return self._build_tree(self.root)
		
prgmlist = Programs()
				
with open('part1.input') as f:
	for line in f:
		prgmlist.add(line[:-1])

root = prgmlist.build_tree()

def tree_weight(tree):
	if tree.leafs is None:
		return tree.weight

	return tree.weight + sum([tree_weight(x) for x in tree.leafs])

def balanced_tree(tree):
	if tree.leafs is None:
		return True

	return 1 == len(set([tree_weight(x) for x in tree.leafs]))

def wrong_weight(tree):
	if balanced_tree(tree):
		return tree

	leaf_weights = [(x,tree_weight(x)) for x in tree.leafs]
	weights = [x[1] for x in leaf_weights]

	for l in leaf_weights:
		if weights.count(l[1]) == 1:
			return wrong_weight(l[0])

def print_tree(tree, ind=0):
	s = ''.join(['-' for x in range(ind)])
	s += tree.name
	print(s)

	if tree.leafs is not None:
		for l in tree.leafs:
			print_tree(l, ind+1)

w = wrong_weight(root)

'''
print(w)
for l in w.leafs:
	print(tree_weight(l))

print(w.parent)
for l in w.parent.leafs:
	print(tree_weight(l))
'''

weights = [tree_weight(x) for x in w.parent.leafs if x.name <> w.name]
print("{0} needs weight {1}".format(w.name,w.weight - (tree_weight(w) - weights[0])))
