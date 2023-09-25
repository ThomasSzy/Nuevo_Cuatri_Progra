import pygame
from sys import *
from config_colores import *  
# Iniciamos Pygame
# mostramos pantallas
# Colores
# Hacemos dos manera de iniciar programa
# Colocamos un titulo a la pantalla

#----------Inicializamos modulos de pygame----------#

pygame.init()  # --> Conectamos Pygame

clock = pygame.time.Clock()

#----------Titulo----------#
pygame.display.set_caption("Primer Juego")

#----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))

#----------Colores----------#
screen.fill((custom))  # --> Red , Green, Blue

#------------Manera 1-------------#
# Inicializamos modulos de pygame
is_ranning = True

# Rectangulo
is_running = True

rect_1 = pygame.Rect(0,0,200,100)

rect_2 = (200, 200, 300, 150)


while is_ranning:
    # ----> Tiempo
    clock.tick(FPS) #-->FPS EN LA LISTA CONFIG

    # ----> Detecta los elementos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_ranning = False

    
    
    # ----> Actualiza los elementos
    pygame.draw.rect(screen, green, rect_1)
    pygame.draw.rect(screen, yellow, rect_2)
    # pygame.draw.rect(Donde?, Color, Rectangulo, [Borde])

#------------Muestra Colores------------#
    # ----> Actualiza la pantalla
    pygame.display.flip()


pygame.quit()




#------------Manera 2------------#
# while True:
#     for event in pygame.event.get():  # -->Nos muestra los eventos que se realicen
#         if event.type == pygame.QUIT:
#             pygame.quit()  # -->Desconectamos pygame
#             sys.exit()  # --> Cerramos programa

#     pygame.display.flip()