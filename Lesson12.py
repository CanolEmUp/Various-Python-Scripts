mainorderchoice = ""
sideorderchoice = ""
playagain = "y"

def Restaurant1():
    if Restaurant == "Mcdonalds" :
        mainorder = raw_input("What main meal do you want at Mcdonalds? \n Big Mac \n Quarter Pounder \n Chicken Mcnuggets \n")
        if mainorder == "Big Mac":
            mainorderchoice = "Big Mac"
        elif mainorder == "Quarter Pounder":
            mainorderchoice = "Quarter Pounder"
        elif mainorder == "Chicken Mcnuggets":
            mainorderchoice = "Chicken Mcnuggets"
        sideorder = raw_input("What Mcdonalds side do you want with that? \n Fries \n Apple Pie \n Cookie \n")
        if sideorder == "Fries":
            sideorderchoice = "Fries"
        elif sideorder == "Apple Pie":
            sideorderchoice = "Apple Pie"
        elif sideorder == "Cookie":
            sideorderchoice = "Cookie"
        print "At McDonalds, you have ordered: ", mainorderchoice, "and", sideorderchoice

def Restaurant2():
    if Restaurant == "KFC" :
        mainorder = raw_input("What main meal do you want at KFC? \n Fried Chicken \n Chicken Burger \n Chicken Wrap \n")
        if mainorder == "Fried Chicken":
            mainorderchoice = "Fried Chicken"
        elif mainorder == "Chicken Burger":
            mainorderchoice = "Chicken Burger"
        elif mainorder == "Chicken Wrap":
            mainorderchoice = "Chicken Wrap"
        sideorder = raw_input("What KFC side do you want with that? \n Fries \n Apple Pie \n Cookie \n")
        if sideorder == "Fries":
            sideorderchoice = "Fries"
        elif sideorder == "Salad":
            sideorderchoice = "Salad"
        elif sideorder == "Brownie":
            sideorderchoice = "Brownie"
        print "At KFC, you have ordered: ", mainorderchoice, "and", sideorderchoice

def Restaurant3():
        if Restaurant == "Pizza Pizza" :
            mainorder = raw_input("What main meal do you want at Pizza Pizza? \n Cheese Pizza \n Pepperoni Pizza \n 3 = Veggie Pizza \n")
        if mainorder == "Cheese Pizza":
            mainorderchoice = "Cheese Pizza"
        elif mainorder == "Pepperoni Pizza":
            mainorderchoice = "Pepperoni Pizza"
        elif mainorder == "Veggie Pizza":
            mainorderchoice = "Veggie Pizza"
        sideorder = raw_input("What Pizza Pizza side do you want with that? \n Fries \n Apple Pie \n Cookie \n")
        if sideorder == "Poutine":
            sideorderchoice = "Poutine"
        elif sideorder == "Soda":
            sideorderchoice = "Soda"
        elif sideorder == "Chicken Tenders":
            sideorderchoice = "Chicken Tenders"
        print "At Pizza Pizza, you have ordered: ", mainorderchoice, "and", sideorderchoice

#main

Restaurant = raw_input("What restaurant do you want to go to? \n Mcdonalds \n KFC \n Pizza Pizza \n")

while playagain == "y":

        Restaurant1()

        Restaurant2()

        Restaurant3()


        playagain = raw_input("Do you want to go again? y for yes or anything else to quit!")

print "Buh Bye!"    
