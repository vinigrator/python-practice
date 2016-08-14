def count_names():
	names = {}
	with open('names.txt', 'r') as f:
		for line in f:
			line = line[:-1]
			if names.get(line) == None :
				names[line] = 0
			else :
				names[line] += 1
	f.close()
	for key, value in names.items():
		print key + " " + str(value)
		
count_names()