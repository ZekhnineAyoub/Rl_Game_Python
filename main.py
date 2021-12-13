import pygame
pygame.init()
from game import Game


#Generation de la fenetre
pygame.display.set_caption("Subway Surfer")
screen = pygame.display.set_mode((980, 630))

# importation img backgroud
background = pygame.image.load('assets/bg.jpg')

#Charger le game
game = Game()


running = True
while running:

    screen.blit(background, (0, 0))
    #appliquer l'image de joueur
    screen.blit(game.player.image,game.player.rect)

    ###
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x+game.player.rect.width<screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_lef()

    # mettre à jour l'ecran
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture")

        elif event.type==pygame.KEYDOWN:
            game.pressed[event.key]= True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key]= False



