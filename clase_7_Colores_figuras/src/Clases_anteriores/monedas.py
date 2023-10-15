import pygame
from pygame import *
from sys import *
from config_colores import *
from random import randint
from random import randrange
from colisiones import *




# print(detectar_colision(r1,r2))
# --> Funcion para diccionario
def crear_bloque(left = 0, top= 0, ancho= 40, alto= 40, color = (255, 255, 255),dir = 3, borde = 0, radio = -1, speed_x = 5, speed_y = 5):
    rec = pygame.Rect(left, top, ancho, alto)
    return {"rect":rec ,"color": color ,"dir": dir , "borde": borde , "radio": radio, "speed_x": speed_x, "speed_y": speed_y}



# ----------Inicializamos modulos de pygame----------#

pygame.init()  # --> Conectamos Pygame



# ----------Titulo----------#
pygame.display.set_caption("Primer Juego")

# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))

# ----------Colores----------#
screen.fill((custom))  # --> Red , Green, Blue

#Creo un reloj
clock = pygame.time.Clock()


#Evento personalizado

EVENT_NEW_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NEW_COIN, 3000)




fuente = pygame.font.SysFont(None, 48) 
#1)Fuente --> None = Arial
#2)Tamaño 

texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
rect_texto = texto.get_rect()
rect_texto.midtop = (width //2, 30)

block = crear_bloque(left = randint(0, width - block_width),
                    top = randint(0, height - block_height),
                    ancho = block_width,
                    alto = block_height,
                    color = red,
                    radio = 25
                    )

#Creamos lista de monedas

coins = []

for i in range(25):
    coins.append(crear_bloque(left = randint(0, width - size_coin),
                                top = randint(0, height - size_coin),
                                ancho = size_coin,
                                alto = size_coin,
                                color = yellow,
                                radio = size_coin // 2 # --> Las hace redondas
                                ))



is_ranning = True

while is_ranning:
    # ----> Tiempo
    clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG
    # ----> Detecta los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_ranning = False

        if event.type == EVENT_NEW_COIN:
            coins.append(crear_bloque(left = randint(0, width - size_coin),
                                top = randint(0, height - size_coin),
                                ancho = size_coin,
                                alto = size_coin,
                                color = magenta,
                                radio = size_coin // 2 # --> Las hace redondas
                                ))
    # ----> ACTUALIZA ELEMENTOS

    # Controlo rebote y cambio de direccion
    # rebote derecha pantalla
    if block["rect"].right >= width:
        if block["dir"] == DR:
            block["dir"] = DL
            # block["color"] = color_aleatoreo()
        elif block["dir"] == UR:
            block["dir"] = UL
            # block["color"] = color_aleatoreo()
            # block["borde"] = randrange(20)
            # block["speed_x"] = randint(1,10)
    # rebote izquierda pantalla
    elif block["rect"].left <= 0:
        if block["dir"] == DL:
            block["dir"] = DR
            # block["color"] = color_aleatoreo()
        elif block["dir"] == UL:
            block["dir"] = UR
            # block["color"] = color_aleatoreo()
            # block["radio"] = randrange(25) # -> Circulo
            # block["speed_x"] = randint(1,10)
    # rebote abajo pantalla
    elif block["rect"].bottom >= height:
        if block["dir"] == DR:
            block["dir"] = UR
            # block["color"] = color_aleatoreo()
            # block["speed_y"] = randint(1,10)
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

            # block["speed_y"] = randint(1,10)

# Muevo el rectangulo segun la direccion
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


    for coin in coins[ : ]: # ---> Creamo una copia y la modificamos de la lista original
        if detectar_colision_circulo(coin["rect"], block["rect"]):
            coins.remove(coin)
            contador_monedas +=1

            texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
            #1)Texto  2)Antialising  3)Color Fuente   4)Color Fondo
            rect_texto = texto.get_rect()
            rect_texto.midtop = (width //2, 30)

    # ----> Dibujar Pantalla
    screen.fill(black)

    for coin in coins:
        pygame.draw.rect(screen, coin["color"], coin["rect"], coin["borde"], coin["radio"])

    pygame.draw.rect(screen, block["color"], block["rect"], block["borde"],block["radio"])
    
    screen.blit(texto, rect_texto)
    # ----> Actualiza la pantalla
    pygame.display.flip()


pygame.quit()
