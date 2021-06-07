"""for in loop practice."""

s: str = "Kaki Ryan"
i: int = 0
while i < len(s):
    print(s[i])
    i += 1

for char in s:
    print(char)


def sum_two_lists(xs: list[int], ys: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(len(xs)):
        result.append(xs[i] + ys[i])
    return result 

