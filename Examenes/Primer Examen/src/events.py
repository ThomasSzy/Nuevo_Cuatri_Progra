import pygame
from pygame import *

EVENT_NEW_ELEMENT = pygame.USEREVENT + 1
EVENT_NEW_SKILL = pygame.USEREVENT + 2
EVENT_NEW_BOSS = pygame.USEREVENT + 3

pygame.time.set_timer(EVENT_NEW_ELEMENT, 15000)
pygame.time.set_timer(EVENT_NEW_SKILL, 20000)
pygame.time.set_timer(EVENT_NEW_BOSS, 60000)
size_element = 100





