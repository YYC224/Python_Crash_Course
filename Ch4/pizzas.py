pizzas=["pizza_A","pizza_B","pizza_C"]
for pizza in pizzas:
	message=f"I like {pizza}"
	print(message)
print("I really love pizza!")

print("The first two items in the list are:")
for pizza in pizzas[:2]:
	print(pizza)
print("The middle item in the list is:")
for pizza in pizzas[1:2]:
	print(pizza)
print("The last two items in the list are:")
for pizza in pizzas[-2:]:
	print(pizza)
print("\n")
friend_pizzes=pizzas[:]
print("my pizzas:")
for pizza in pizzas:
	print(pizza)
print("friend's pizzas:")
for pizza in friend_pizzes:
	print(pizza)	
pizzas.append("mynew")
friend_pizzes.append("friendnew")
print("my pizzas:")
for pizza in pizzas:
	print(pizza)
print("friend's pizzas:")
for pizza in friend_pizzes:
	print(pizza)	