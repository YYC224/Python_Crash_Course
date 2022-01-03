person1={'first_name':'Ye','last_name':'Yuchen','age':21,'city':'Beijing'}
person2={'first_name':'Wu','last_name':'Yuchen','age':20,'city':'Beijing'}
person3={'first_name':'Su','last_name':'Yuchen','age':19,'city':'Beijing'}
people=[]
people.append(person1)
people.append(person2)
people.append(person3)
print(people)
for person in people:
	for key,value in person.items():
		print(f"{key} is {value}")
	print("\n")