"""A program to determine top favorite colors."""

__author__ = "730341660"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your functions here
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


# TODO 1: Define the favorite_color function, and its logic, her
def favorite_color(students: dict[str, str]) -> str:
    """Given favorite colors, which color is the most popular?"""
    result: str
    frequencies: dict[str, int] = {}
    for student in students:
        color: str = students[student]
        if frequencies.get(color) is None:
            frequencies[color] = 1
        else:
            frequencies[color] = frequencies[color] + 1
    highest_frequency: int = 0
    for entry in frequencies:
        if frequencies[entry] > highest_frequency:
            result = entry
            highest_frequency = frequencies[entry]
    return result


if __name__ == "__main__":
    main()