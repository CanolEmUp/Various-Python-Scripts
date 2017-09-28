import random

def healthmod():
    global health
    print "You are attacking!"
    health = health - damage
    print "Your health is", health

def dieroll():
    damage = random.randrange(10)+1

# main
health = 20
damage = random.randrange(10)+1

playagain = "y"

while playagain == "y":
    mode = raw_input("Do you want to Attack or Defend? ")
    if mode == "Attack":
        healthmod()
    elif mode == "Defend":
        print "Your health is", health
        print "You are defending!"
    else:
        print "Type Attack or Defend!"
    if health <= 0:
        print "You are dead"
        raw_input("Press anything to quit ")
        exit()
        
