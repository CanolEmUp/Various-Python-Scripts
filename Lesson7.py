import random
playagain = "y"
randnum = range(1,6)

while playagain == "y" :
    num = 1
    for num in range(1, 0 ,-1):
        random.shuffle(randnum)
        print randnum

    playagain = raw_input("Do you want to go again? y for yes or anything else to quit!")
print "Buh Bye!"
    
