
#
# For Loops
#

# First example we are just going just print out all the products for
# one number that we take in has an input. The input is going to be
# a string so we will need to use int() function to change it to a
# int so we can multiply it. The f in the print statement is called
# a formatted string literal, f-string for short. It is available in
# Python version 3.6

def productsNum():
    num = int(input("Enter a number: "))
    for i in range(0, 10):
        print(f"{num} * {i} = {num * i}")

# timesLine()

# That's not too bad. But we need a full multiplication table. So let's
# remove the input and multiply our iterable against it.

def timeTable():
    for i in range(1, 10):
        print(f"{i} {i * 2} {i * 3} {i * 4} {i * 5} {i * 6} {i * 7} {i * 8} {i * 9} {i * 10}")

# timeTable()

# That worked perfect, but it's big. Could we do to make it shorter?
# It looks like we need to use another loop to iterate over all the
# numbers that we are multiplying. We can nest a loop inside our other loop.

def timesTable():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i * j}")

# timesTable()


# That worked, but it didn't print out the way we wanted. Each time
# the print statement is run a new line is added to the end by default.
# We can change this behavior by adding , end=" "  with this we are
# replacing the new line with a space. But then we need to add a print
# statement at our 1st nested level to get the line change when we start
# on a new number.

def betterTimesTable():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i * j}", end=" ")
        print("")

# betterTimesTable()

