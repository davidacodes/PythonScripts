import time
import random

# game function
keep_playing = True

while keep_playing:

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the cavern of secrets!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)

    print("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    ch1 = str(input("Do you take it? [y/n]: \n"))

    # Stick taken
    if ch1.lower() == 'y':
        print("You have taken the stick!")
        time.sleep(2)
        stick = 1

    # Stick Not taken
    else:
        print("You did not take the stick")
        stick = 0

    print("As you proceed further into the cave, you see a small glowing object")
    ch2 = str(input("Do you approach the object [y/n]"))

    # Approach Spider
    if ch2.lower() == 'y':
        print("You approach the object...")
        time.sleep(2)
        print("As you draw closer, you begin to make out the object as an eye!")
        time.sleep(1)
        print("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it [y/n]"))

        # Fight Spider
        if ch3.lower() == 'y':

            # With Stick
            if stick == 1:
                print("You only have a stick to fight with!")
                print("You quickly jab the spider in it's eye and gain an advantage")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                    Fighting..                  ")
                print("    You must hit above a 5 to kill the spider   ")
                print("If the spider hits higher than you, you will die")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(3, 10))
                edmg1 = int(random.randint(1, 5))
                print("you hit a", fdmg1)
                print("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print("The spider has dealt more than you!")
                    complete = 0

                elif fdmg1 < 5:
                    print("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1

                else:
                    print("You killed the spider")
                    complete = 1

            # Without Stick
            else:
                print("You don't have anything to fight with!")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                    Fighting..                  ")
                print("   You must hit above a 5 to kill the spider    ")
                print("If the spider hits higher than you, you will die")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg2 = int(random.randint(1, 8))
                edmg2 = int(random.randint(1, 5))
                print("you hit a", fdmg2)
                print("the spider hits a", edmg2)
                time.sleep(2)

                if edmg2 > fdmg2:
                    print("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1

                else:
                    print("You killed the spider!")
                    complete = 1

        # Don't Fight Spider
        else:
            print("You choose not to fight the spider.")
            time.sleep(1)
            print("As you turn away, it ambushes you and impales you with it's fangs!!!")
            complete = 0

    # Don't Approach Spider
    else:
        print("You turn away from the glowing object, and attempt to leave the cave...")
        time.sleep(1)
        print("But you feel like there is more to this cave....")
        time.sleep(2)
        complete = 1

    # Display Alive with complete var == 1, dead if anything else
    # Play again, if 'n' is selected turn keep_playing var to False stopping the game while loop
    if complete == 1:
        alive = input('You managed to escape the cavern alive! Would you like to play again? [y/n]: ')
        if alive.lower() == 'y':
            continue
        else:
            keep_playing = False

    else:
        alive = input('You have died! Would you like to play again? [y/n]: ')
        if alive.lower() == 'y':
            continue
        else:
            keep_playing = False





