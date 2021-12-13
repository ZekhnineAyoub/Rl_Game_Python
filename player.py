import pygame
pygame.init()



#Création de notre joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health= 100
        self.velocity = 1
        self.image = pygame.image.load('assets/Heroo.png')
        self.rect = self.image.get_rect()
        self.rect.y= 140
        self.rect.x= 400

    def move_right(self):
        self.rect.x +=self.velocity

    def move_lef(self):
        self.rect.x-=self.velocity