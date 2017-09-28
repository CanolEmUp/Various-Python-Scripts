countupto = input("How high do you want the first number to count up to? ")
countdown = input("How high do you want the second number to count down from? ")
countup = 0
countdownto = countdown
for countup in range(0, countupto, +1) :
    countdown = countdownto
    for countdown in range(countdown, 0, -1) :
        print countup, countdown

        
