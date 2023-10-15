import pygame
from pygame import *
from sys import *
from config_colores import *
from random import randint
from random import randrange




def detectar_colision(rect_1, rect_2):

    if punto_en_rectangulo(rect_1.topleft, rect_2) or \
        punto_en_rectangulo(rect_1.topright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or\
        punto_en_rectangulo(rect_2.topleft, rect_1) or \
        punto_en_rectangulo(rect_2.topright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1):
            return True
    else:
        return False


#Punto dentro de un rectanguulo


def punto_en_rectangulo(punto, rect):
    x = punto[0]
    y = punto[1]
    if x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom:
        return True
    else:
        return False


# r1 = pygame.Rect(30, 40, 100, 50)
# r2   = pygame.Rect(30, 40, 100, 50)
p1 = (80, 65)
p2 = (30, 90)

# print(detectar_colision(r1,r2))
# --> Funcion para diccionario
def crear_bloque(left = 0, top= 0, ancho= 40, alto= 40, color = (255, 255, 255),dir = 3, borde = 0, radio = -1, speed_x = 5, speed_y = 5):
    rec = pygame.Rect(left, top, ancho, alto)
    return {"rect":rec ,"color": color ,"dir": dir , "borde": borde , "radio": radio, "speed_x": speed_x, "speed_y": speed_y}









# Iniciamos Pygame
# mostramos pantallas
# Colores
# Hacemos dos manera de iniciar programa
# Colocamos un titulo a la pantalla

# ----------Inicializamos modulos de pygame----------#

pygame.init()  # --> Conectamos Pygame

clock = pygame.time.Clock()


# ----------Titulo----------#
pygame.display.set_caption("Primer Juego")

# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))

# ----------Colores----------#
screen.fill((custom))  # --> Red , Green, Blue

# ------------Manera 1-------------#
# Inicializamos modulos de pygame
is_ranning = True

# Rectangulo
# is_running = True

# rect_1 = pygame.Rect(0, 0, 200, 100)  # objeto rectangulo

# rect_2 = (200, 200, 300, 150)  # instrucciones para dibujar un rectangulo
#   (x,y)->Ubicacion (300,150) ->Tamaño (Ancho \ Largo)

# IMPORTANTE PARA QUE REBOTE
# Como hacer que rebote
# bajando = True
# costado = True

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
# Bloque

bloques = []

for i in range(2):
    bloques.append(crear_bloque(left = randint(0, width - block_width),
                                top = randint(0, height - block_height),
                                ancho = randint(0,block_width),
                                alto = randint(0,block_height),
                                color = color_aleatoreo()
                                ))

# bloques = [
#     {
#         "rect": pygame.Rect(randint(0, width - block_width),randint(0, height - block_height),block_width,block_height,
#         ),
#         "color": color_random(color_aleatoreo()),
#         "dir": DL, "borde": 0, "radio": -1
#     },
#     {
#         "rect": pygame.Rect(
#             randint(0, width - block_width),
#             randint(0, height - block_height),
#             block_width,
#             block_height,
#         ),
#         "color": color_random(color_aleatoreo()),
#         "dir": UR, "borde": 0, "radio": -1
#     },
#     {
#         "rect": pygame.Rect(
#             randint(0, width - block_width),
#             randint(0, height - block_height),
#             block_width,
#             block_height,
#         ),
#         "color": color_random(color_aleatoreo()),
#         "dir": UL, "borde": 0, "radio": -1
#     },
# ]

while is_ranning:
    # ----> Tiempo
    clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG
    # ----> Detecta los elementos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_ranning = False

    # ----> ACTUALIZA ELEMENTOS

    # Controlo rebote y cambio de direccion
    # rebote derecha pantalla
    for block in bloques:
        if block["rect"].right >= width:
            if block["dir"] == DR:
                block["dir"] = DL
                block["color"] = color_aleatoreo()
            elif block["dir"] == UR:
                block["dir"] = UL
                # block["color"] = color_aleatoreo()
                block["borde"] = randrange(20)

                block["speed_x"] = randint(1,10)
        # rebote izquierda pantalla
        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
                # block["color"] = color_aleatoreo()
            elif block["dir"] == UL:
                block["dir"] = UR
                # block["color"] = color_aleatoreo()
                block["radio"] = randrange(25) # -> Circulo

                block["speed_x"] = randint(1,10)
        # rebote abajo pantalla
        elif block["rect"].bottom >= height:
            if block["dir"] == DR:
                block["dir"] = UR
                # block["color"] = color_aleatoreo()
                block["speed_y"] = randint(1,10)
            elif block["dir"] == DL:
                block["dir"] = UL

                # block["color"] = color_aleatoreo()
        # rebote arriba pantalla
        elif block["rect"].top <= 0:
            if block["dir"] == UL:
                block["dir"] = DL
                # block["color"] = color_aleatoreo()
            elif block["dir"] == UR:
                block["dir"] = DR
                # block["color"] = color_aleatoreo()

                block["speed_y"] = randint(1,10)



    if detectar_colision(bloques[0]["rect"], bloques[1]["rect"]): # los bloques vienen de donde creamo los rectangu
        print("COLISIONNNN!!!")
        for bloque in bloques:
            bloque["color"] = color_aleatoreo()
    # Muevo el rectangulo segun la direccion
    for block in bloques:
        if block["dir"] == DR:
            block["rect"].top += speed_y
            block["rect"].left += speed_x

        elif block["dir"] == DL:
            block["rect"].left -= speed_y
            block["rect"].top += speed_x

        elif block["dir"] == UL:
            block["rect"].left -= speed_y
            block["rect"].top -= speed_x

        elif block["dir"] == UR:
            block["rect"].left += speed_y
            block["rect"].top -= speed_x

    # ----> Dibujar Pantalla
    screen.fill(black)
    for block in bloques:
        pygame.draw.rect(screen, block["color"], block["rect"], block["borde"],block["radio"])

    # ----> Actualiza la pantalla
    pygame.display.flip()

    # ----------Como hacer que baje y vuelva de arriba Infinitamente----------#
    # pos_y += 1 -->Lo que hace esto es que y vaya bajando
    # if pos_y == height:
    #     pos_y = -alto

    # ----------Como hacer que apolle en la parte inferior----------#

    # if pos_y < height - alto:
    #     pos_y +=1 #-->Lo que hace esto es que y vaya bajando

    # ----------Como hacer que suba----------#

    # if pos_y > 0:
    #     pos_y -= SPEED

    # ----------Como hacer que baje y suba----------#

    # if bajando:
    #     if pos_y < height - alto:
    #         pos_y += SPEED
    #     else:
    #         bajando = False
    # else:
    #     if pos_y > 0:
    #         pos_y -= SPEED
    #     else:
    #         bajando = True

    # ----------Como hacer que vaya de costado a costado----------#

    # if costado:
    #     if pos_x < width - ancho:
    #         pos_x += SPEED
    #     else:
    #         costado = False
    # else:
    #     if pos_x > 0:
    #         pos_x -= SPEED
    #     else:
    #         costado = True
    # ----------Colores----------#
    # screen.fill((custom))  # --> Red , Green, Blue

    # pygame.draw.rect(screen, green, rect_1)
    # y = pygame.draw.rect(screen, yellow, rect_2)

    # z = draw.rect(screen, red, (300, pos_y, ancho, alto), 5)

    # Rectangulo
    # z = draw.rect(screen, red, (pos_x, pos_y, ancho, alto), 5)

    # ----------FIGURAS----------#

    # ----------CIRCULO----------#
    # draw.circle(screen, blue, center_screen, 100, 5, False,False,False,True)
    # Tengo que escribir todos los anteriores

    # draw.circle(screen, blue, (width - radio, radio), radio, 5)

    # O le agrego el draw_bottom_left o el que quuiera elegir

    # ----------LINEA----------#
    # draw.line(screen, blue, (0, 0), (width, height), 5)

    # ----------PORTAL----------#
    # draw.ellipse(screen, black, (200, 300, 50, 100))

    # ----------TRIANGULO----------#
    # r_poligono = draw.polygon(screen, white, [(500, 150), (700, 50), (750, 350)])

    # draw.polygon(screen, white, [(500, 150), (700, 50), (750, 350)])

    # draw.rect(screen, yellow, r_poligono, 4)

    # --------------------
    # pygame.draw.rect(Donde?, Color, Rectangulo, [Borde, borde redondeado,])

    # ------------Muestra Colores------------#


pygame.quit()


# ------------Manera 2------------#
# while True:
#     for event in pygame.event.get():  # -->Nos muestra los eventos que se realicen
#         if event.type == pygame.QUIT:
#             pygame.quit()  # -->Desconectamos pygame
#             sys.exit()  # --> Cerramos programa

#     pygame.display.flip()
