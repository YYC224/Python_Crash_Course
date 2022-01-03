toppings=[]
new_topping = ""
while new_topping!="quit":
	message = "\n\n(Enter quit to end the program)."
	message+="\nPlease input the topping: "
	new_topping=input(message)
	toppings.append(new_topping)
	print("There are your toppings: ", end='')
	for topping in toppings:
		print(topping,end = ' ')
print("\nThank you for coming!")