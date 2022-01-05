import random

nums = list(range(0,10))
letters = ['a','b','c','d','e']
for letter in letters:
	nums.append(letter)

# print(nums)


counter = 0
lottery = []
my_ticket = [1,2,3,4]

while lottery!=my_ticket:
	counter += 1
	lottery = []
	for i in range(0,4):
		lottery.append(random.choice(nums))

print(f"You need buy {counter} tickets to win a prize!")