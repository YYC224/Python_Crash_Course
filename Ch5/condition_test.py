car="subaru"
print("Is car == 'subaru'? I predict True")
print(car=='subaru')
print("\nIs car =='audi'? I predict False")
print(car == 'audi')

print("\nTest_1")
str_1="abc"
str_2="abcd"
if (str_1==str_2):
	print("str_1=str_2")
else:
	print("str_1!=str_2")

print("\nTest_2")
name="john"
user_name="John"
if(user_name.lower()==name):
	print("Please change your name!")
else:
	print("OK!")

print("\nTest_3")
num1=10
num2=5
if(num1>=num2):
	print("num1>=num2")
else:
	print("num1<num2")

print("\nTest_4")
num=6
if(num>4) and (num<10):
	print("OK!")
if (num>5) or (num<3):
	print("OK!")	

print("\nTest_5")
nums=[value**2 for value in range(1,6)]
print(nums)
for value in range(1,6):	
	if value not in nums:
		print(f"{value} is not in the nums list!")
	else:
		print(f"{value} is in the nums list!")
