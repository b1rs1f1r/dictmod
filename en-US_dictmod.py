'''
This dictionary prepared by
Enes Işık, with Python.
All rights reserved.
'''

dictionary={"book":"kitap","computer":"bilgisayar","apple":"elma","pen":"kalem"}

def search(word):
	error="{} isn't in dictionary!"
	return dictionary.get(word,error.format(word))

def add(word,meaning):
	message="{} is added to dictionary!"
	dictionary[word]=meaning
	print(message.format(word))

def delete(word):
	try:
		dictionary.pop(word)
	except KeyError as err:
		print(err, "Word not found!")
	else:
		print("{} is deleted from dictionary!".format(word))