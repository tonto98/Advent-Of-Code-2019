def formula(x):
	"""
	while(rez > 0):
		rez += int(rez/3) -2
	return rez
	"""
	rez = int(x/3) -2
	if(rez > 0):
		return rez + formula(rez)
	return 0
	


f = open("in.txt")
lines = f.readlines()
sum = 0


for line in lines:
	sum += formula(int(line))
	
print(sum)
