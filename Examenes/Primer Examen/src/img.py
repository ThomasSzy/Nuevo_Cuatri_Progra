import pygame
from pygame import *
from screen import *
import random

# Jugador
image_player = pygame.transform.scale(
    pygame.image.load("./src/imagenes/Homer.png"), (200, 200)
)

# donas
image_dona = pygame.transform.scale(
    pygame.image.load("./src/imagenes/dona_homero.png"), (200, 200)
)

# Enemigos
image_cerveza = pygame.transform.scale(
    pygame.image.load("./src/imagenes/cerveza_quitavida.png"), (200, 200)
)

image_rata = pygame.transform.scale(
    pygame.image.load("./src/imagenes/rata_enemigo.png"), (200, 200)
)

image_pescado = pygame.transform.scale(
    pygame.image.load("./src/imagenes/pescado_enemigo.png"), (200, 200)
)


# Disparo
image_eructo = pygame.image.load("./src/imagenes/eructo_homero.png")


# skill
image_cerveza_skill = pygame.transform.scale(
    pygame.image.load("./src/imagenes/cerveza_vida.png"), (200, 200)
)


# Fondo Inicio
home_background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/fondo_inicio.jpg"), size_screen
)

# Fondo Juego
background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/fondo_juego.jpg"), size_screen
)

# Fondo Options
options_background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/Fondo_Opciones.jpg"), size_screen
)

# fondo perdiste
lose_background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/fondo_perdiste.jpg"), size_screen
)

# Image The Simpsons
the_simpsons = pygame.transform.scale(
    pygame.image.load("./src/imagenes/the_simpsons.png"), screen_the_simpson
)


# Imagenes Enemys
enemys = [image_cerveza, image_pescado]
random_enemy = random.choice(enemys)
