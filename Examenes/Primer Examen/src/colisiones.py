from math import *


def calcular_radio_rectangulo(rect):
    return rect.width // 2


def distancia_entre_puntos(punto_1, punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)


def distancia_entre_centros_rectangulo(rect_1, rect_2):
    return distancia_entre_puntos(rect_1.center, rect_2.center)


def detect_colision_circle(rect_1, rect_2):
    distancia = distancia_entre_centros_rectangulo(rect_1, rect_2)
    r1 = calcular_radio_rectangulo(rect_1)
    r2 = calcular_radio_rectangulo(rect_2)
    return distancia <= (r1 + r2)
