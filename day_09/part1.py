class Stack:
	def __init__(self):
		self.stack = []

	def peek(self):
		if len(self.stack) == 0:
			return ''
		else:
			return self.stack[-1]

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		if len(self.stack) == 0:
			return ''
		else:
			return self.stack.pop()

	def __len__(self):
		return len(self.stack)

	def __str__(self):
		if len(self.stack) == 0:
			return "Empty"
		s = ''
		self.stack.reverse()
		for i in self.stack:
			s += i + ' -> '
		self.stack.reverse()
		return s[:-4]

def stream_score(stream):
	ops = Stack()
	cancel = False
	score = 0
	
	for c in stream:
#		print("'{}':".format(c))
#		print("Stack Before: {}".format(ops))
		
		if cancel is True:
			cancel = False
		else:
			if c == '!':
				cancel = True

			elif (c == '<' or c == '{') and ops.peek() <> '<':
				ops.push(c)

			elif c == '}' and ops.peek() == '{':
				score += len(ops)
				ops.pop()

			elif c == '>' and ops.peek() == '<':
				ops.pop()
#			else:
#				print("Ignore '{}'".format(c))
				
#		print("Stack After:  {}".format(ops))
#		print("Score: {}".format(score))
#		print
#		raw_input()

	return score

def test(stream, correct):
	print("Stream: {}".format(stream))
	score = stream_score(stream)
	print("Score: {}".format(score))
	if score == correct:
		print("Pass")
	else:
		print("Fail, expected {}".format(correct))
	print	

'''
test('{}', 1)
test('{{{}}}', 6)
test('{{},{}}', 5)
test('{{{},{},{{}}}}', 16)
test('{<a>,<a>,<a>,<a>}', 1)
test('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9)
test('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9)
test('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)
'''

with open('part1.input') as f:
	for line in f:
		print("Score is {}".format(stream_score(line[:-1])))
