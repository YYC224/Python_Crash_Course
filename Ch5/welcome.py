users=["A","B","C","D","admin"]
# users=[]
if users:
	for user in users:
		if (user == "admin"):
			print("Hello admin!")
		else:
			print(f"Hello {user}!")
else:
	print("We need more users!")
