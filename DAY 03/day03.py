import math

pathh = []
pathh.append([1,2])
pathh.append([1,4])
print(pathh[-1][1])
"""
def move(direction, length, path):
	if direction == 'R':
		for i in range(1,length+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x+1,y])
	elif direction == 'L':
		for i in range(1,length+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x-1,y])
	elif direction == 'D':
		for i in range(1,length+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x,y-1])
	elif direction == 'U':
		for i in range(1,length+1):
			x = path[-1][0]
			y = path[-1][1]
			path.append([x,y+1])
	





f = open("in.txt")
line1, line2 = f.readlines()
line1 = line1.strip().split(",")
line2 = line2.strip().split(",")

path1 = []
path1.append([0,0])

path2 = []
path2.append([0,0])







for command in line1:
	direction = command[0]
	length = int(command[1:])
	move(direction,length,path1)

for command in line2:
	direction = command[0]
	length = int(command[1:])
	move(direction,length,path2)

colisions = []
mini = 9999
step_mini = math.inf

for point in path1:
	if point in path2:
		dist = abs(point[0]) + abs(point[1])
		steps1 = path1.index(point)
		steps2 = path2.index(point)
		sum_of_steps = steps1 + steps2

		if dist == 0:
			print("kek")
		elif mini > dist:
			mini = dist

		if sum_of_steps == 2:
			print("kek")
		elif step_mini > sum_of_steps:
			step_mini = sum_of_steps
		print(point)

print(mini)
print(step_mini)

"""