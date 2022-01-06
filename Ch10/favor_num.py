import json

filename = 'favorite_num.txt'

try:
	with open(filename) as f:
		favor_num = f.read()
	
except FileNotFoundError:
	num = input("Please input your favorite number: ")
	with open(filename, 'w') as f:
		f.write(num)
else:
	print(f"I know your favorite number! It's {favor_num}!")