"""Relative reassignment."""
a: int = 3
b: str = "<"
iterations: int = 0

while iterations < 100:
    b += str(a)
    print(b)
    iterations += 1

print("loop done!")