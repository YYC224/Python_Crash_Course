guests=["Tom","Bob","Susan"]
message=f"Hello!{guests[0]}, {guests[1]} and {guests[2]}. Would you want to have a meeting with me?"
print(message)
message_2=f"Sorry! {guests.pop(-1)} can't attend this meeting!"
print(message_2)
guests.append("New guest")
message=f"Hello!{guests[0]}, {guests[1]} and {guests[2]}. Would you want to have a meeting with me?"
print(message)
print("Oh! I've found a bigger table!")
guests.insert(0,"New guest2")
guests.insert(1,"New guest3")
guests.append("New guest4")
for i in range(0,len(guests)):
	print(guests[i])
	print("\t")
print(f"Sorry, there are only two people be invited!")
#only left 2 perple
for i in range(0,len(guests)-2): 
	print(f"Sorry! {guests.pop()}")
for i in range(0,len(guests)):
	print(f"Hi! {guests[i]}")
print(f"There are totally {len(guests )} perple!")
while len(guests)!=0:
	del guests[0]
for i in range(0,len(guests)):
	print(guests[i])
