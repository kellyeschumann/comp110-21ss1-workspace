"""A program to determine names over 21."""

__author__ = "730314660"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your function here
    print(over_21({"Kris": 2001, "Kaki": 1998, "Marlee": 1994}))
    

# TODO 1: Define the over_21 function, and its logic, here.
def over_21(students: dict[str, int]) -> list[str]:
    """Given student info, who is 21 or older?"""
    result: list[str] = []
    for student in students:
        if students[student] <= 2000:
            result.append(student)
    return result 


if __name__ == "__main__":
    main()