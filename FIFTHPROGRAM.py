#happy or not happy?

x = 0

while x==0:
   print "You are cool!\n"
   answer = raw_input("Should I say that again? Enter 'y' or 'n': ")

   if "y" in answer:
      print "Ok! I'll say it again!"
   else:
      print "Ok, you are not cool any ways."
      x=1

raw_input("\n\nPress Enter to exit!")
