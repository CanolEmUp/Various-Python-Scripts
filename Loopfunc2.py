import random
def course():
    print "Please enter your courses:"
    course1 = raw_input("Course 1: ")
    course2 = raw_input("Course 2: ")
    course3 = raw_input("Course 3: ")
    course4 = raw_input("Course 4: ")
    print "I predict your grades this term will be:"
    print course1,":", random.randrange(100)+1, "%"
    print course2,":", random.randrange(100)+1, "%"
    print course3,":", random.randrange(100)+1, "%"
    print course4,":", random.randrange(100)+1, "%"

# main
course()
