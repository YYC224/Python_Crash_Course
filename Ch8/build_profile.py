def build_profile(first, last, **user_info):
	'''创建一个字典，包含知道的一切user信息'''
	user_info['first_name']=first
	user_info['last_name']=last

	return user_info


user_profile = build_profile('Yuchen','Ye',University='XJTU',city='Beijing')

print(user_profile)