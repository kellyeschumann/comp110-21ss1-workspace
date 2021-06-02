"""A while loop demo."""

iterations: int = int(input("Loop how many times? "))

i: int = 0
while i < iterations:
    print("In repeat block!")
    print("i is " + str(i))
    i += 1

print("After repeat block")
print("i's final value is :" + str(i))