"""A function to abbreviate strings."""




def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Prompt the user for text....
    # .. and make use of abbreviate function and print it.
    phrase: str = str(input("Write some text with some uppercase letters: "))
    ans: str = abbreviate(phrase)
    print("The abbreviation is \"" + ans + "\".")
    

# TODO 1: Define the abbreviate function, and its logic, here.
def abbreviate(phrase: str) -> str:
    """Gives abbreviation of word inputted by user according to it's uppercase letters."""
    length: int = len(phrase)
    answer: str = ""
    index: int = 0
    while index < length:
        current: str = str(phrase[index])
        if current.isupper():
            answer = answer + current
        index += 1
    return answer
    

if __name__ == "__main__":
    main()