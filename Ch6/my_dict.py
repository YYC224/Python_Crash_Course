mydict={
	'animal':'cat',
	'fruit':'apple',
	'city':'Beijing',
}
mydict['age']=18
# print(f"animal: {mydict['animal']}")
# print(f"fruit: {mydict['fruit']}")

for key,value in mydict.items():
	print(f"{key}:{value}")