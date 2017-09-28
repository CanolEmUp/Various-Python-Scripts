def room1():
    print "You are in room 1!"
    direction = input("Where do you want to go? Enter 1 for west, 2 for east: ")
    if direction == 1:
        print "You cannot go further west!"
        return room1()
    elif direction == 2:
        return room2()
def room2():
    print "You are in room 2!"
    direction = input("Where do you want to go? Enter 1 for west, 2 for east: ")
    if direction == 1:
        return room1()
    elif direction == 2:
        return room3()
def room3():
    print "You are in room 3!"
    direction = input("Where do you want to go? Enter 1 for west, 2 for east: ")
    if direction == 1:
        return room2()
    elif direction == 2:
        print "You cannot go further east!"
        return room3()

# main
room2()
