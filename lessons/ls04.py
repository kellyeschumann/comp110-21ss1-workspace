"""Check if a random number is even or odd."""

from random import randint

some_int: int = randint(0, 20)
b: bool = some_int % 2 == 0

if b:
    print("Even!")
else:
    print("Odd!")