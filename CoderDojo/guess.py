import random

print("Hello!")
def guess():
    a = random.randint(1, 9)
    b = input("Please input a whole number between 1 and 9 or Exit:")
    while b in ("exit", "Exit"):
        print("Bye, Bye")
        break
    try:
        b == int(b)
    except ValueError:
        print("Not an integer!")

guess()