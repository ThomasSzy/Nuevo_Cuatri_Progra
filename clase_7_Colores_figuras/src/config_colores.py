# Pantalla
width = 800
height = 600
size_screen = (width, height)


center_screen = (width // 2, height // 2)  # // -> Devuelve un valor entero

# Tiempo
FPS = 60

SPEED = 5


# Medidas
radio = 100
alto = 100
ancho = 200

# Posiciones
pos_x = 0
pos_y = 0
















def color_random(lista_colores):
    from random import randrange

    return lista_colores[randrange(len(lista_colores))]


# Colors
def color_aleatoreo():
    from random import randrange

    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r, g, b)


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
custom = (255, 174, 174)
