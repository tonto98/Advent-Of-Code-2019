f = open("in.txt")
lines = f.readlines()
array = lines[0].strip().split(",")
originalIpnut = [int(i) for i in array]


GOAL = 19690720


#before?
for noun in range(0,100):
	for verb in range(0,100):

		results = originalIpnut.copy()
		results[1] = noun
		results[2] = verb

		currIndex = 0
		while (results[currIndex] != 99):
			if results[currIndex] == 1:
				#add
				results[results[currIndex+3]] = results[results[currIndex+1]] + results[results[currIndex+2]]

			elif results[currIndex] == 2:
				#multiply
				results[results[currIndex+3]] = results[results[currIndex+1]] * results[results[currIndex+2]]
			currIndex += 4
		if(results[0] == GOAL):
			print("FINALNO: " + str(100*results[1] + results[2]))
			break



print(results)
print("------------------------")
print(originalIpnut)














"""
f = open("in.txt")
lines = f.readlines()
array = lines[0].strip().split(",")
results = [int(i) for i in array]

#before?
results[1] = 12
results[2] = 2


currIndex = 0

while (results[currIndex] != 99):
	if results[currIndex] == 1:
		#add
		results[results[currIndex+3]] = results[results[currIndex+1]] + results[results[currIndex+2]]

	elif results[currIndex] == 2:
		#multiply
		results[results[currIndex+3]] = results[results[currIndex+1]] * results[results[currIndex+2]]
	currIndex += 4

print(results)
"""