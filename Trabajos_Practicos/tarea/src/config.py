from main import pygame

# Pantalla
width = 800
height = 600
size_screen = (width, height)

# EVENTOS
EVENT_FIGURAS = pygame.USEREVENT + 1


# figuras
def crear_bloque(
    left=0,
    top=0,
    ancho=40,
    alto=40,
    color=(255, 255, 255),
    dir=3,
    borde=0,
    radio=-1,
    speed_x=5,
    speed_y=5,
):
    rec = pygame.Rect(left, top, ancho, alto)
    return {
        "rect": rec,
        "color": color,
        "dir": dir,
        "borde": borde,
        "radio": radio,
        "speed_x": speed_x,
        "speed_y": speed_y,
    }


rectangulo = crear_bloque(100, 50)


# reloj
FPS = 60


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
custom = (255, 174, 174)
gold = (255, 215, 0)
