# traces out the spiral
def spiral():
	step = 0
	while True:
		# right
		step += 1
		yield (1,0, step)
		
		# up
		yield (0,1, step)
		
		# left
		step += 1
		yield (-1,0, step)
		
		# down
		yield (0,-1, step)

# find the (x,y) location of a number
def next_val(num):
	val = 1
	x = 0
	y = 0
	bag = []

	for vx, vy, step in spiral():
#		print(vx, vy, step, val)
		for i in range(step):
			bag += [(x,y,val)]
			if val > num:
				return val

			x += vx
			y += vy

			adj = [l for l in bag if (abs(x-l[0]) <= 1) and (abs(y-l[1]) <= 1)]
#			print(adj)
			val = 0
			for a in adj:
				val += a[2]

input = 312051
print("Next value is {0}".format(next_val(input)))
