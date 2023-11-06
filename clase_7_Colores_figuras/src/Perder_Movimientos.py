import pygame
from pygame import *
from sys import *
import config_colores
from config_colores import *
from random import randint
from random import randrange
from colisiones import *
from pygame.locals import *
from utilidades import *

# print(detectar_colision(r1,r2))
# --> Funcion para diccionario


def mostrar_texto(
    suuperficie, texto, fuente, coordenadas, color_fuente, color_fondo=black
):
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenadas
    suuperficie.blit(sup_texto, rect_texto)


def terminar():
    pygame.QUIT
    exit()


# Pausa
def wait_user():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # -> Va con from pygame.locals import *
                terminar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminar()
                return None  # --> Terminamos la Funcion


# Esperar que el usuario haga click
def wait_user_click(rect_1: pygame.Rect):
    while True:
        crear_boton(screen, rect_1, "Comenzar Juego", blue, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:  # -> Va con from pygame.locals import *
                terminar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminar()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_1.collidepoint(
                        event.pos
                    ):  # Si el rect_1 colisiona con la pos del mouse
                        return None


def crear_bloque(
    imagen=None,  # --> Imagen si no la pasan no se coloca
    left=0,
    top=0,
    ancho=40,
    alto=40,
    color=(255, 255, 255),
    dir=3,
    borde=0,
    radio=-1,
    speed_x=5,
    speed_y=5,
):
    rec = pygame.Rect(left, top, ancho, alto)

    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))

    return {
        "rect": rec,
        "color": color,
        "dir": dir,
        "borde": borde,
        "radio": radio,
        "speed_x": speed_x,
        "speed_y": speed_y,
        "imagen": imagen,
    }


def load_coins_list(coins, cantidad, imagen=None):
    for i in range(cantidad):
        size_coin = randint(size_min_coin, size_max_coin)
        speed_coin = randint(speed_min, speed_max)
        coins.append(
            crear_bloque(
                imagen,
                left=randint(0, width - size_coin),
                top=randint(-height, -size_coin),
                ancho=size_coin,
                alto=size_coin,
                color=white,
                speed_y=speed_coin,
                radio=size_coin // 2,  # --> Las hace redondas
            )
        )


def dibujar_asteroides(superficie, coins):
    for coin in coins:
        if coin["imagen"]:
            superficie.blit(coin["imagen"], coin["rect"])
        else:
            pygame.draw.rect(
                superficie, coin["color"], coin["rect"], coin["borde"], coin["radio"]
            )


# ----------Inicializamos modulos de pygame----------#

pygame.init()  # --> Conectamos Pygame


# ----------Titulo----------#
pygame.display.set_caption("Primer Juego")

# ----------Tamaño pantalla----------#
screen = pygame.display.set_mode((size_screen))
# ----------Colores----------#
screen.fill((custom))  # --> Red , Green, Blue

# Creo un reloj
clock = pygame.time.Clock()

# Seteo Sonidos!
# Sonidos cortos
game_over_sound = pygame.mixer.Sound("./src/Sonidos/mario-bros-die.mp3")
coin_sound = pygame.mixer.Sound("./src/Sonidos/gameboy-1.mp3")
end_level_sound = pygame.mixer.Sound("./src/Sonidos/victory-sonic.mp3")

coin_sound.set_volume(0.1)
game_over_sound.set_volume(0.1)
end_level_sound.set_volume(0.1)

# Cancion de fondo
pygame.mixer.music.load("./src/Sonidos/tetrisgameboy1-gameboy.mp3")

# pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.1)
playing_music = True


# Cargo Imagenes

image_player = pygame.image.load("./src/imagenes/homer_personaje.jpg")
image_asteroid = pygame.image.load("./src/imagenes/asteroid.png")
image_asteroid_especial = pygame.image.load("./src/imagenes/asteroid_especial.png")

background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/Estrellas.jpg"), size_screen
)

# Evento personalizado

EVENT_NEW_COIN = pygame.USEREVENT + 1

EVENT_COIN_GOLD = pygame.USEREVENT + 2

pygame.time.set_timer(EVENT_NEW_COIN, 5000)

pygame.time.set_timer(EVENT_COIN_GOLD, 15000)

