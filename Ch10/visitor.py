filename = 'guest_book.txt'

while True:
	name = input("Please input your name: ")
	if name == 'quit':
		break
	else:
		print(f"Hello {name}!")
	with open(filename,'a') as file_object:
		file_object.write(f"{name}\n")