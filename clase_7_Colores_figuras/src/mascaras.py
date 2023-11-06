import pygame
from pygame import *
from config_colores import *

pygame.init()  # --> Conectamos Pygame

# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))
# ----------Titulo----------#
pygame.display.set_caption("Menu")
# Creo un reloj
clock = pygame.time.Clock()

# Mascaras
player = pygame.transform.scale(image.load("./src/imagenes/ovni.png"), (200, 200))
rect_player = player.get_rect()
mask_player = pygame.mask.from_surface(player)


asteroid = pygame.transform.scale(image.load("./src/imagenes/asteroid.png"), (200, 200))
rect_asteroid = asteroid.get_rect()
rect_asteroid.center = center_screen
mask_asteroid = pygame.mask.from_surface(asteroid)


running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == MOUSEMOTION:
            rect_player.center = e.pos

    offset = (rect_asteroid.x - rect_player.x , rect_asteroid.y - rect_player.y)
    if mask_player.overlap(mask_asteroid, offset) != None:
        print("Chocaron")

    




    screen.fill(black)
    screen.blit(asteroid, rect_asteroid)
    screen.blit(player, rect_player)

    pygame.display.flip()
pygame.quit()
exit()
