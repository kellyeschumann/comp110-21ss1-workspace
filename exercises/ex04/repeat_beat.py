"""Repeating a beat in a loop."""

__author__ = "730314660"


from typing import Counter


beat: str = input("What beat do you want to repeat? ")
amount: str = input("How many times do you want to repeat it? ")
amount2 = int(amount)
iterations = amount2

counter: int = 0
total_beats: str = ""

if amount2 <= 0:
    print ("No beat...")
else:
    while counter < iterations - 1:
        total_beats = total_beats + beat + " "
        counter += 1
    print(total_beats + beat)