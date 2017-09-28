import random
dollars = 50
playagain = "y"
winningnumber = 0
numbers = 0

while playagain == "y" :
    print "You have $", dollars
    tickets = input("How many tickets do you want to buy for $1 each? ")
    if tickets > dollars :
        print "You can't afford that much tickets!"
    dollars = dollars - tickets
    winningnumber = random.randrange(100)+1
    if tickets < dollars:
        print "Your numbers are: "
        for tickets in range(tickets, 0, -1):
            numbers = random.randrange(100)+1
            print numbers
            dollars = dollars - tickets
        if numbers == winningnumber :
            print "You won $100!"
            dollars = dollars + 100
    playagain = raw_input("Do you want to go agian? y for yes or anything else to quit! ")
    if dollars == 0 :
        print "Sorry you have no more money!"
        playagain = "n"
    
print "Buh Bye!"
        
        
