import pygame


# Screen
width = 600
height = 800
size_screen = (width, height)
donas = (100, 100)
origin = (0, 0)
screen = pygame.display.set_mode((size_screen))
center_screen = (width // 2, height // 2)  # // -> Devuelve un valor entero


init_screen = (width // 2, height - 200)
option_screen = (width - 500, height - 200)
quit_screen = (width - 100, height - 200)

# Tamaño The simpsons
screen_the_simpson = (400, 300)


# Botons
centro_x = screen.get_width() // 2
