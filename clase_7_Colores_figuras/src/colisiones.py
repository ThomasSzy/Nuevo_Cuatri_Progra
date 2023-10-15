from math import *
def detectar_colision(rect_1, rect_2):

    for r1, r2 in [(rect_1, rect_2), (rect_1, rect_2)]:

        #--> lo que hace este for es iterar dos veces en el codigo y luego dice rect 1 y rect 2 vale esto
            #luego rect 1 y rect 2 se da vuelta y cambia de valores

        return punto_en_rectangulo(r1.topleft, r2) or \
            punto_en_rectangulo(r1.topright, r2) or \
            punto_en_rectangulo(r1.bottomright, r2) or \
            punto_en_rectangulo(r1.bottomleft, r2)
            


#Punto dentro de un rectanguulo


def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom


def detectar_colision_circulo(rect_1, rect_2):
    # distancia = distancia_entre_puntos(rect_1.center, rect_2.center) # --> Pasamos el centro del circulo 
    distancia = distancia_entre_centros_rectangulo(rect_1, rect_2)  # --> Pasamos los rectangulos y calcula los centros del rectangulo
    r1 = calcular_radio_rectangulo(rect_1)
    r2 = calcular_radio_rectangulo(rect_2)
    return distancia <= (r1 + r2) #--> si chocan o no, si chocan va a ser True de no ser asi es False

def distancia_entre_puntos(punto_1, punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return sqrt((y1 -y2) ** 2 + (x1 - x2) ** 2 )


def calcular_radio_rectangulo(rect):
    return rect.width // 2


def distancia_entre_centros_rectangulo(rect_1, rect_2):
    return distancia_entre_puntos(rect_1.center ,rect_2.center)
