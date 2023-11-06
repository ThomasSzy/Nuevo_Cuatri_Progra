import pygame
from pygame.locals import *
from config import *

# ----------Inicializamos modulos de pygame----------#
pygame.init()

# ----------Titulo----------#
pygame.display.set_caption("Calculadora de formas")

# ----------Pantalla----------#
screen = pygame.display.set_mode((size_screen))

# ----------Reloj----------#
clock = pygame.time.Clock()

# ----------Iniciamos----------#

is_raning = True

while is_raning:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_raning = False

        if event.type == EVENT_FIGURAS:
            
screen.fill(black)



pygame.quit()