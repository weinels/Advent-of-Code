import re

def find_group(program, group=[]):
#	print('[Enter] Program: {} Group: {}'.format(program, group))
#	raw_input()

	if program not in group:
		group += [program]
		
	for c in pipes[program]:
		if c not in group:
			find_group(c, group)

#	print('[Exit] Program: {} Group: {}'.format(program, group))
	return group

pipes = {}
with open('part1.input') as f:
	for line in f:
		m = re.match('(\d+) <-> (.+)', line)
		if m:
			program = int(m.group(1))
			connections = [int(x) for x in m.group(2).split(', ')]

			if program in pipes:
				raise Exception

			pipes[program] = connections

print("There are {} programs.".format(len(find_group(0))))
