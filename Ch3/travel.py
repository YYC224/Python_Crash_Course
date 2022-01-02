cities=["Beijing","Shanghai","Guangzhou","Shenzhen"]

print("Here is the original list:")
print(cities)

#not changed
#sort()
print("\nHere is the sorted list:")
print(sorted(cities))
print("Here is the original list again:")
print(cities)

print("\nHere is the reversed sorted list:")
print(sorted(cities,reverse=True))
print("Here is the original list again:")
print(cities)

#changed
#.reverse()
print("\nHere is the reversed list:")
cities.reverse()
print(cities)
print("Here is the original list again:")
cities.reverse()
print(cities)

#changed
#.sort()
print("\nHere is the sorted list:")
cities.sort()
print(cities)
print("\nHere is the reversed sorted list:")
cities.reverse()
print(cities)
