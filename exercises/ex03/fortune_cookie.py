"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730314660"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")

some_int: int = randint(1, 4)

if some_int == 1:
    print("Soon, you will acquire many riches.")
else:
    if some_int == 2:
        print("You will meet someone next week who will change your life.")
    else:
        if some_int == 3:
            print("You have already met the love of your life.")
        else:
            if some_int == 4:
                print("A difficult journey leads to a happy ending.")

print("Now, go spread positive vibes!")