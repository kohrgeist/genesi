#import futureGameLoopEventsFile
import time
from src.controllers.eventsController import randomEvent

class GameLoop:
    def __init__(self, isOn, player):
        self.isOn = isOn
        self.player = player        

    # method to start a loop and check if the player wants to keep playing.
    def startLoop(self):
        
        while self.isOn == True:

            print("Game on!")
            time.sleep(1)
            keepOn = int(input("\nGame continues?\n1 for 'NO' and 2 for 'YES'\nAnswer: "))

            if keepOn == 1:
                print("Game ended...")
                break

            elif keepOn != 2:
                print("Game ended for invalid option...")
                break

            else: 
                randomEvent(self.player)
                time.sleep(0.2)