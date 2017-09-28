playagain = "y"

while (playagain == "y") or (playagain == "Y"):
    
    marks = 0
    if input("What is 12 * 12?: ") == 144 :
        marks = marks + 1
    if raw_input("What is the biggest country in the world by size?: ") == "Russia" :
        marks = marks + 1
    if input("What is 35 - 15?: ") == 20 :
        marks = marks + 1
    if raw_input("What is the most biggest country in the world by population?: ") == "China" :
        marks = marks + 1 
    if input("What is the square root of 9?: ") == 3 :
        marks = marks + 1

    print "You got ", marks, " out of 5!"
    print "You got ", marks * 100 / 5,"%!"
    
    playagain = raw_input("Do you want to go again? y for Yes, any other button for No ")
    

print "Buh Bye!"
