filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			content = f.read()
		
	except FileNotFoundError:
		pass
		# print(f"Cant't find {filename}")
	else:
		print(content)