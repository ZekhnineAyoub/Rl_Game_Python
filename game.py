import  pygame
from player import Player

pygame.init()



class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}