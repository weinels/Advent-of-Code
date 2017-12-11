from collections import deque

def window(s, n=2):
	sit = iter(s)
	w = deque((next(sit, None) for _ in xrange(n)), maxlen=n)
	yield w
	append = w.append
	for x in sit:
		append(x)
		yield w

def input(file):
	with open(file) as f:
		first = None
		for line in f:
			for c in line:
				if c != '\n':
					if first is None:
						first = int(c)
					yield(int(c))
		# tack the first item at the end to simulate the cicular list
		yield(first)

					
sum = 0

for w in window(input('part1.input')):
#	print("{0}->{1}".format(w[0],w[1]))
	if w[0] == w[1]:
		sum += w[0]

print("Sum is {0}".format(sum))
