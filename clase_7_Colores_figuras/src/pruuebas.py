def detectar_colision(rect_1, rect_2):

    if punto_en_rectangulo(rect_1.topleft, rect_2) or \
        punto_en_rectangulo(rect_1.topright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or\
        punto_en_rectangulo(rect_2.topleft, rect_1) or \
        punto_en_rectangulo(rect_2.topright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1):
            return True
    else:
        return False