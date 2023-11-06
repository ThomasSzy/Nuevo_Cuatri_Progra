import pygame
from config_colores import *


def mostrar_texto_boton(superficie, texto, x, y, font_size=24, color=white):
    fuente = pygame.font.SysFont("comicsans", font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center=(x, y))
    superficie.blit(render, rect_texto)


def crear_boton(screen, rect: pygame.Rect, texto, color_normal, color_hover):
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius=20)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius=20)

    mostrar_texto_boton(screen, texto, rect.centerx, rect.centery)
