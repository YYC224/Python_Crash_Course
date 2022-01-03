cities = {
	'Beijing':{
		'country':'china',
		'population':'many',
		'fact':'high school',
	},
	"Xi'an":{
		'country':'china',
		'population':'some',
		'fact':'university',
	}
}
for city, messages in cities.items():
	print(f"In {city}:")
	for key,value in messages.items():
		print(f"The {key} is {value}")