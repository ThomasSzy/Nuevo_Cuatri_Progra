# Pantalla
width = 800
height = 600
size_screen = (width, height)
origin = (0, 0)

center_screen = (width // 2, height // 2)  # // -> Devuelve un valor entero

# Tiempo
FPS = 60


# botones Menu
button_width = 200
button_heigth = 50

# Laser
size_laser = (4, 10)
speed_laser = 6
laser = None

# Vida
lives = 3

speed_min = 1
speed_max = 3
speed = 1
# Direcciones

UR = 9
DR = 3
DL = 1
UL = 7
# Rectangulo
block_width = 50
block_height = 50

speed_x = 5
speed_y = 5


# Positions
pos_x = 0
pos_y = 0


# -----MONEDAS-----#
# Tamaño
size_coin = 30
size_min_coin = 20
size_max_coin = 40


# Contador
contador_monedas = 0
max_contador = 0
cont_grande = 0
count_coins = 25

# -----MONEDA ESPECIAL-----#
size_coin_rainbow = 60


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
gold = (255, 215, 0)


# Trucos
trick_reverse = False
trick_slow = False
