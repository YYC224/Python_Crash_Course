print("Please input two number to sum up:\n")
while True:
	x = input("First number: ")

	y = input("Second number: ")

	try:
		x = int(x)
		y = int(y)
	except ValueError:
		print("\nPlease input two number instead of text!")
	else:
		print(f"sum is {x+y}")