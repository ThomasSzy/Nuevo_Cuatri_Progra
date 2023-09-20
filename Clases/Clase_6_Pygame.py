import pygame, sys
#sys Funciones del sistema


# lista -> Elemento entre "[]" -> Mutable
# tupla -> Elemento entre "()" -> inmutable

# l = [3, 4, 5] #-->Se puede modificar
# x = (3, 4, 5) #-->No se puede modificar
#             #Es para leerla

SIZE = (800, 600)
pygame.init()


VENTANA = pygame.display.set_mode(SIZE)
# --> Crea la pantalla

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
