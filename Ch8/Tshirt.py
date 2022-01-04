def make_shirt(size='L', style='I love Python'):
	'''print some message'''
	print(f"The size of shirt is {size} and the style is {style}.")


#positional arguments
make_shirt('M', 'free')

#key arguments
make_shirt(size='S',style='yyc')

make_shirt()
make_shirt('M')
make_shirt(style='I love C')
