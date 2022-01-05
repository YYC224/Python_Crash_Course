"""一组用于表示管理员的类"""

from user import User

class Privileges():
	"""特权"""

	def __init__(self, privileges=[]):
		self.privileges=privileges

	def show_privileges(self):
		print(f"Privileges are: ")
		for privilege in self.privileges:
			print(privilege)


class Admin(User):
	"""管理员"""

	def __init__(self, first_name, last_name, age,privileges=[]):
		"""初始化属性"""
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges(privileges)

	# def show_privileges(self):
	# 	print(f"{self.first_name.title()} {self.last_name.title()}'s privileges are: ")
	# 	for privilege in self.privileges:
	# 		print(privilege)