"""Choose your own adventure."""

from random import randint

__author__ = "730314660"


points: int = 1
high_score: int = 0
player: str 


def greet() -> None:
    """Greets the player and welcomes them to the game."""
    player = input("What is your name? ")
    print("Hello " + player + "! Welcome to the coinflip guessing game!")
    print("In this game, you will choose either heads or tails and see how many")
    print("in a row you can guess correctly.")
    print("Good luck, and have fun!")


def game() -> int:
    """Plays the heads and tails game."""
    global points, high_score
    quit: bool = False
    while not quit:
        response: str = input("Heads or tails? Press 1 for Heads, 2 for Tails, or 3 if you want to quit. ")
        if response == "3":
            quit = True
            print("GAME OVER!")
        elif response == "1" or response == "2":
            number: int = randint(1, 2)
            if number == 1 and response == "1":
                print("Correct! :)")
                points += 1
            elif number == 2 and response == "2":
                print("Correct! :)")
                points += 1
            else:
                print("Incorrect :( GAME OVER!")
                print("You scored " + str(points) + " points!")
                print("High Score = " + str(high_score))
                if points > high_score:
                    high_score = points
                points = 0


def main() -> None:
    """Entrypoint of the game."""
    greet()
    game()
    

if __name__ == "__main__":
    main()