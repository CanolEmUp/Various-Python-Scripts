import random
def randquestion():
    num1 = random.randrange(10)+1
    num2 = random.randrange(10)+1
    print "What is ", num1, "+", num2, "?",
    answer = input("")
    if answer == num1 + num2:
        print "Correct!"
    else:
        print "Wrong!"

# main
loop = 1
while loop == 1:
    randquestion()
