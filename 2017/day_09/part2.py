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

def garbage_count(stream):
	ops = Stack()
	cancel = False
	count = 0
	
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
				ops.pop()

			elif c == '>' and ops.peek() == '<':
				ops.pop()
				
			elif ops.peek() == '<':
				count += 1
#			else:
#				print("Ignore '{}'".format(c))
				
#		print("Stack After:  {}".format(ops))
#		print("Score: {}".format(score))
#		print
#		raw_input()

	return count

def test(stream, correct):
	print("Stream: {}".format(stream))
	count = garbage_count(stream)
	print("Count: {}".format(count))
	if count == correct:
		print("Pass")
	else:
		print("Fail, expected {}".format(correct))
	print	

'''
test('{}', 0)
test('{{{}}}', 0)
test('{{},{}}', 0)
test('{{{},{},{{}}}}', 0)
test('{<a>,<a>,<a>,<a>}', 4)
test('{{<ab>},{<ab>},{<ab>},{<ab>}}', 8)
test('{{<!!>},{<!!>},{<!!>},{<!!>}}', 0)
test('{{<a!>},{<a!>},{<a!>},{<ab>}}', 17)
test('<>', 0)
test('<random characters>', 17)
test('<<<<>', 3)
test('<{!>}>', 2)
test('<!!>', 0)
test('<!!!>>', 0)
test('<{o"i!a,<{i<a>', 10)
'''

with open('part1.input') as f:
	for line in f:
		print("Count is {}".format(garbage_count(line[:-1])))

