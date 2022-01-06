import json

def get_stored_username():
	'''如果存储了username，就返回；否则，返回None'''
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username		

def get_new_username():
	"""获取新用户的用户名，存储到'username.json'文件，并返回username"""
	username = input("Please input your username: ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""问候用户，并指出其username"""
	username = get_stored_username()
	if username:
		flag = input(f"Are you {username}?(yes/no)" )
		if (flag == 'yes'):
			print(f"Welcome back, {username}!")
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()