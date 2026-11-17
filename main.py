# create a terminal loop that has 6 options to choose from

from src.config.gameLoop import GameLoop
from src.models.player import Player

player = Player("Evan")

gameLoop = GameLoop(True, player)
gameLoop.startLoop()
