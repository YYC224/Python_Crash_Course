"""一个用于表示用户的类"""

class User:
	"""用户"""

	def __init__(self, first_name, last_name, age):
		"""初始化属性"""
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.login_attempts=0
	
	def describe_user(self):
		"""打印用户摘要"""
		msg = f"User's name is {self.first_name.title()} {self.last_name.title()} "
		msg += f"and the age is {self.age}"
		print(msg)

	def greet_user(self):
		print(f"Hello! {self.first_name.title()} {self.last_name.title()}.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0






# yyc=User('Yuchen','Ye',21)
# yyc.describe_user()
# yyc.greet_user()

# mpy=User('Peiyu','Ma',22)
# mpy.describe_user()
# mpy.greet_user()

# yyc.increment_login_attempts()
# yyc.increment_login_attempts()
# print(yyc.login_attempts)
# yyc.reset_login_attempts()
# print(yyc.login_attempts)

# privileges = ['can add post','can delete post','can ben user']
# mpy = Admin('Peiyu', 'Ma','22',privileges)
# mpy.privileges.show_privileges()