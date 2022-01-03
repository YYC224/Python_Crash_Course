favorite_nums={
	'Tom':[1,2,3],
	'Bob':[4,5,6],
	'Susan':[7,8,9],
}
# print(favorite_nums)
for name,nums in favorite_nums.items():
	print(f"\n{name}'s favorite numbers are:")
	for num in nums:
		print(f"{num}",end = ' ')