sandwich_orders=["apple sandwich","banana sandwich","pear sandwich","apple sandwich"]
finished_sandwichs=[]
print("Sorry! THe apple sandwich is sold out!")
while "apple sandwich" in sandwich_orders:
	sandwich_orders.remove("apple sandwich")
while sandwich_orders:
	print(f"I made your {sandwich_orders[0]}")
	finished_sandwichs.append(sandwich_orders.pop(0))
print("These sandwichs are finished: ",end='')
for sandwich in finished_sandwichs:
	print(sandwich,end=',')
