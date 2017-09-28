#if program

counter = 0
n1 = input("Enter your first number: ")

while counter == 0:
   n2 = input("Enter another number that is higher than the first number: ")
   if n2 < n1:
      print "That number is not higher, try again!"
   elif n2 == n1:
      print "That number is the SAME number!  Do one different!"
   else:
      counter = 1

print "Yay the number is higher!"
