"""Simple guessing game."""

print("Guess a number!")

guess: int = int(input("Guess: "))

if guess == 8:
    print("correct")
else:
    print("No, try again")

print("Game over")