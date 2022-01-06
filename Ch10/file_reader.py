filename = 'learning_python.txt'

print("\n Method 1:")
with open(filename) as file_object:
	content = file_object.read()
print(content)	

print("\n Method 2:")
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip().replace('Python','C'))

print("\n Method 3:")
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())