# Direccion movimiento


move_up = False
move_rigth = False
move_down = False
move_left = False


# Establezco Fuente
fuente = pygame.font.SysFont(None, 30)

texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
rect_texto = texto.get_rect(topleft=(30, 40))

texto_lives = fuente.render(f"Lives: {lives}", True, magenta)
rect_texto_lives = texto_lives.get_rect(topright=(width - 30, 40))
# rect_texto.midtop = (width // 2, 30)

block = crear_bloque(
    image_player,
    left=randint(0, width - block_width),
    top=randint(0, height - block_height),
    ancho=block_width,
    alto=block_height,
    color=red,
    radio=25,
)

button_comenzar = pygame.Rect(0, 0, button_width, button_heigth)
button_comenzar.center = center_screen


while True:
    screen.fill(black)
    mostrar_texto(screen, "Asteroids", fuente, (width // 2, 20), cyan)
    wait_user_click(button_comenzar)  # --> Se escapa de la pausa / menu
    pygame.mouse.set_visible(False)
    contador_monedas = 0
    is_ranning = True
    pygame.mixer.music.play(-1)

    coins = []
    lasers = []
    rafaga = True
    load_coins_list(coins, count_coins, image_asteroid)

    while is_ranning:
        # ----> Tiempo
        clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG
        for event in pygame.event.get():
            if event.type == QUIT:  # -> Va con from pygame.locals import *
                is_ranning = False

            if event.type == EVENT_NEW_COIN:
                coins.append(
                    crear_bloque(
                        None,
                        left=randint(0, width - size_coin),
                        top=randint(0, height - size_coin),
                        ancho=size_coin,
                        alto=size_coin,
                        color=magenta,
                        radio=size_coin // 2,  # --> Las hace redondas
                    )
                )
            if event.type == EVENT_COIN_GOLD:
                coins.append(
                    crear_bloque(
                        None,
                        left=randint(0, width - size_coin_rainbow),
                        top=randint(0, height - size_coin_rainbow),
                        ancho=size_coin_rainbow,
                        alto=size_coin_rainbow,
                        color=gold,
                        radio=size_coin_rainbow // 2,  # --> Las hace redondas
                    )
                )

            if event.type == KEYDOWN:
                if event.key == K_f:
                    if rafaga:
                        mid_top = block["rect"].midtop
                        (
                            laser_w,
                            laser_h,
                        ) = size_laser
                
                        lasers.append(
                            crear_bloque(
                                None,
                                mid_top[0] - laser_w // 2,
                                mid_top[1] - laser_h,
                                laser_w,
                                laser_h,
                                red,
                                speed_laser,
                            )
                        )

                    else:
                        if not laser:
                            mid_top = block["rect"].midtop
                            (
                                laser_w,
                                laser_h,
                            ) = size_laser

                            laser = crear_bloque(
                                None,
                                mid_top[0] - laser_w // 2,
                                mid_top[1] - laser_h,
                                laser_w,
                                laser_h,
                                red,
                                speed_laser,
                            )

                if event.key == K_d or event.key == K_RIGHT:
                    move_rigth = True
                    move_left = False

                if event.key == K_a or event.key == K_LEFT:
                    move_left = True
                    move_rigth = False

                if event.key == K_w or event.key == K_UP:
                    move_up = True
                    move_down = False

                if event.key == K_s or event.key == K_DOWN:
                    move_down = True
                    move_up = False

                # Pausar Musica
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                    playing_music = not playing_music
                    # --> Esta bandera la usamos para saber si tiene que sonar o no

                if event.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                    mostrar_texto(screen, "Pausa", fuente, center_screen, red, black)
                    pygame.display.flip()

                    wait_user()
                    if playing_music:
                        pygame.mixer.music.unpause()

                if event.key == K_r:
                    trick_reverse = True

                if event.key == K_l:
                    trick_slow = True

                if event.key == K_i:
                    rafaga = not rafaga

            if event.type == KEYUP:
                # Salir Al soltar el Escape
                if event.key == K_ESCAPE:
                    is_ranning = False

                if event.key == K_d or event.key == K_RIGHT:
                    move_rigth = False

                if event.key == K_a or event.key == K_LEFT:
                    move_left = False

                if event.key == K_w or event.key == K_UP:
                    move_up = False

                if event.key == K_s or event.key == K_DOWN:
                    move_down = False

                if event.key == K_r:
                    trick_reverse = False

                if event.key == K_l:
                    trick_slow = False

            # CLICK BOTON AGRENGANDO FORMAS DONDE TOQUEMOS
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not laser:
                        mid_top = block["rect"].midtop
                        (
                            laser_w,
                            laser_h,
                        ) = size_laser

                        laser = crear_bloque(
                            None,
                            mid_top[0] - laser_w // 2,
                            mid_top[1] - laser_h,
                            laser_w,
                            laser_h,
                            red,
                            speed_laser,
                        )
                    # ENVIAR PERSONAJE AL MEDIO!
                if event.button == 2:
                    block["rect"].topleft = center_screen

            if event.type == MOUSEMOTION:
                block["rect"].center = (event.pos[0], event.pos[1])

        # ----> ACTUALIZA ELEMENTOS

        # ----> Muevo el rectangulo segun la direccion <----
        if move_rigth and block["rect"].right <= (width - speed):
            # Derecha
            block["rect"].left += speed

        if move_left and block["rect"].left >= (0 + speed):
            # Izquierda
            block["rect"].left -= speed

        if move_up and block["rect"].top >= (0 + speed):
            # Arriba
            block["rect"].top -= speed

        if move_down and block["rect"].bottom <= (height - speed):
            # Abajo
            block["rect"].top += speed
        # QUE EL MOUSE SIGA EL LUGAR DE LA NAVE SI MOVEMOS CON TECLAS
        pygame.mouse.set_pos(block["rect"].centerx, block["rect"].centery)

        # MOVEMOS ASTEROIDES

        for coin in coins:
            if not (trick_reverse or trick_slow):
                coin["rect"].move_ip(0, coin["speed_y"])

            # Esten en Reversa
            elif trick_reverse:
                coin["rect"].move_ip(0, -coin["speed_y"])

            # Mas Velocidad
            elif trick_slow:
                coin["rect"].move_ip(0, 1)
            # QUE NO SE DEL EJE X Y SE MUEVA 5PX DEL EJE Y

        # MUEVO EL LASER
        if rafaga:
            for laser in lasers[:]:
                if laser["rect"].bottom > 0:
                    laser["rect"].move_ip(0, -laser["speed_y"])
                else:
                    lasers.remove(laser)
        else:
            if laser:
                if laser["rect"].bottom > 0:
                    laser["rect"].move_ip(0, -laser["speed_y"])
                else:
                    laser = None

        for coin in coins:
            if not trick_reverse and not trick_slow:
                coin["rect"].move_ip(0, coin["speed_y"])
            elif trick_reverse == True:
                coin["rect"].move_ip(0, -coin["speed_y"])
            elif trick_slow == True:
                coin["rect"].move_ip(0, 1)

        # MONEDA APARECE ARRIBA Y DESAPARECE DE ABASJO
        # IMPORTANTE
        for coin in coins[:]:
            if coin["rect"].top > height:
                coin["rect"].y = -coin["rect"].height

        for coin in coins[:]:
            # ---> Creamos una copia y la modificamos de la lista original
            if detectar_colision_circulo(coin["rect"], block["rect"]):
                coins.remove(coin)

                if lives >= 1:
                    lives -= 1
                    texto_lives = fuente.render(f"Lives: {lives}", True, white)
                    rect_texto_lives = texto_lives.get_rect(topright=(width - 30, 40))
                else:
                    is_ranning = False

                if (
                    coin["color"] == gold
                ):  # --> Si la moneda es color dorado la puntuacion vale doble
                    contador_monedas += 2
                else:
                    contador_monedas += (
                        1  # --> de lo contrario la moneda sigue valiendo 1
                    )

                # Pausar efectos de coins

                if playing_music:
                    coin_sound.play()

        if len(coins) == 0:
            load_coins_list(coins, count_coins, image_asteroid_especial)
            end_level_sound.play()

        if rafaga:
            for laser in lasers[:]:
                colision = False
                for coin in coins[:]:
                    # ---> Creamos una copia y la modificamos de la lista original
                    if detectar_colision_circulo(coin["rect"], laser["rect"]):
                        coins.remove(coin)
                        if (
                            coin["color"] == gold
                        ):  # --> Si la moneda es color dorado la puntuacion vale doble
                            contador_monedas += 2
                        else:
                            contador_monedas += (
                                1  # --> de lo contrario la moneda sigue valiendo 1
                            )

                        texto_lives = fuente.render(f"Lives: {lives}", True, magenta)
                        rect_texto_lives = texto_lives.get_rect(
                            topright=(width - 30, 40)
                        )

                        # buscar
                        texto = fuente.render(
                            f"coins: {contador_monedas}", True, magenta
                        )
                        rect_texto = texto.get_rect(topleft=(30, 40))
                        cont_grande = 10
                        colision = True
                        # Pausar efectos de coins
                        if playing_music:
                            coin_sound.play()

                        if len(coins) == 0:
                            load_coins_list(coins, count_coins, image_asteroid_especial)
                            end_level_sound.play()
                if colision == True:
                    lasers.remove(laser)

        else:
            if laser:
                colision = False
                for coin in coins[:]:
                    # ---> Creamos una copia y la modificamos de la lista original
                    if detectar_colision_circulo(coin["rect"], laser["rect"]):
                        coins.remove(coin)
                        if (
                            coin["color"] == gold
                        ):  # --> Si la moneda es color dorado la puntuacion vale doble
                            contador_monedas += 2
                        else:
                            contador_monedas += (
                                1  # --> de lo contrario la moneda sigue valiendo 1
                            )
                        texto = fuente.render(
                            f"coins: {contador_monedas}", True, magenta
                        )
                        rect_texto = texto.get_rect(topleft=(30, 40))
                        cont_grande = 10
                        colision = True
                        # Pausar efectos de coins

                        if playing_music:
                            coin_sound.play()

                        if len(coins) == 0:
                            load_coins_list(coins, count_coins, image_asteroid_especial)
                            end_level_sound.play()
                if colision == True:
                    laser = False

        if cont_grande > 0:
            cont_grande -= 1
            block["rect"].width = block_width * 1.1
            block["rect"].height = block_height * 1.1
            block["color"] = color_aleatoreo()
        else:
            block["rect"].width = block_width
            block["rect"].height = block_height
            block["color"] = red

        # ----> Dibujar Pantalla
        screen.blit(background, origin)

        dibujar_asteroides(screen, coins)

        # Dibujo el Lase
        if rafaga:
            for laser in lasers:
                pygame.draw.rect(screen, laser["color"], laser["rect"])
        else:
            if laser:
                pygame.draw.rect(screen, laser["color"], laser["rect"])

        screen.blit(block["imagen"], block["rect"])
        screen.blit(texto, rect_texto)
        screen.blit(texto_lives, rect_texto_lives)

        # ----> Actualiza la pantalla
        pygame.display.flip()

    if contador_monedas > max_contador:
        max_contador = contador_monedas

    screen.fill(black)
    pygame.mixer.music.stop()
    game_over_sound.play()

    mostrar_texto(screen, "Game Over", fuente, (width // 2, 20), blue)
    mostrar_texto(
        screen,
        "Presione una tecla para comenzar",
        fuente,
        center_screen,
        white,
    )
    mostrar_texto(
        screen,
        f"max Score: {max_contador}",
        fuente,
        (width // 2, height - 30),
        yellow,
    )
    pygame.display.flip()
    wait_user()  # --> Se escapa de la pausa / menu


terminar()

# TERMINAR POR TIEMPO
# Game Over Por tiempo
# def game_over():
#     clock = pygame.time.Clock()
#     start_time = pygame.time.get_ticks()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()

#         current_time = pygame.time.get_ticks()
#         elapsed_time = (
#             current_time - start_time
#         ) / 1000  # Tiempo transcurrido en segundos

#         if elapsed_time >= 10:
#             main_menu()
#             return  # Sal del bucle para evitar que la función continúe ejecutándose

#         screen.blit(lose_background, (0, 0))
#         game_over_text = f"Game Over {elapsed_time}"
#         screen_text(screen, game_over_text, font, (width // 2, height // 2), white)
#         pygame.display.flip()
#         clock.tick(60)
