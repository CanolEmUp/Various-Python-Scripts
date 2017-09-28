import random
def randnumber():
    randnum = range(1,6)
    num = 1
    for num in range(1, 0 ,-1):
        random.shuffle(randnum)
        print randnum
playagain = "y"

while playagain == "y" :
    randnumber()
    playagain = raw_input("Do you want to go again? y for yes or anything else to quit!")
print "Buh Bye!"
