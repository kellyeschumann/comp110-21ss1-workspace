"""This takes two numbers input from user and completes four mathematical equations."""


__author__: str = "730314660"

left = "Left-hand side"
right = "Right-hand side"

numberOne: str = input("What is the first number? ")
print("You entered: ")
print(numberOne)

numberTwo: str = input("What is the second number? ")
print("You entered: ")
print(numberTwo)

print(left + ": " + numberOne)
print(right + ": " + numberTwo)

integerOne = int(numberOne)
integerTwo = int(numberTwo)

resultOne = integerOne ** integerTwo
resultTwo = integerOne / integerTwo
resultThree = integerOne // integerTwo
resultFour = integerOne % integerTwo

print(numberOne + " ** " + numberTwo + " is " + str(resultOne))
print(numberOne + " / " + numberTwo + " is " + str(resultTwo))
print(numberOne + " // " + numberTwo + " is " + str(resultThree))
print(numberOne + " % " + numberTwo + " is " + str(resultFour))