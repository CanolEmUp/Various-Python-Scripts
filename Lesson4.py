Restaurant = raw_input("What restaurant do you want to go to? \n Mcdonalds \n KFC \n Pizza Pizza \n")
mainorderchoice = ""
sideorderchoice = ""
playagain = "y"

while playagain == "y":
    if Restaurant == "Mcdonalds" :
        mainorder = raw_input("What main meal do you want at Mcdonalds? \n Big Mac \n Quarter Pounder \n Chicken Mcnuggets \n")
        if mainorder == "Big Mac":
            mainorderchoice = "Big Mac"
        elif mainorder == "Quarter Pounder":
            mainorderchoice = "Quarter Pounder"
        elif mainorder == "Chicken Mcnuggets":
            mainorderchoice = "Chicken Mcnuggets"
        sideorder = raw_input("What Mcdonalds side do you want with that? \n 1 = Fries \n 2 = Apple Pie \n 3 = Cookie \n")
        if sideorder == "Fries":
            sideorderchoice = "Fries"
        elif sideorder == "Apple Pie":
            sideorderchoice = "Apple Pie"
        elif sideorder == "Cookie":
            sideorderchoice = "Cookie"
        print "At McDonalds, you have ordered: ", mainorderchoice, "and", sideorderchoice


    if Restaurant == "KFC" :
        mainorder = raw_input("What main meal do you want at KFC? \n 1 = Fried Chicken \n 2 = Chicken Burger \n 3 = Chicken Wrap \n")
        if mainorder == "Fried Chicken":
            mainorderchoice = "Fried Chicken"
        elif mainorder == "Chicken Burger":
            mainorderchoice = "Chicken Burger"
        elif mainorder == "Chicken Wrap":
            mainorderchoice = "Chicken Wrap"
        sideorder = raw_input("What KFC side do you want with that? \n 1 = Fries \n 2 = Apple Pie \n 3 = Cookie \n")
        if sideorder == "Fries":
            sideorderchoice = "Fries"
        elif sideorder == "Salad":
            sideorderchoice = "Salad"
        elif sideorder == "Brownie":
            sideorderchoice = "Brownie"
        print "At KFC, you have ordered: ", mainorderchoice, "and", sideorderchoice

    if Restaurant == "Pizza Pizza" :
        mainorder = raw_input("What main meal do you want at Pizza Pizza? \n 1 = Cheese Pizza \n 2 = Pepperoni Pizza \n 3 = Veggie Pizza \n")
        if mainorder == "Cheese Pizza":
            mainorderchoice = "Cheese Pizza"
        elif mainorder == "Pepperoni Pizza":
            mainorderchoice = "Pepperoni Pizza"
        elif mainorder == "Veggie Pizza":
            mainorderchoice = "Veggie Pizza"
        sideorder = raw_input("What Pizza Pizza side do you want with that? \n 1 = Fries \n 2 = Apple Pie \n 3 = Cookie \n")
        if sideorder == "Poutine":
            sideorderchoice = "Poutine"
        elif sideorder == "Soda":
            sideorderchoice = "Soda"
        elif sideorder == "Chicken Tenders":
            sideorderchoice = "Chicken Tenders"
        print "At Pizza Pizza, you have ordered: ", mainorderchoice, "and", sideorderchoice    

    else:
        print "Invalid Answer!"

    playagain = raw_input("Do you want to go again? y for yes or anything else to quit!")

print "Buh Bye!"
