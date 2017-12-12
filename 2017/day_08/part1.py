import re
import operator
from collections import namedtuple

class Instruction:
	Condition = namedtuple('Condition', ['register', 'operator', 'value'])
	def __init__(self, str):
		m = re.match('(\S+) (\S+) (\S+) if (.*)', str)
		if m:
			self.register = m.group(1)
			
			if m.group(2) == 'inc':
				self.amount = int(m.group(3))
			else:
				self.amount = -1 * int(m.group(3))
				
			cond = m.group(4).split(' ')
			
			if cond[1] == '==':
				op = lambda x,y: x == y
			elif cond[1] == '!=':
				op = lambda x,y: x <> y
			elif cond[1] == '>':
				op = lambda x,y: x > y
			elif cond[1] == '>=':
				op = lambda x,y: x >= y
			elif cond[1] == '<':
				op = lambda x,y: x < y
			elif cond[1] == '<=':
				op = lambda x,y: x <= y
			else:
				raise Exception
				
			self.condition = self.Condition(cond[0], op, int(cond[2]))
		else:
			raise Exception

	def __str__(self):
		s = self.register + ' '
		if self.increase:
			s += 'inc '
		else:
			s += 'dec '
		s += str(self.amount) + ' '

		s += 'if '
		for c in self.condition:
			s += str(c) + ' '

		return s[:-1]
		

class Register_Bank:
	def __init__(self):
		self.registers = {}

	def run_instruction(self, inst):
#		print(inst)
		
		if inst.condition.operator(self.registers.get(inst.condition.register,0), inst.condition.value):
			self.registers[inst.register] = self.registers.get(inst.register,0) + inst.amount

#		print(self.registers)

	def largest_value(self):
		if len(self.registers) == 0:
			return (None, None)
			
		key = max(self.registers.iteritems(), key=operator.itemgetter(1))[0]
		return (key, self.registers[key])

bank = Register_Bank()

with open('part1.input') as f:
	for line in f:
		inst = Instruction(line)
		bank.run_instruction(inst)

print("Register {large[0]} has the largest value ({large[1]}).".format(large=bank.largest_value()))
