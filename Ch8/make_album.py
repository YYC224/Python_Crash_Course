def make_album(singer_name, album_name, songs_num=None):
	'''create album dictionary'''
	album={}
	album['singer_name']=singer_name
	album['album_name']=album_name
	if songs_num:
		album['songs_num']=songs_num
	return album

while True:
	print("Enter 'quit' to end the program.")

	singer_name = input("Please input singer's name: ")
	if singer_name == 'quit':
		break

	album_name = input ("Please input album's name: ")
	if album_name == 'quit':
		break

	songs_num = input ("Please input the number of songs: (a number/No)")
	
	if songs_num != 'No':
		songs_num=int(songs_num)
		album=make_album(singer_name,album_name,songs_num)
		print(f"\nThe singer's name is {album['singer_name']}.")
		print(f"The album's name is {album['album_name']}")
		print(f"The songs number is {album['songs_num']}")

	else:
		album=make_album(singer_name,album_name)
		print(f"\nThe singer's name is {album['singer_name']}.")
		print(f"The album's name is {album['album_name']}")
