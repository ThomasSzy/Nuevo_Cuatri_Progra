import pygame
import sys

pygame.init()  # --> Conectamos Pygame


screen = pygame.display.set_mode((800, 600))


screen.fill((0, 0, 0))  # --> Red , Green, Blue


while True:
    for event in pygame.event.get():  # -->Nos muestra los eventos que se realicen
        if event.type == pygame.QUIT:
            pygame.quit()  # -->Desconectamos pygame
            sys.exit()  # --> Cerramos programa

    pygame.display.flip()
