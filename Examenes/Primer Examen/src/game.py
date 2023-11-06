from config import *
from sys import *
from pygame import *
from sound import *

# ----------Inicializamos modulos de pygame----------#
pygame.init()

# ----------Titulo----------#
pygame.display.set_caption("The Simpsons")
# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))
screen.fill((custom))  # --> Red , Green, Blue

main_menu()
pygame.display.flip()

pygame.quit()
