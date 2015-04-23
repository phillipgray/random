# global variables
pyg = 'ay'

# helper functions
def find_vowel(orig_word):
	'''
	this function takes an string and
	returns the index of the first vowels
	as an int
	'''
	index = 0
	low_word = orig_word.lower()
	for char in low_word:
		if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
			vowel_index = index
			break
		index += 1
	return vowel_index



# actual control flow of script
game_end = False

while game_end == False:
	original = raw_input('Enter a word: ')

	if len(original) > 0 and original.isalpha():
	    word = original.lower()

	    first_vowel_index = find_vowel(word)
	    first_chunk = word[0:first_vowel_index]
	    
	    new_word = word[first_vowel_index:] + first_chunk + pyg

	    print new_word

	else:
	    print "That's not a word, you urkeytay! Try again!"


	while True:    
		play_again = raw_input("Would you like to translate another word? ")
		
		if play_again.lower() == "y":
			break
		elif play_again.lower() == "n":
			game_end = True
			print "Aterlay!"
			break
		else:
			print "Huh?!"
			
