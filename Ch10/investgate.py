filename = 'reasons.txt'

while True:
	reason = input("Please input your reason: ")
	if reason =='quit':
		break
	with open(filename, 'a') as file_object:
		file_object.write(f"{reason}\n")