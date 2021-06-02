"""An exercise in remainders and boolean logic."""

__author__ = "730314660"

num: str = input("Enter an int: ")
number = int(num)

if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 2 == 0:
        print("TAR")
    else:
        if number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")