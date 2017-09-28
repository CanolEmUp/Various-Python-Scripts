#functions which return values

def function1():
    print "You have activated Function 1! It does not return a value"

def function2():
    print "You have activated Funtion 2! It returns a value"
    x=5
    return x

#main

a=1

while True:
    choice=input("Which function would you like to activate? Enter 1 or 2. Entering 0 will exit:")
    if choice==1:
        function1()
    elif choice==2:
        value2=function2()
        print "The value it returns is", value2
    elif choice==0:
        break
    else:
        print "You have tp enter a number between 1 or 2! Or 0 to exit!"

raw_input("\n\nPress the enter key to exit.")


def randomnumber():
    print randrange(20)
    
#main

a=1

while True:
    choice=input("How many random numbers do you want?")
    if choice >=1:
        randomnumber() * choice
    elif choice >=20:
        print "That is too many numbers! choose less than 20 random numbers"
    else:
        print "
    



