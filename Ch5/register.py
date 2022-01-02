current_users=["A","B","C","D","admin"]
# current_users_lower=[]
# for current_user in current_users:
# 	current_users_lower.append(current_user.lower())
current_users_lower=[ i.lower() for i in current_users ]
print(current_users_lower)
new_users=["e","f","g","h","Admin"]
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Please change it!")
	else:
		print("OK!")