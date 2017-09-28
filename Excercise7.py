import random

computerinput = 0
playagain = "y"

while playagain == "y" :
    playerchoice = input("Enter 1 = rock, 2 = paper and 3 = scissors: ")
    if playerchoice == 1 :
        print "You picked rock!"
        computerinput = random.randrange(3)+1
        if computerinput == 1 :
            print "Computer picked rock! You tie!"
        elif computerinput == 2 :
            print "Computer picked paper! You lose!"
        elif computerinput == 3 :
            print "Computer picked scissors! You win!"

    elif playerchoice == 2 :
        print "You picked paper!"
        computerinput = random.randrange(3)+1
        if computerinput == 1 :
            print "Computer picked rock! You win!"
        elif computerinput == 2 :
            print "Computer picked paper! You tie!"
        elif computerinput == 3 :
            print "Computer picked scissors! You lose!"
            
    elif playerchoice == 3 :
        print "You picked scissors!"
        computerinput = random.randrange(3)+1
        if computerinput == 1 :
            print "Computer picked rock! You lose!"
        elif computerinput == 2 :
            print "Computer picked paper! You win!"
        elif computerinput == 3 :
            print "Computer picked scissors! You tie!"

    else :
        print "Pick 1, 2 or 3!"

    playagain = raw_input("Do you want to go again? y for Yes, any other button for No ")

print "Buh Bye!"

