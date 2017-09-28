countupto = input("How high do you want the first number to count up to? ")
countdown = input("How high do you want the second number to count down from? ")
countup = 0
countdownto = countdown

while countup < countupto :
    countup = countup + 1
    countdown = countdownto
    while countdown > 0 :
        print countup, countdown
        countdown = countdown - 1

        

