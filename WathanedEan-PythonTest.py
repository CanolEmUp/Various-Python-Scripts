# Ned Ean Python Test

import random

playagain = "y"
dollars = 50
winningnumber = 0
numbers = 0
numofwins = 0
numoflosses = 0

while playagain == "y" :

    program = input("What program do you want to activate? \n 1 = Calculator \n 2 = Math Quiz \n 3 = Lottery \n 4 = Build a Computer \n 5 = Random Program \n")

    while program == 5 :
        print "You have chosen a random program!"
        program = random.randrange(3)+1

    while program != 5 :
    
        if program == 1 :
            print "You have chosen: Calculator"
            calculation = input("What option do you want? 1 = add, 2 = subtract, 3 = multiply, 4 = divide: ")
            number1 = input("What is the first number? ")
            number2 = input("What is the second number? ")
            if calculation == 1:
                print number1, "+", number2, "=", number1 + number2
            elif calculation == 2:
                print number1, "-", number2, "=", number1 - number2
            elif calculation == 3:
                print number1, "*", number2, "=", number1 * number2
            elif calculation == 4:
                print number1, "/", number2, "=", number1 / number2
            else :
                print "Please enter a valid option"
            program = input("What program do you want to activate? \n 1 = Calculator \n 2 = Math Quiz \n 3 = Lottery \n 4 = Build a Computer \n 5 = Random Program \n")
                
        elif program == 2 :
            print "You have chosen: Math Quiz"
            marks = 0
            if input("What is 12 * 12?: ") == 144 :
                marks = marks + 1
            if input("What is 100 / 25?: ") == 4 :
                marks = marks + 1
            if input("What is 35 - 15?: ") == 20 :
                marks = marks + 1
            if input("What is 9 to the power of 2?: ") == 81 :
                marks = marks + 1 
            if input("What is the square root of 9?: ") == 3 :
                marks = marks + 1

            print "You got ", marks, " out of 5!"
            print "You got ", marks * 100 / 5,"%!"
            program = input("What program do you want to activate? \n 1 = Calculator \n 2 = Math Quiz \n 3 = Lottery \n 4 = Build a Computer \n 5 = Random Program \n")

        while program == 3 :
            print "You have chosen: Lottery"
            print "You have $", dollars
            tickets = input("How many tickets do you want to buy for $1 each? ")
            if tickets > dollars :
                print "You can't afford that much tickets!"
            winningnumber = random.randrange(100)+1
            if tickets <= dollars:
                dollars = dollars - tickets
                print "Your numbers are: "
                for tickets in range(tickets, 0, -1):
                    numbers = random.randrange(100)+1
                    print numbers
                    numoflosses = numoflosses + 1
                if numbers == winningnumber :
                    print "You won $100!"
                    dollars = dollars + 100
                    numofwins = numofwins + 1
                print "Number of wins: ", numofwins
                print "Number of Losses: ", numoflosses
            program = input("Do you want to go again? 3 for yes or 1 = Calculator \n 2 = Math Quiz \n 4 = Build a Computer \n 5 = Random Program \n ")
                
        while program == 4 :
            print "Let's build your own computer!"
            badparts = 0
            burndown = 0
            cpu = input("What brand of cpu do you want? \n 1 = Intel \n 2 = AMD \n")
            gpu = input("What brand of video card do you want? \n 1 = Nvidia \n 2 = AMD \n")
            space = input("What kind of storage do you want? \n 1 = HDD \n 2 = SSD \n")
            case = input("What kind of case do you want? \n 1 = super fancy big \n 2 = super cheap small \n")
            if cpu == 2 :
                print "Oh noes! Your computer is super hot because you chose an AMD CPU!"
                badparts = badparts + 1
            if cpu == 1:
                print "Nice! The CPU is nice and cool with Intel!"
            if gpu == 2 :
                print "Oh noes! Your computer can grill food because you chose an AMD GPU!"
                badparts = badparts + 1
            if gpu == 1 :
                print "Good choice with Nvidia! Every game looks amazing!"
            if space == 1:
                print "Man, your computer is slow with an HDD..."
                badparts = badparts + 1
            if space == 2:
                print "Man! your computer boots up super fast!"
            if case == 1 :
                print "Your computer looks cooler than a freezer and flows with the wind!"
            if case == 2 :
                print "Your computer is struggling because of the small space and no airflow!"
                badparts = badparts + 1
            while badparts > 0  :
                print "Your computer is having a risk of burning down due to bad parts! \n . \n . \n . \n"
                burndown = random.randrange(10)+1
                if burndown > 5 :
                    print "Your computer burned down!"
                    break
                if burndown < 5 :
                    print "Your computer did not burn down, yet..."
                    break
            if badparts == 0 :
                print "Good choice on all of those computer parts!"
            program = input("Do you want to go again? 4 for yes or \n 1 = Calculator \n 2 = Math Quiz \n 3 = Lottery \n 5 = Random Program \n ")
            

