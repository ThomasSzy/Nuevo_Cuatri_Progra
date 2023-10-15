import pygame
from pygame import *
from sys import *
from config_colores import *
from random import randint
from random import randrange
from colisiones import *
from pygame.locals import *



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

EVENT_COIN_GOLD = pygame.USEREVENT + 2

pygame.time.set_timer(EVENT_NEW_COIN, 5000)

pygame.time.set_timer(EVENT_COIN_GOLD, 15000)

#Direccion movimiento


move_up = False
move_rigth = False
move_down = False
move_left = False







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
                                color = white,
                                radio = size_coin // 2 # --> Las hace redondas
                                ))



is_ranning = True

while is_ranning:
    # ----> Tiempo
    clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG
    # ----> Detecta los eventos
    for event in pygame.event.get():
        if event.type == QUIT: #-> Va con from pygame.locals import *
            is_ranning = False

        if event.type == EVENT_NEW_COIN:
            coins.append(crear_bloque(left = randint(0, width - size_coin),
                                top = randint(0, height - size_coin),
                                ancho = size_coin,
                                alto = size_coin,
                                color = magenta,
                                radio = size_coin // 2 # --> Las hace redondas
                                ))
        if event.type == EVENT_COIN_GOLD:
            coins.append(crear_bloque(left = randint(0, width - size_coin_rainbow),
                                top = randint(0, height - size_coin_rainbow),
                                ancho = size_coin_rainbow,
                                alto = size_coin_rainbow,
                                color = gold,
                                radio = size_coin_rainbow // 2 # --> Las hace redondas
                                ))
            
        if event.type == KEYDOWN:
            if event.key == K_d or event.key == K_RIGHT:
                move_rigth = True
                move_left = False

            if event.key == K_a or event.key == K_LEFT:
                move_left = True
                move_rigth = False

            if event.key == K_w or event.key == K_UP:
                move_up= True
                move_down = False
            if event.key == K_s or event.key == K_DOWN:
                move_down = True
                move_up = False
        if event.type == KEYUP:
            #Salir Al soltar el Escape
            if event.key == K_ESCAPE:
                is_ranning = False

            if event.key == K_d or event.key == K_RIGHT:
                move_rigth = False

            if event.key == K_a or event.key == K_LEFT:
                move_left = False

            if event.key == K_w or event.key == K_UP:
                move_up= False

            if event.key == K_s or event.key == K_DOWN:
                move_down = False
        
        if event.type == MOUSEBUTTONDOWN:
            coins.append(crear_bloque(left = randint(0, width - size_coin),
                                top = randint(0, height - size_coin),
                                ancho = size_coin,
                                alto = size_coin,
                                color = blue,
                                radio = size_coin // 2 # --> Las hace redondas
                                ))
    # ----> ACTUALIZA ELEMENTOS


#----> Muevo el rectangulo segun la direccion <----
    if  move_rigth and block["rect"].right <= (width - speed) :
        #Derecha
        block["rect"].left += speed

    if move_left and block["rect"].left >= (0 + speed):
        #Izquierda
        block["rect"].left -= speed

    if move_up and block["rect"].top >= (0 + speed):
    # Arriba
        block["rect"].top -= speed
    
    if move_down and block["rect"].bottom <= (height - speed):
        #Abajo
        block["rect"].top += speed


    for coin in coins[ : ]: # ---> Creamos una copia y la modificamos de la lista original
        if detectar_colision_circulo(coin["rect"], block["rect"]):
            coins.remove(coin)
            if coin["color"] == gold: # --> Si la moneda es color dorado la puntuacion vale doble
                contador_monedas +=2
            else: 
                contador_monedas +=1 #--> de lo contrario la moneda sigue valiendo 1
        
            texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
            #1)Texto  2)Antialising  3)Color Fuente   4)Color Fondo
            rect_texto = texto.get_rect()
            rect_texto.midtop = (width //2, 30)
            cont_grande = 10
    
    if cont_grande > 0:
        cont_grande -= 1
        block["rect"].width = block_width * 1.1
        block["rect"].height = block_height * 1.1
        block["color"] = color_aleatoreo()
    else:
        block["rect"].width = block_width
        block["rect"].height = block_height
        block["color"] = red
    # ----> Dibujar Pantalla
    screen.fill(black)

    for coin in coins:
        pygame.draw.rect(screen, coin["color"], coin["rect"], coin["borde"], coin["radio"])

    pygame.draw.rect(screen, block["color"], block["rect"], block["borde"],block["radio"])
    
    screen.blit(texto, rect_texto)
    # ----> Actualiza la pantalla
    pygame.display.flip()


pygame.quit()
