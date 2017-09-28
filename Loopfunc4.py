import random

def randquestion(right, questions):
    num1 = random.randrange(10)+1
    num2 = random.randrange(10)+1
    print "What is ", num1, "+", num2, "?",
    answer = input("")
    if answer == num1 + num2:
        print "Correct!"
        right = right + 1
    else:
        print "Wrong!"
        questions = questions + 1
    print "Your score is", right
    print "Your percentage is ", right * 100 / questions, "%"

# main
right = 0
questions = 1
loop = 1
while loop == 1:
    randquestion(right, questions)
