import random
def randomnumber():
    randomnum = random.randrange(20)+1
    print randomnum

#main
playagain = "y"
while playagain == "y":
    
    numnum = input("How many random numbers do you want? ")

    if numnum > 20:
        print "Please enter a number less than 20!"
        
    else:
        for numnum in range(numnum, 0 , -1):
            randomnumber()

    playagain = raw_input("Do you want to go again? y for yes or anything else to quit! ")
    
print "Buh Bye!"
    
