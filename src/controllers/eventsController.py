import random
import time

def randomEvent(player):
    randomEvent = random.randint(1,2)
    time.sleep(0.5)

    if randomEvent == 1:
        print("\nYou have found a lost bee! Grab the bee and return it to his comb!")
        player.addToInventory("Bee",1)

    else: print("fuck it was 2")
        