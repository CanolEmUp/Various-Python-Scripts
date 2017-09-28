# Wathaned Ean
import random
def namey():
    global name
    name = raw_input("What is your name? ")
    randomnumber()
def randomnumber():
    global ranum
    ranum = random.randrange(10)+1
def printname():
    for printy in range(ranum, 0, -1):
        print name
def goodbye():
    print "Bye", name
# main
ranum = 0
playagain = "yes"
while playagain != "no":
    namey()
    print "Hi", name
    print "Your random number is", ranum
    printname()
    playagain = raw_input("Do you want to go again? anything to go again or no to quit! ")
if playagain == "no":
    goodbye()
    print "Exiting..."
