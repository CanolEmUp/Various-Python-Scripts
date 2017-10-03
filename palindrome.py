# Wathaned Ean
def name_input():
	global name
name = raw_input("What is the word? ")

def palindrome():
        # using slice notation, leave start and end blank, use step of -1 to reverse word and see if it is a palindrome
	if name == name[::-1]:
		print "The word is a palindrome!"
	else :
		print "The word is not a palindrome."
# main
name_input()
palindrome()
