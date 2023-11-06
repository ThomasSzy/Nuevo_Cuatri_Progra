# Sonidos
import pygame
from pygame import *
from pygame.locals import *


def musica_intro():
    pygame.mixer.music.load("./src/sounds/musica_the_simpsons.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def music_game():
    pygame.mixer.music.load("./src/sounds/music_game.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def ouch():
    homero_ouch = pygame.mixer.Sound("./src/sounds/homero_ouch.mp3")
    homero_ouch.set_volume(0.1)
    homero_ouch.play()


def musica_final():
    pygame.mixer.music.load("./src/sounds/music_final.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)



