import pygame
from pygame import *
from sys import *
from config_colores import *
from random import randint
from random import randrange
from colisiones import *
from pygame.locals import *


# print(detectar_colision(r1,r2))
# --> Funcion para diccionario


def mostrar_texto(suuperficie, texto, fuente, coordenadas, color_fuente, color_fondo):
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rec_texto = sup_texto.get_rect()
    rec_texto_center = coordenadas
    suuperficie.blit(sup_texto, rect_texto)
    pygame.display.flip()


def terminar():
    pygame.QUIT
    exit()


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
        coins.append(
            crear_bloque(
                imagen,
                left=randint(0, width - size_coin),
                top=randint(0, height - size_coin),
                ancho=size_coin,
                alto=size_coin,
                color=white,
                radio=size_coin // 2,  # --> Las hace redondas
            )
        )


def wait_user():
    while True:
        for event in event.get():
            if event.type == QUIT:  # -> Va con from pygame.locals import *
                terminar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminar()
                return  # --> Terminamos la Funcion


def dibujar_asteroides(suuperficie, coins):
    for coin in coins:
        # pygame.draw.rect(
        #     screen, coin["color"], coin["rect"], coin["borde"], coin["radio"]
        # )

        if coin["imagen"]:
            screen.blit(coin["imagen"], coin["rect"])

        else:
            pygame.draw.rect(
                screen, block["color"], block["rect"], block["borde"], block["radio"]
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

# Cancion de fondo
pygame.mixer.music.load("./src/Sonidos/tetrisgameboy1-gameboy.mp3")

pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.1)
playing_music = True


# Cargo Imagenes

image_player = pygame.image.load("./src/imagenes/ovni.png")
image_asteroid = pygame.image.load("./src/imagenes/asteroid.png")

background = pygame.transform.scale(
    pygame.image.load("./src/imagenes/asteroid.png"), size_screen
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
fuente = pygame.font.SysFont(None, 48)
# 1)Fuente --> None = Arial
# 2)Tamaño

texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
rect_texto = texto.get_rect()
rect_texto.midtop = (width // 2, 30)

block = crear_bloque(
    image_player,
    left=randint(0, width - block_width),
    top=randint(0, height - block_height),
    ancho=block_width,
    alto=block_height,
    color=red,
    radio=25,
)

# Creamos lista de monedas

coins = []
load_coins_list(coins, count_coins)
# for i in range(25):
#     coins.append(crear_bloque(left = randint(0, width - size_coin),
#                                 top = randint(0, height - size_coin),
#                                 ancho = size_coin,
#                                 alto = size_coin,
#                                 color = white,
#                                 radio = size_coin // 2 # --> Las hace redondas
#                                 ))


is_ranning = True

while is_ranning:
    # ----> Tiempo
    clock.tick(FPS)  # -->FPS EN LA LISTA CONFIG
    # ----> Detecta los eventos
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

            if event.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

                playing_music = (
                    not playing_music
                )  # --> Esta bandera la usamos para saber si tiene que sonar o no

            if event.key == K_p:
                if playing_music:
                    pygame.mixer.music.pause()
                mostrar_texto(screen, "Pausa", fuente, center_screen, red, black)
                wait_user()
                if playing_music:
                    pygame.mixer.music.unpause
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

        # CLICK BOTON AGRENGANDO FORMAS DONDE TOQUEMOS
        if event.type == MOUSEBUTTONDOWN:
            # coins.append(crear_bloque(left = event.pos[0] - size_coin // 2 , # --> Dividimos a la mitad porque se genera el el puunto 0,0 del mouse y el rectangulo tiene que ir mas arriba
            #                     top = event.pos[1]- size_coin // 2 ,
            #                     ancho = size_coin,
            #                     alto = size_coin,
            #                     color = blue,
            #                     radio = size_coin // 2 # --> Las hace redondas
            #                     ))
            # Logra lo mismo pero de diferente manera
            if event.button == 1:
                new_coin = crear_bloque(
                    None,
                    left=event.pos[0],
                    top=event.pos[1],
                    ancho=size_coin,
                    alto=size_coin,
                    color=blue,
                    radio=size_coin // 2,  # --> Las hace redondas
                )
                new_coin["rect"].left -= size_coin // 2
                new_coin["rect"].top -= size_coin // 2
                coins.append(new_coin)

                # ENVIAR PERSONAJE AL MEDIO!
            if event.button == 2:
                block["rect"].topleft = center_screen

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

    for coin in coins[:]:
        # ---> Creamos una copia y la modificamos de la lista original
        if detectar_colision_circulo(coin["rect"], block["rect"]):
            coins.remove(coin)
            if (
                coin["color"] == gold
            ):  # --> Si la moneda es color dorado la puntuacion vale doble
                contador_monedas += 2
            else:
                contador_monedas += 1  # --> de lo contrario la moneda sigue valiendo 1

            texto = fuente.render(f"coins: {contador_monedas}", True, magenta)
            # 1)Texto  2)Antialising  3)Color Fuente   4)Color Fondo
            rect_texto = texto.get_rect()
            rect_texto.midtop = (width // 2, 30)
            cont_grande = 10
            coin_sound.play()
            if len(coins) == 0:
                load_coins_list(coins, count_coins, image_asteroid)
                end_level_sound.play()

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

    # screen.fill(black)
    screen.blit(background, origin)

    screen.blit(block["imagen"], block["rect"])
    screen.blit(texto, rect_texto)
    # ----> Actualiza la pantalla
    pygame.display.flip()


terminar()
