playagain = "y"

while playagain == "y" :
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

    playagain = raw_input("Want to go again? y to go again or anything else to quit! ")

print "Buh Bye!"
        
