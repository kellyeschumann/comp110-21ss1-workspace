"""An exercise with functions and lists."""

__author__ = "730314660"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Test your functions here
    input("Type in a positive integer greater than 1: ")
    return
    

# TODO 1: Define the is_prime function, and its logic, here.
def is_prime(number: int) -> bool:
    """Tells user if a number inputted is prime or not."""
    if number <= 1:
        return False
    integer: int = 2
    while integer < number:
        if number % integer == 0:
            return False
        integer += 1
    return True


# TODO 2: Define the list_primes function, and its logic, here.
def list_primes(lower: int, upper: int) -> list[int]:
    """Determines if numbers in a list are prime."""
    counter: int = lower
    result: list[int] = []
    while counter < upper:
        if is_prime(counter):
            result.append(counter)
        counter += 1
    return result


if __name__ == "__main__":
    main()