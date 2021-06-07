"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730314660"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Outputs a fortune that corresponds with a specific integer."""
    rand = randint(1, 4)
    if rand == 1:
        return "Soon, you will acquire many riches."
    if rand == 2:
        return "You will meet someone next week who will change your life."
    if rand == 3:
        return "You have already met the love of your life."
    else:
        return "A difficult journey leads to a happy ending."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()