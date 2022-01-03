rivers={'nile':'egypt','yangtze':'china','amazon':'peru'}
for rever,nation in rivers.items():
	print(f"The {rever.title()} runs through {nation.title()}")
for rever in rivers.keys():
	print(rever)
for nation in rivers.values():
	print(nation)