def make_car(manufacture, model, **car_info):
	'''car messages'''
	car_info['manufacture'] = manufacture
	car_info['model'] = model
	return car_info


car = make_car('sabaru','outback',color='blue',tow_package=True)

print(car)