toppings=[]
while True:
	message = "\n\n(Enter quit to end the program)."
	message+="\nPlease input the topping: "
	new_topping=input(message)
	if new_topping=='quit':
		break
	else:
		toppings.append(new_topping)
		print("There are your toppings: ", end='')
		for topping in toppings:
			print(topping,end = ' ')
print("Thank you for coming!")