

def show_messages(messages):
	'''show messages'''
	for message in messages:
		print(message)


def sent_msg(messages,sent_messages):
	'''send messages'''
	while messages:
		current_msg = messages.pop()
		print(current_msg)
		sent_messages.append(current_msg)

messages = ["Hi","Hello","Good morning!"]	
sent_messages=[]

# show_messages(messages)
sent_msg(messages[:],sent_messages)

msgs=[messages,sent_messages]
for msg in msgs:
	print(msg)