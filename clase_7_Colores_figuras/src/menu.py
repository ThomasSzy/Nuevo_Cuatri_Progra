import pygame
from pygame import *
from sys import *
from config_colores import *
from random import *
from colisiones import *
from pygame.locals import *
from utilidades import *

def mostrar_texto(superficie, texto, x, y, font_size=36, color=(0, 0, 0)):
    fuente = pygame.font.SysFont("comicsans", font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center=(x, y))
    superficie.blit(render, rect_texto)


def crear_boton(screen, rect: pygame.Rect, texto, color_normal, color_hover):
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius=10)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius=10)

    mostrar_texto(screen, texto, rect.centerx, rect.centery)


background_color_button = magenta
background_color_button_hover = yellow


pygame.init()  # --> Conectamos Pygame

# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))
# ----------Titulo----------#
pygame.display.set_caption("Menu")
# Creo un reloj
clock = pygame.time.Clock()


running = True

centro_x = screen.get_width() // 2

button_width = 200
button_heigth = 50

rect_saludar = pygame.Rect(centro_x - button_width / 2, 100, 200, 50)
rect_brindar = pygame.Rect(centro_x - button_width / 2, 160, 200, 50)
rect_despedir = pygame.Rect(centro_x - button_width / 2, 220, 200, 50)


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                # Coordenadas donde  se hizo click
                cursor = e.pos

                if rect_saludar.collidepoint(cursor[0], cursor[1]):
                    print("Hola Mundo")

                elif rect_brindar.collidepoint(cursor[0], cursor[1]):
                    print("Chin Chin...")

                elif rect_despedir.collidepoint(cursor[0], cursor[1]):
                    print("Cerrando Programa")
                    running = False

    screen.fill(black)

    crear_boton(
        screen,
        rect_saludar,
        "Saludar",
        background_color_button,
        background_color_button_hover,
    )
    crear_boton(
        screen,
        rect_brindar,
        "Brindar",
        background_color_button,
        background_color_button_hover,
    )
    crear_boton(
        screen,
        rect_despedir,
        "Despedir",
        background_color_button,
        background_color_button_hover,
    )

    pygame.display.flip()


pygame.quit()
exit()
