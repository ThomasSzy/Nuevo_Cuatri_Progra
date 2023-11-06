def load_elements_list(
    elements,
    cantidad,
    imagen=None,
    element_min=50,
    element_max=100,
    speed_a=1,
    speed_b=2,
):
    for i in range(cantidad):
        size_elements = randint(element_min, element_max)
        speed = randint(speed_a, speed_b)
        elements.append(
            create_block(
                imagen,
                left=randint(0, width - size_elements),
                top=randint(-height, -size_elements),
                ancho=size_elements,
                alto=size_elements,
                color=white,
                speed_y=speed,
                radio=size_elements // 2,  # --> Las hace redondas
            )
        )


def stock(key, float, image, altura_a, altura_b, speed_a, speed_b):
    if len(key) == 0:
        load_elements_list(key, float, image, altura_a, altura_b, speed_a, speed_b)


# Speed
speed = 2
speed_donas_min = 1
speed_donas_max = 3

speed_enemy_min = 2
speed_enemy_max = 4
# Tamaños
tam_element_min = 50
tam_element_max = 120

tam_enemy_min = 50
tam_enemy_max = 150
