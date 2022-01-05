class Restaurant:
	"""模拟餐厅"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""打印两条信息"""
		print(f"{self.restaurant_name}'s name is {self.restaurant_name}.")

	def open_restaurant(self):
		"""打印一条信息"""
		print(f"{self.restaurant_name}'s restaurant is opened!")

	def set_number_served(self, number_served):
		"""设置就餐人数"""
		self.number_served = number_served

	def increment_number_served(self, increment):
		self.number_served += increment

class IceCreamStand(Restaurant):
	"""冰激凌小店"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化父类的属性"""
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=[]

	def add_flavors(self, flavor):
		"""添加风味"""
		self.flavors.append(flavor)

	def show_flavors(self):
		"""打印风味列表"""
		for flavor in self.flavors:
			print(flavor)


# my_restaurant = Restaurant('CanTing','China')
# your_restaurant = Restaurant('Canteen','Amarica')

# print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
# print(f"My restaurant's cuisine type is {my_restaurant.cuisine_type}.")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# your_restaurant.describe_restaurant()
# print(my_restaurant.number_served)
# my_restaurant.number_served = 10
# print(my_restaurant.number_served)
# my_restaurant.set_number_served(20)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(5)
# print(my_restaurant.number_served)

# my_store = IceCreamStand('YYC Store','Icecream')
# print(my_store.restaurant_name)
# print(my_store.cuisine_type)

# my_store.add_flavors('apple')
# my_store.show_flavors()
# my_store.add_flavors('banana')
# my_store.show_flavors()