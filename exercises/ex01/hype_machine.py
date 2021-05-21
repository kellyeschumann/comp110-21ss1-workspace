"""When given a name, this hype machine sends you messages to motivate you"""

__author__: str = "730314660"

name: str = input("What is your name? ")
print("You entered: ")
print(name)

hypeMessageOne = "You are so smart "
y = "!"
print(hypeMessageOne + name + y)

hypeMessageTwo = "You can do this "
hypeMessageThree = " I know you can!"
print(hypeMessageTwo + name  + hypeMessageThree)

hypeMessageFour = " have a great night!"
print(name + hypeMessageFour)


