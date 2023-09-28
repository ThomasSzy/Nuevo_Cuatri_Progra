import pygame
from pygame import *
from sys import *
from config_colores import *

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
is_running = True

rect_1 = pygame.Rect(0, 0, 200, 100)  # objeto rectangulo

rect_2 = (200, 200, 300, 150)  # instrucciones para dibujar un rectangulo
#   (x,y)->Ubicacion (300,150) ->Tamaño (Ancho \ Largo)
radio = 100

pos_x = 0
pos_y = 0
alto = 100
ancho = 200

# Como hacer que rebote
bajando = True

costado = True

while is_ranning:
    # ----> Tiempo
    clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG

    # ----> Detecta los elementos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_ranning = False

    # ----> Actualiza los elementos

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

    if costado:
        if pos_x < width - ancho:
            pos_x += SPEED
        else:
            costado = False
    else:
        if pos_x > 0:
            pos_x -= SPEED
        else:
            costado = True

    # ----------Colores----------#
    screen.fill((custom))  # --> Red , Green, Blue

    # pygame.draw.rect(screen, green, rect_1)
    # y = pygame.draw.rect(screen, yellow, rect_2)

    # z = draw.rect(screen, red, (300, pos_y, ancho, alto), 5)

    # Para que vaya de costado
    z = draw.rect(screen, red, (pos_x, pos_y, ancho, alto), 5)

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
    # ----> Actualiza la pantalla
    pygame.display.flip()


pygame.quit()


# ------------Manera 2------------#
# while True:
#     for event in pygame.event.get():  # -->Nos muestra los eventos que se realicen
#         if event.type == pygame.QUIT:
#             pygame.quit()  # -->Desconectamos pygame
#             sys.exit()  # --> Cerramos programa

#     pygame.display.flip()
