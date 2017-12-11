with open('part1.input') as f:
	valid = 0
	for line in f:
		words = line[:-1].split(' ')
		if len(words) == len(set(words)):
			valid += 1

print("Valid passphrases: {0}".format(valid))
