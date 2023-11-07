# Init main
import pygame
from screen import *

button_width = 200
button_heigth = 50
button_comenzar = pygame.Rect(0, 0, button_width, button_heigth)
button_comenzar.center = init_screen
# Options main
button_options = pygame.Rect(0, 0, button_width, button_heigth)
button_options.center = option_screen
# Quit main
button_quit = pygame.Rect(0, 0, button_width, button_heigth)
button_quit.center = quit_screen
# Back Option
button_back = pygame.Rect(0, 0, button_width, button_heigth)
button_back.center = init_screen

# Botones
boton_comenzar = pygame.Rect(centro_x - button_width // 2, 300, 200, 50)
boton_options = pygame.Rect(centro_x - button_width // 2, 400, 200, 50)
boton_quit = pygame.Rect(centro_x - button_width // 2, 500, 200, 50)
boton_back = pygame.Rect(centro_x - button_width // 2, 400, 200, 50)


