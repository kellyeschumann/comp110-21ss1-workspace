"""An exercise in computing the factorial of an int."""

__author__ = "730314660"


some_int: int = int(input("Enter a number: "))

number: int = 1
total: int = 1
while number <= some_int:
    if some_int > 0:
        total *= number
        number += 1

total: int = str(total)

print("Factorial: " + total)