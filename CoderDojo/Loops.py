
# for loop complete a series of actions once for every item in that list.
#     So before the for loop starts we know how many it will run. No matter
#     how many times the loop runs it will complete the same number of actions
#     every time.

# for i in range(1, 10):
#     print("Hello" + str(i))
#     print(i)

backpack = ["sword", "bread", "armor", "funny hat", "shield"]

for item in backpack:
    print(item)



# while loop run and run and continue running as it checks a condition to
#   determine if it should keep running.

# import random
# catIsAwake = True
#
# while catIsAwake:
#     print("Meow Meow")
#
#     if random.randrange(0, 100) == 0:
#         catIsAwake = False


import random

goblinHealth = 1000

while goblinHealth > 0:
    print("Attack Goblin!")
    attackDamge = random.randrange(25, 50)
    print("You attacked for " + str(attackDamge))
    goblinHealth = goblinHealth - attackDamge



