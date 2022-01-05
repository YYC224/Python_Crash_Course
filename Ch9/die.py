import random

class Die:
	"""一个模拟骰子的类"""

	def __init__(self, sides=6):
		"""初始化属性"""
		self.sides=sides

	def roll_die(self):
		"""打印一个位于1和sides之间的随机数"""
		print(random.randint(1,self.sides), end=' ')

sides = [6, 10, 20]
for side in sides:
	my_die=Die(side)
	print(f"\nMy die has {my_die.sides} sides.")
	for i in range(0,10):
		my_die.roll_die()