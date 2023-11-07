import pygame
from screen import *
from colors import *
from random import randint
from sys import *
from pygame import *
from img import *
from colisiones import *
from events import *
from sound import *
from button import *
import os
import json


def create_block(
    imagen=None,
    left=0,
    top=0,
    ancho=40,
    alto=40,
    color=(255, 255, 255),
    borde=0,
    radio=-1,
    speed_x=5,
    speed_y=5,
):
    """
    Crea el rectangulo para los objetos, personajes, etc

    Args:
        imagen (img): imagen para el objeto o personaje
        left (int): la coordenada x del bloque
        top (int): la coordenada y del bloque
        ancho (int): ancho del objeto
        alto (int): alto del objeto.
        color (int): color del rect
        borde (int): Borde del rect
        radio (int): el radio en caso de ser redondo
        speed_x (int): La velocidad del personaje / objeto sobre el eje x
        speed_y (int): La velocidad del personaje / objeto sobre el eje y

    Returns:
        dict: Retorna un diccionario con los valores del rect separados por Id
    """
    rec = pygame.Rect(left, top, ancho, alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return {
        "rect": rec,
        "color": color,
        "borde": borde,
        "radio": radio,
        "speed_x": speed_x,
        "speed_y": speed_y,
        "imagen": imagen,
    }


def stock(key, float, image, altura_a, altura_b, speed_a, speed_b):
    """
    Crea nuevos objetos si ya en pantalla no quedan mas

    Args:
        key (str): tipo de objeto a crear
        float (int): Cantidad de objetos
        image (img): imagen del objeto
        altura_a (int): altura minima
        altura_b (int): altura maxima
        speed_a (int): velocidad minima
        speed_b (int): velocidad maxima
    """
    if len(key) == 0:
        load_elements_list(key, float, image, altura_a, altura_b, speed_a, speed_b)


def paint_elements(superficie, elements):
    """
    Dibuja los elementos

    Args:
        superficie (int): tamaño de pantalla
        elements (str): el elemento a dibujar
    """
    for element in elements:
        if element["imagen"]:
            superficie.blit(element["imagen"], element["rect"])
        else:
            pygame.draw.rect(
                superficie,
                element["color"],
                element["rect"],
                element["borde"],
                element["radio"],
            )


def screen_text(
    suuperficie, texto, fuente, coordenadas, color_fuente, color_fondo=black
):
    """
    Muestra un texto en pantalla

    Args:
        suuperficie (int): tamaño en pantalla
        texto (str): texto que muestra en pantalla
        fuente (str): tipo de fuente
        coordenadas (int): donde ubica el texto
        color_fuente (str): Color de la fuente
        color_fondo (str): Color de la fondo del texto.
    """
    sup_text = fuente.render(texto, True, color_fuente, color_fondo)
    rect_text = sup_text.get_rect()
    rect_text.center = coordenadas
    suuperficie.blit(sup_text, rect_text)


def screen_text_boton(superficie, texto, x, y, font_size=24, color=black):
    """
    Muestra el texto del boton

    Args:
        superficie (int): donde se coloca el boton
        texto (str): El texto que va encima del boton
        x (int): Posicion del rect en el eje x
        y (int): Posicion del rect en el eje y
        font_size (int): tamaño de fuente
        color (str): Color del texto
    """
    fuente = pygame.font.SysFont("comicsans", font_size)
    render = fuente.render(texto, True, color)
    rect_text = render.get_rect(center=(x, y))
    superficie.blit(render, rect_text)


def exit_game():
    """
    Quita el juego
    """
    pygame.QUIT
    exit()


def wait_user():
    """
    Quita el juego al colocar la tecla definida
    detiene el juego temporalmente para y esperar a la accion que realice el usuario

    Returns:
        None: La funcion no devuelve ningun valor
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit_game()
                return None


def crear_boton(screen, rect, texto, color_normal, color_hover):
    """
    Crea los botones y su iteracion

    Args:
        screen (int): tamaño de pantalla
        rect (int): rectangulo del boton
        texto (str): texto que muestra el boton
        color_normal (str): Color principal
        color_hover (str): Color al pasar el mouse por encima
    """
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius=20)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius=20)

    screen_text_boton(screen, texto, rect.centerx, rect.centery)


def options():
    """
    Muestra la pantalla de opciones.

    esta funcion se encarga de crear mostrar las opciones del juego y
    poder volver hacia el menu principal.
    """
    pygame.mixer.music.stop()
    pygame.display.set_caption("Options")

    while True:
        pygame.mouse.set_visible(True)

        boton_back = pygame.Rect(380, 680, 200, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if boton_back.collidepoint(cursor[0], cursor[1]):
                        pygame.display.set_caption("The Simpsons")
                        main_menu()

        screen.blit(options_background, (0, 0))
        crear_boton(
            screen,
            boton_back,
            "Back",
            yellow,
            blue,
        )
        pygame.display.flip()


def main_menu():
    """
    Muestra la pantalla del menu y sus botones

    esta funcion se encarga de mostrar los botones detectando las interacciones
    para continuar donde realice el click.
    """
    global contador_grande, font, cont_donas
    font = pygame.font.SysFont(None, 30)
    musica_intro()
    while True:
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if boton_comenzar.collidepoint(cursor[0], cursor[1]):
                        try:
                            init_game()
                        except ValueError:
                            "La funcion del juego contiene un error"
                    elif boton_options.collidepoint(cursor[0], cursor[1]):
                        options()
                    elif boton_quit.collidepoint(cursor[0], cursor[1]):
                        exit()

        screen.blit(home_background, (0, 0))
        screen.blit(the_simpsons, (80, 0))

        crear_boton(
            screen,
            boton_comenzar,
            "Comenzar",
            yellow,
            blue,
        )
        crear_boton(
            screen,
            boton_options,
            "Opciones",
            yellow,
            blue,
        )
        crear_boton(
            screen,
            boton_quit,
            "Salir",
            yellow,
            blue,
        )

        pygame.display.flip()


def load_elements_list(
    elements,
    cantidad,
    imagen=None,
    element_min=50,
    element_max=100,
    speed_a=1,
    speed_b=2,
):
    """
    Crea los elementos, habilidades y enemigos
    Args:
        elements (str): ingresa el nombre del elemento
        cantidad (int): Ingresa la cantidad de objetos a crear
        imagen (img): Ingresa la imagen del elemento. De no tener queda en None.
        element_min (int): Ingresa la altura minima del elemento. Defaults to 50.
        element_max (int): Ingresa la altura maxima del elemento. Defaults to 100.
        speed_a (int): La velocidad minima del elemento. Defaults to 1.
        speed_b (int): la velocidad maxima del elemento. Defaults to 2.
    """
    if cantidad >= 0:
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
    else:
        print("La cantidad no puede ser menor a 0")


def puntuacion_max(point):
    """
    Crea un archivo de no tenerlo creado.
    compara la puntacion con la del archivo en caso de existir sino lo crea, y nos muestra la puntuacion maxima.

    Args:
        point (int): puntuacion actual
    """
    directorio = os.getcwd()
    path_completo = os.path.join(directorio, "puntuacion_maxima.txt")

    try:
        if os.path.exists(path_completo):
            with open(path_completo, "r") as file:
                puntuacion_maxima = int(file.read())
        else:
            puntuacion_maxima = 0

        if point > puntuacion_maxima:
            with open(path_completo, "w") as file:
                file.write(str(point))
    except Exception as error:
        print(f"Error al actualizar el archivo {str(error)}")


# Rectangulo
block_width = 150
block_height = 150

# Creamos Jugador
block = create_block(
    image_player,
    left=300,
    top=(800 - block_height),
    ancho=block_width,
    alto=block_height,
    color=red,
)


def init_game():
    """
    Inicializa el juego principal

    contiene la logica de los movimientos, las vidas, habilidades del personaje y eventos personalizados.
    realiza acciones dependiendo la colision de los del personaje con los objetos en pantalla.


    """
    pygame.mixer.music.stop()
    play_music = True
    music_game()
    clock = pygame.time.Clock()
    cont_donas = 0
    lives = 3
    habilidad = 0
    while True:
        move_right = False
        move_left = False
        is_running = True

        eructo_rafagas = False
        eructo_largo = True
        eructos = []
        elements = []
        enemys = []
        habilidades = []
        enemy_final = []
        load_elements_list(enemys, 3, image_cerveza)
        load_elements_list(enemy_final, 1, image_rata)
        load_elements_list(elements, 10, image_dona)
        load_elements_list(habilidades, 2, image_cerveza_skill)

        while is_running:
            clock.tick(FPS)
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

                if event.type == EVENT_NEW_ELEMENT:
                    enemys.append(
                        create_block(
                            image_pescado,
                            left=randint(0, width - size_element),
                            top=(height - 900),
                            ancho=size_element,
                            alto=size_element,
                        )
                    )
                if event.type == EVENT_NEW_SKILL:
                    habilidades.append(
                        create_block(
                            image_cerveza_skill,
                            left=randint(0, width - size_element),
                            top=(height - 900),
                            ancho=size_element,
                            alto=size_element,
                            radio=size_element // 2,  # --> Las hace redondas
                        )
                    )

                if event.type == EVENT_NEW_SKILL:
                    enemy_final.append(
                        create_block(
                            image_rata,
                            left=randint(0, width - size_element),
                            top=(height - 900),
                            ancho=size_element,
                            alto=size_element,
                            radio=size_element // 2,  # --> Las hace redondas
                        )
                    )

                if event.type == KEYDOWN:
                    if event.key == K_d or event.key == K_RIGHT:
                        move_right = True
                        move_left = False

                    if event.key == K_a or event.key == K_LEFT:
                        move_left = True
                        move_right = False

                    if event.key == K_f:
                        if eructo_largo:
                            if not eructo_rafagas:
                                mid_top = block["rect"].midtop
                                (eructo_w, eructo_h) = size_eructo

                                eructos.append(
                                    create_block(
                                        image_eructo,
                                        mid_top[0] - eructo_w // 2,
                                        mid_top[1] - eructo_h,
                                        eructo_w,
                                        eructo_h,
                                        1,
                                    )
                                )
                                eructo_rafagas = True

                    if event.key == K_p:
                        if music_game:
                            pygame.mixer.music.pause()
                        screen.blit(lose_background, (0, 0))
                        screen_text(screen, "Pausa", font, center_screen, red, black)
                        pygame.display.flip()
                        wait_user()

                    if event.key == K_m:
                        if play_music == True:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                        play_music = not play_music

                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        exit()

                    if event.key == K_d or event.key == K_RIGHT:
                        move_right = False

                    if event.key == K_a or event.key == K_LEFT:
                        move_left = False

            # Movimiento personaje

            if move_right and block["rect"].right <= (width - speed):
                block["rect"].left += speed

            if move_left and block["rect"].left >= (0 + speed):
                block["rect"].left -= speed

            # dibujamos
            for element in elements:
                element["rect"].move_ip(0, element["speed_y"])

            for enemy in enemys:
                enemy["rect"].move_ip(0, enemy["speed_y"])

            for habilidad in habilidades:
                habilidad["rect"].move_ip(0, habilidad["speed_y"])

            for enemy_f in enemy_final:
                enemy_f["rect"].move_ip(0, enemy_f["speed_y"])

            # Choque con Personaje

            for element in elements[:]:
                if detect_colision_circle(element["rect"], block["rect"]):
                    elements.remove(element)
                    cont_donas += 1

            # Agregamos lo mismo para una suma de puntos
            for habilidad in habilidades[:]:
                if detect_colision_circle(habilidad["rect"], block["rect"]):
                    habilidades.remove(habilidad)
                    if lives <= 4:
                        lives += 1

            for enemy in enemys[:]:
                if detect_colision_circle(enemy["rect"], block["rect"]):
                    enemys.remove(enemy)
                    lives -= 1
                    ouch()

            for enemy_f in enemy_final[:]:
                if detect_colision_circle(enemy_f["rect"], block["rect"]):
                    enemy_final.remove(enemy_f)
                    ouch()
                    lives -= 3

            # Agrega elementos cuando no lo hay
            stock(
                elements,
                randint(7, 15),
                image_dona,
                tam_element_min,
                tam_element_max,
                speed_donas_min,
                speed_donas_max,
            )
            stock(
                enemys,
                randint(1, 10),
                random_enemy,
                tam_enemy_min,
                tam_enemy_max,
                speed_enemy_min,
                speed_enemy_max,
            )

            if eructo_largo:
                for eructo in eructos[:]:
                    if eructo["rect"].bottom > 0:
                        eructo["rect"].move_ip(0, -eructo["speed_y"])
                    else:
                        eructos.remove(eructo)
                        eructo_rafagas = False

            for enemy in enemys[:]:
                if enemy["rect"].top > height:
                    enemy["rect"].y = -enemy["rect"].height
                    enemy["rect"].x = randint(0, width - enemy["rect"].width)

            for enemy_f in enemy_final[:]:
                if enemy_f["rect"].top > height:
                    enemy_f["rect"].y = -enemy_f["rect"].height
                    enemy_f["rect"].x = randint(0, width - enemy_f["rect"].width)

            for habilidad in habilidades[:]:
                if habilidad["rect"].top > height:
                    habilidad["rect"].y = -habilidad["rect"].height
                    habilidades.remove(habilidad)

            for element in elements[:]:
                if element["rect"].top > height:
                    element["rect"].y = -element["rect"].height
                    element["rect"].x = randint(0, width - element["rect"].width)

            # Colision Eructos
            if eructo_largo:
                for eructo in eructos[:]:
                    remove_objet = False
                    for element in elements[:]:
                        if detect_colision_circle(element["rect"], eructo["rect"]):
                            elements.remove(element)
                            cont_donas += 1
                            remove_objet = True

                    for habilidad in habilidades[:]:
                        if detect_colision_circle(habilidad["rect"], eructo["rect"]):
                            habilidades.remove(habilidad)
                            if lives <= 4:
                                lives += 1
                            remove_objet = True
                    for enemy_f in enemy_final[:]:
                        if detect_colision_circle(enemy_f["rect"], eructo["rect"]):
                            enemy_final.remove(enemy_f)
                            cont_donas += 1
                            remove_objet = True
                    for enemy in enemys[:]:
                        if detect_colision_circle(enemy["rect"], eructo["rect"]):
                            enemys.remove(enemy)
                            cont_donas += 1
                            remove_objet = True
                    if remove_objet:
                        eructos.remove(eructo)
                        eructo_rafagas = False
            screen.blit(background, (0, 0))

            paint_elements(screen, habilidades)
            paint_elements(screen, elements)
            paint_elements(screen, enemys)
            paint_elements(screen, enemy_final)

            if eructo_largo:
                for eructo in eructos:
                    screen.blit(eructo["imagen"], eructo["rect"])
            else:
                if eructo:
                    screen.blit(eructo["imagen"], eructo["rect"])

            live_text = f"Vidas Restantes: {lives}"
            screen_text(screen, live_text, font, (510, 10), white)
            donas_text = f"Donas recogidas: {cont_donas}"
            screen_text(screen, donas_text, font, (30, 10), white)
            screen.blit(block["imagen"], block["rect"])
            pygame.display.flip()

            if lives < 1:
                is_running = False

        point = cont_donas
        puntuacion_max(point)
        game_over(point)

        pygame.display.flip()


def game_over(point):
    """
    Pantalla de Game Over
    esta pantalla muestra el score maximo, el que realizaste y un boton para volver al menu

    Args:
        point (int): Puntuacion del jugador
    """

    font_game_over = pygame.font.SysFont(None, 40)
    pygame.mixer.music.stop()
    musica_final()

    directorio = os.getcwd()
    path_completo = os.path.join(directorio, "puntuacion_maxima.txt")
    with open(path_completo, "r") as file:
        point_max = int(file.read())

    while True:
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if boton_back.collidepoint(cursor[0], cursor[1]):
                        main_menu()
                    elif boton_quit.collidepoint(cursor[0], cursor[1]):
                        exit()

        screen.blit(lose_background, (0, 0))
        puntos = f"Puntos Actuales: {point}"
        screen_text(screen, puntos, font_game_over, (width // 2, 350), white)
        max_point = f"La puntuacion maxima es {point_max}"
        screen_text(screen, max_point, font_game_over, (width // 2, 200), white)
        crear_boton(
            screen,
            boton_back,
            "MAIN",
            yellow,
            blue,
        )
        crear_boton(
            screen,
            boton_quit,
            "QUIT",
            yellow,
            blue,
        )
        pygame.display.flip()


# Enemys, life and skills
good_element_min = 10
good_element_max = 30

skill_element_min = 1
skill_element_max = 5

enemy_element_min = 5
enemy_element_max = 15
# Speed
speed = 2
speed_donas_min = 1
speed_donas_max = 3

speed_enemy_min = 1
speed_enemy_max = 4
# Tamaños
tam_element_min = 50
tam_element_max = 100

tam_enemy_min = 50
tam_enemy_max = 100

# Eructo
size_eructo = (60, 60)
# Time
FPS = 60

cont_elements = 0
