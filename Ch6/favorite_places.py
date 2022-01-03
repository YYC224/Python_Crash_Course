favorite_places = {
	'yyc':['Beijing','Shanghai'],
	'mpy':["Xi'an"],
}
for key,value in favorite_places.items():
	if len(value)==1:
		print(f"\n{key.title()}'s favorite place is:")
	elif len(value)>1:
		print(f"\n{key.title()}'s favorite places are:")
	for place in value:
		print(f"\t{place}")