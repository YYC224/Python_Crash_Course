from restaurant import Restaurant, IceCreamStand

my_store = IceCreamStand('YYC Store','Icecream')
print(my_store.restaurant_name)
print(my_store.cuisine_type)

my_store.add_flavors('apple')
my_store.show_flavors()
my_store.add_flavors('banana')
my_store.show_flavors()