number1 = input("How many marks will you enter? ")
number2 = number1
marks = 0
while number1 > 0:
    marks = marks + input("Enter a mark: ")
    number1 = number1 - 1
print marks / number2
