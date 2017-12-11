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
def grid_loc(num):
	val = 1
	x = 0
	y = 0

	for vx, vy, step in spiral():
#		print(vx, vy, step, val)
		for i in range(step):
			if val == num:
				return (x,y)

			x += vx
			y += vy
			val += 1

def manhatten_dist(pos):
	return abs(pos[0])+abs(pos[1])
			
#for i in range(1,23):
#	print("{0}: {1} = {2}".format(i,grid_loc(i), manhatten_dist(grid_loc(i))))
		
#print("{0}: {1} = {2}".format(i,grid_loc(1), manhatten_dist(grid_loc(1))))
#print("{0}: {1} = {2}".format(i,grid_loc(12), manhatten_dist(grid_loc(12))))
#print("{0}: {1} = {2}".format(i,grid_loc(23), manhatten_dist(grid_loc(23))))
#print("{0}: {1} = {2}".format(i,grid_loc(1024), manhatten_dist(grid_loc(1024))))

input = 312051
pos = grid_loc(input)
print("Steps = {0}".format(manhatten_dist(pos)))
