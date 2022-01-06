filename = 'cats.txt'

with open(filename, 'a') as f:
	while True:
		cat = input("Please input your cat's name: ")
		if cat == 'quit':
			break
		else:
			f.write(f"{cat}\n")